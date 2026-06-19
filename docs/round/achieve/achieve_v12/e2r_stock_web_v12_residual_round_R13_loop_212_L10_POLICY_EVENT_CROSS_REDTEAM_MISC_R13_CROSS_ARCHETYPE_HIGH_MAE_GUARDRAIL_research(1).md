# E2R Stock-Web v12 Residual Research — R13 / L10 / High-MAE Guardrail

```text
file_name: e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
research_session: post_calibrated_sector_archetype_residual_research_v12
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R13
selected_loop: 212
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / R13 high-MAE representative compression after recent C10 and C13 source-sector refresh
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 1. Scheduler / Coverage Selection

The main execution prompt is used as the controlling procedure. This file is a **R13 cross-archetype checkpoint**, not a new L2 semiconductor or L3 battery positive study. R13 is allowed only under `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`, and the selected scope is `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`.

The no-repeat index is used only as the duplicate ledger. Its latest snapshot says all C01~C32 canonical archetypes already exceed 80 representative rows, so raw row filling is less useful than direct URL quality, representative compression, false-positive taxonomy, 4B/4C boundary cleanup, and high-MAE guardrail refresh.

This run compresses two recent source-sector refreshes:

```text
source_large_sector_focus:
- L2_AI_SEMICONDUCTOR_ELECTRONICS / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- L3_BATTERY_EV_GREEN_MOBILITY / C13_BATTERY_JV_UTILIZATION_AMPC_IRA

source_sector_case_reused_count: 12
new_independent_case_count_for_r13_scope: 12
new_independent_trigger_count_for_r13_scope: 12
unique_symbol_count: 12
unique_source_canonical_count: 2
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
production_scoring_changed: false
shadow_weight_only: true
```

### Research question

C10 and C13 both create the same mechanical trap. A row can have real evidence — HBM package/test exposure, supplier order route, AMPC/IRA benefit, customer/JV route — and still produce a deep 90D/180D drawdown. The question is whether that high MAE should delete Stage2, or whether it should instead act as a brake against Yellow/Green escalation.

The answer from this holdout batch is narrow:

> **High MAE is usually a Stage escalation brake, not a Stage2 eraser, when issuer-level second bridge evidence survives. But when high MAE combines with weak conversion evidence or confirmed utilization/margin break, the row must stay capped at Stage2, 4B/watch, or hard 4C.**

## 2. Stock-Web Price Validation

```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
raw_shard_used_for_weight: false
mfe_mae_formula: inclusive entry-row max high / min low over 30, 90, 180 tradable rows
corporate_action_contamination_rule: block D~D+180 overlap by default
```

Stock-Web manifest checked:

```json
{
  "atlas_version": "1.0.0",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

## 3. Price-Source Map

| symbol | entry_date | stock-web shard | profile path | window status |
|---|---:|---|---|---|
| `222800` | 2024-01-11 | `atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv` | `atlas/symbol_profiles/222/222800.json` | clean_180D_window |
| `067310` | 2024-02-29 | `atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv` | `atlas/symbol_profiles/067/067310.json` | clean_180D_window |
| `095340` | 2024-02-21 | `atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv` | `atlas/symbol_profiles/095/095340.json` | clean_180D_window |
| `240810` | 2025-02-11 | `atlas/ohlcv_tradable_by_symbol_year/240/240810/2025.csv` | `atlas/symbol_profiles/240/240810.json` | clean_180D_window |
| `036540` | 2025-03-21 | `atlas/ohlcv_tradable_by_symbol_year/036/036540/2025.csv` | `atlas/symbol_profiles/036/036540.json` | clean_180D_window |
| `061970` | 2025-03-20 | `atlas/ohlcv_tradable_by_symbol_year/061/061970/2025.csv` | `atlas/symbol_profiles/061/061970.json` | clean_180D_window |
| `373220` | 2024-10-28 | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv` | `atlas/symbol_profiles/373/373220.json` | clean_180D_window |
| `006400` | 2024-07-30 | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` | `atlas/symbol_profiles/006/006400.json` | clean_180D_window |
| `361610` | 2024-04-30 | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv` | `atlas/symbol_profiles/361/361610.json` | clean_180D_window |
| `020150` | 2024-11-01 | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv` | `atlas/symbol_profiles/020/020150.json` | clean_180D_window |
| `247540` | 2024-07-30 | `atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv` | `atlas/symbol_profiles/247/247540.json` | clean_180D_window |
| `066970` | 2024-11-04 | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` | `atlas/symbol_profiles/066/066970.json` | clean_180D_window |

## 4. Evidence URL Pack

| source canonical | symbol | evidence family | URL | source proxy |
|---|---|---|---|---:|
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `222800` | customer_utilization_forecast_needs_order_or_margin_bridge | https://www.simmtech.com/upload/media/file/638406815140413547.pdf | false |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `067310` | advanced_packaging_technology_route_without_revenue_bridge | https://www.kedglobal.com/korean-chipmakers/newsView/ked202402290006 | false |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `095340` | direct_customer_test_socket_bridge_high_mae_green_blocker | https://www.asiae.co.kr/en/article/2024022012532687968 | false |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `240810` | equipment_revenue_route_needs_order_repeat | https://w4.kirs.or.kr/download/research_eng/%EC%9B%90%EC%9D%B5IPS_EN.pdf | false |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `036540` | backend_package_profile_with_margin_conversion_gap | https://www.sfasemicon.com/en/investor/finance | false |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `061970` | revenue_recovery_without_operating_profit_conversion | https://www.lbsemicon.com/eng/IR.lb | false |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `373220` | 3Q24 OP included KRW466bn IRA credit; ex-IRA loss KRW17.7bn; EV demand outlook/capex discipline. | https://news.lgensol.com/company-news/press-releases/3343/ | false |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `006400` | 2Q24 revenue down 24% YoY, EV utilization/sales declined, but ESS rebound and future projects offset. | https://www.samsungsdi.com/sdi-now/sdi-news/3862.html | false |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `361610` | 1Q24 revenue -73% QoQ, operating loss KRW67.4bn, utilization/shipment collapse tied to SK On demand. | https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220 | false |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `020150` | 3Q24 operating loss KRW31.7bn after production/sales decline, FX and inventory valuation losses; North America growth only medium-term offset. | https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=108 | false |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `247540` | 2Q24/2024 battery-material weakness, inventory valuation burden and downstream slowdown; no utilization/ex-margin bridge. | https://www.ecopro.co.kr/eng/ir | false |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `066970` | High-nickel cathode supply route to Tesla/affiliates; direct customer bridge but severe forward MAE keeps Yellow/Green blocked. | https://www.kedglobal.com/batteries/newsView/ked202411030003 | false |

## 5. Selected Representative Trigger Rows

| # | source canonical | symbol | company | trigger_type | entry_date | entry close | entry OHLCV | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | residual role |
|---:|---|---|---|---|---:|---:|---|---:|---:|---:|---|
| 1 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `222800` | Simmtech | Stage2 | 2024-01-11 | 38,800 | `o=39,250 h=39,500 l=38,600 c=38,800 v=354,220` | 1.80/-17.01 | 28.35/-17.01 | 38.92/-25.52 | forecast_bridge_counterexample |
| 2 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `067310` | Hana Micron | Stage2 | 2024-02-29 | 25,900 | `o=25,000 h=26,550 l=24,700 c=25,900 v=2,028,485` | 18.34/-4.63 | 46.33/-13.13 | 46.33/-41.70 | technology_route_counterexample |
| 3 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `095340` | ISC | Stage2-Actionable | 2024-02-21 | 73,200 | `o=73,600 h=74,800 l=72,900 c=73,200 v=127,475` | 52.46/-5.87 | 81.15/-12.70 | 92.08/-24.32 | positive_control |
| 4 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `240810` | Wonik IPS | Stage2-Actionable | 2025-02-11 | 25,950 | `o=24,050 h=27,250 l=23,500 c=25,950 v=1,854,019` | 10.79/-19.85 | 23.31/-19.85 | 45.66/-19.85 | equipment_revenue_bridge |
| 5 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `036540` | SFA Semicon | Stage4B | 2025-03-21 | 3,220 | `o=3,210 h=3,310 l=3,190 c=3,220 v=1,066,162` | 3.73/-11.49 | 15.53/-11.49 | 38.20/-16.15 | margin_conversion_guardrail |
| 6 | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | `061970` | LB Semicon | Stage4B | 2025-03-20 | 3,795 | `o=3,825 h=3,840 l=3,795 c=3,795 v=38,456` | 1.84/-15.94 | 10.67/-15.94 | 33.60/-15.94 | revenue_without_margin_counterexample |
| 7 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `373220` | LG Energy Solution | Stage4B | 2024-10-28 | 416,500 | `o=403,000 h=417,500 l=403,000 c=416,500 v=360,352` | 4.56/-10.92 | 4.56/-21.37 | 4.56/-36.13 | C13_AMPC_IRA_JV_direct_bridge_quality_repair |
| 8 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `006400` | Samsung SDI | Stage4B | 2024-07-30 | 330,500 | `o=333,000 h=344,500 l=330,500 c=330,500 v=423,808` | 14.98/-10.89 | 19.06/-28.74 | 19.06/-48.56 | C13_AMPC_IRA_JV_direct_bridge_quality_repair |
| 9 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `361610` | SK IE Technology | Stage4C | 2024-04-30 | 59,100 | `o=62,100 h=62,200 l=58,600 c=59,100 v=661,182` | 5.25/-27.75 | 5.25/-48.73 | 5.25/-63.03 | C13_AMPC_IRA_JV_direct_bridge_quality_repair |
| 10 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `020150` | LOTTE Energy Materials | Stage4C | 2024-11-01 | 36,300 | `o=37,300 h=37,550 l=35,600 c=36,300 v=141,288` | 3.44/-42.42 | 3.44/-44.21 | 3.44/-46.39 | C13_AMPC_IRA_JV_direct_bridge_quality_repair |
| 11 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `247540` | EcoPro BM | Stage4C | 2024-07-30 | 187,500 | `o=177,100 h=190,000 l=176,100 c=187,500 v=927,485` | 2.35/-20.69 | 3.73/-35.79 | 3.73/-53.60 | C13_AMPC_IRA_JV_direct_bridge_quality_repair |
| 12 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `066970` | L&F | Stage2-Actionable | 2024-11-04 | 112,000 | `o=114,800 h=119,000 l=108,300 c=112,000 v=750,031` | 12.77/-17.68 | 12.77/-37.41 | 12.77/-58.04 | C13_AMPC_IRA_JV_direct_bridge_quality_repair |

## 6. Source-Canonical Holdout Matrix

| source canonical | selected rows | high-MAE rows | main residual |
|---|---:|---:|---|
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | 6 | 3 | memory/HBM/package/test profile must become issuer-level supplier order, shipment, recognized revenue, margin, or repeat reorder before Actionable/Yellow. |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | 6 | 6 | AMPC/IRA/JV/customer route must become utilization, eligible production volume, shipment, ex-subsidy margin, or customer pull before positive escalation. |

```text
stage2_count: 2
stage2_actionable_count: 3
stage4b_count: 4
stage4c_count: 3
high_MAE_180D_count: 9
deep_MAE_180D_count: 6
positive_or_direct_bridge_control_count: 3
counterexample_or_guardrail_count: 9
```

## 7. Case Interpretation

### C10 semiconductor supplier conversion

C10 rows show why memory-cycle evidence must be split into three layers.

1. **Customer/macro recovery layer**: memory recovery, HBM capex, DDR5 substrate, or advanced-packaging theme. This is valid Stage2 input but not enough for Actionable.
2. **Issuer-level conversion layer**: direct supplier order, shipment, named customer qualification, revenue conversion, margin conversion, or repeat reorder. This is the minimum for Stage2-Actionable.
3. **Escalation layer**: multiple evidence families showing margin/cashflow/repeat order durability. Without this layer, high MAE blocks Yellow/Green even when 180D MFE is attractive.

Simmtech and Hana Micron are useful profile / technology-route rows: the narrative is real, but the conversion bridge is not yet fully proven. ISC is the positive control because AI/HBM test-socket evidence is closer to issuer-level customer route. Wonik IPS is Actionable only when treated as an equipment revenue conversion row, not as generic customer capex beta. SFA Semicon and LB Semicon show why backend package/test revenue without operating-profit conversion should route to local 4B/watch.

### C13 battery utilization and ex-subsidy quality

C13 rows show the subsidy/JV mirror image of the C10 trap. LG Energy Solution reported positive operating profit, but the IRA credit exceeded reported operating profit, so the row should block Green until ex-credit economics are visible. Samsung SDI had EV slowdown but ESS/project offset, so 4B/watch is better than sticky hard 4C. SK IE Technology, LOTTE Energy Materials, and EcoPro BM are hard 4C / severe watch controls because utilization, operating loss, inventory valuation, or downstream-demand break are directly visible. L&F keeps Stage2-Actionable because a direct customer bridge survives, but deep MAE blocks Yellow/Green.

## 8. Current Profile Stress Test

| stress axis | observed result | residual verdict |
|---|---|---|
| C10 profile-only rows | strong MFE can appear after technology/profile rows, but MAE is often deep | preserve Stage2 cap; do not promote to Actionable without issuer-level conversion |
| C10 direct supplier rows | direct customer/order/revenue bridge can survive high MAE | preserve Stage2-Actionable; block Yellow/Green |
| C13 subsidy-supported OP | reported OP may be lower quality than it looks when AMPC/IRA exceeds OP | keep Green blocked until ex-credit margin/utilization appears |
| C13 utilization/margin break | direct utilization/shipment collapse aligns with deep MAE | protect Stage4C when non-price thesis break is confirmed |
| high MAE generally | high MAE alone is not a thesis break | use as escalation brake before using it as bearish deletion |

```text
current_profile_error_count: 9
current_profile_false_positive_risk_count: 6
current_profile_too_late_risk_count: 1
hard_4c_correct_control_count: 3
stage2_preservation_control_count: 3
```

## 9. Shadow Rule Candidate

```text
rule_candidate:
R13_HIGH_MAE_SUPPLIER_CONVERSION_ESCALATION_BRAKE_GATE_V1

core residual:
- High MAE is not a universal Stage2 deletion signal.
- If issuer-level direct second bridge survives, Stage2 / Stage2-Actionable is preserved.
- High MAE plus missing repeat order, margin, utilization, cashflow, or ex-subsidy economics blocks Stage3-Yellow / Stage3-Green first.
- Product profile, technology-development route, macro memory recovery, AMPC/IRA/JV wording, or North America optionality stays capped until conversion evidence appears.
- Hard Stage4C still requires confirmed non-price thesis break: utilization collapse, order cancellation, customer call-off, operating loss with weak offset, inventory valuation break, accounting/trust break, or margin thesis failure.
- Do not loosen Stage3-Green globally.
```

### Runtime boundary

This R13 file does not propose direct production scoring changes. It is a holdout compression MD. The future coding agent should ingest it only as R13 representative evidence when validating whether existing `stage2_required_bridge`, `local_4b_watch_guard`, `hard_4c_confirmation`, and `stage3_green_not_loosened` axes remain internally consistent across L2 and L3.

## 10. Machine-readable JSONL

```jsonl
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "Simmtech", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-01-11", "entry_ohlcv": {"c": 38800.0, "d": "2024-01-11", "h": 39500.0, "l": 38600.0, "m": "KOSDAQ", "o": 39250.0, "v": 354220.0}, "entry_price": 38800.0, "evidence_summary": "customer_utilization_forecast_needs_order_or_margin_bridge", "evidence_url": "https://www.simmtech.com/upload/media/file/638406815140413547.pdf", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -25.52, "mae_30d_pct": -17.01, "mae_90d_pct": -17.01, "mfe_180d_pct": 38.92, "mfe_30d_pct": 1.8, "mfe_90d_pct": 28.35, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/222/222800.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|222800|Stage2|2024-01-11", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_fine_archetype_id": "C10_PACKAGE_TEST_INTERFACE_SUPPLIER_ORDER_CONVERSION_GATE_V7", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R2_loop_207_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_sector_case_reused": true, "symbol": "222800", "trigger_type": "Stage2"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "Hana Micron", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-02-29", "entry_ohlcv": {"c": 25900.0, "d": "2024-02-29", "h": 26550.0, "l": 24700.0, "m": "KOSDAQ GLOBAL", "o": 25000.0, "v": 2028485.0}, "entry_price": 25900.0, "evidence_summary": "advanced_packaging_technology_route_without_revenue_bridge", "evidence_url": "https://www.kedglobal.com/korean-chipmakers/newsView/ked202402290006", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -41.7, "mae_30d_pct": -4.63, "mae_90d_pct": -13.13, "mfe_180d_pct": 46.33, "mfe_30d_pct": 18.34, "mfe_90d_pct": 46.33, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/067/067310.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|067310|Stage2|2024-02-29", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_fine_archetype_id": "C10_PACKAGE_TEST_INTERFACE_SUPPLIER_ORDER_CONVERSION_GATE_V7", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R2_loop_207_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_sector_case_reused": true, "symbol": "067310", "trigger_type": "Stage2"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "ISC", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-02-21", "entry_ohlcv": {"c": 73200.0, "d": "2024-02-21", "h": 74800.0, "l": 72900.0, "m": "KOSDAQ", "o": 73600.0, "v": 127475.0}, "entry_price": 73200.0, "evidence_summary": "direct_customer_test_socket_bridge_high_mae_green_blocker", "evidence_url": "https://www.asiae.co.kr/en/article/2024022012532687968", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -24.32, "mae_30d_pct": -5.87, "mae_90d_pct": -12.7, "mfe_180d_pct": 92.08, "mfe_30d_pct": 52.46, "mfe_90d_pct": 81.15, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/095/095340.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|095340|Stage2-Actionable|2024-02-21", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_fine_archetype_id": "C10_PACKAGE_TEST_INTERFACE_SUPPLIER_ORDER_CONVERSION_GATE_V7", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R2_loop_207_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_sector_case_reused": true, "symbol": "095340", "trigger_type": "Stage2-Actionable"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "Wonik IPS", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2025-02-11", "entry_ohlcv": {"c": 25950.0, "d": "2025-02-11", "h": 27250.0, "l": 23500.0, "m": "KOSDAQ GLOBAL", "o": 24050.0, "v": 1854019.0}, "entry_price": 25950.0, "evidence_summary": "equipment_revenue_route_needs_order_repeat", "evidence_url": "https://w4.kirs.or.kr/download/research_eng/%EC%9B%90%EC%9D%B5IPS_EN.pdf", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -19.85, "mae_30d_pct": -19.85, "mae_90d_pct": -19.85, "mfe_180d_pct": 45.66, "mfe_30d_pct": 10.79, "mfe_90d_pct": 23.31, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2025.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/240/240810.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "non_high_mae_positive_control", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|240810|Stage2-Actionable|2025-02-11", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_fine_archetype_id": "C10_PACKAGE_TEST_INTERFACE_SUPPLIER_ORDER_CONVERSION_GATE_V7", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R2_loop_207_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_sector_case_reused": true, "symbol": "240810", "trigger_type": "Stage2-Actionable"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "SFA Semicon", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2025-03-21", "entry_ohlcv": {"c": 3220.0, "d": "2025-03-21", "h": 3310.0, "l": 3190.0, "m": "KOSDAQ", "o": 3210.0, "v": 1066162.0}, "entry_price": 3220.0, "evidence_summary": "backend_package_profile_with_margin_conversion_gap", "evidence_url": "https://www.sfasemicon.com/en/investor/finance", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -16.15, "mae_30d_pct": -11.49, "mae_90d_pct": -11.49, "mfe_180d_pct": 38.2, "mfe_30d_pct": 3.73, "mfe_90d_pct": 15.53, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036540/2025.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036540.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "non_high_mae_positive_control", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|036540|Stage4B|2025-03-21", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_fine_archetype_id": "C10_PACKAGE_TEST_INTERFACE_SUPPLIER_ORDER_CONVERSION_GATE_V7", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R2_loop_207_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_sector_case_reused": true, "symbol": "036540", "trigger_type": "Stage4B"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "LB Semicon", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2025-03-20", "entry_ohlcv": {"c": 3795.0, "d": "2025-03-20", "h": 3840.0, "l": 3795.0, "m": "KOSDAQ", "o": 3825.0, "v": 38456.0}, "entry_price": 3795.0, "evidence_summary": "revenue_recovery_without_operating_profit_conversion", "evidence_url": "https://www.lbsemicon.com/eng/IR.lb", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -15.94, "mae_30d_pct": -15.94, "mae_90d_pct": -15.94, "mfe_180d_pct": 33.6, "mfe_30d_pct": 1.84, "mfe_90d_pct": 10.67, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/061/061970/2025.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/061/061970.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "non_high_mae_positive_control", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|061970|Stage4B|2025-03-20", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_fine_archetype_id": "C10_PACKAGE_TEST_INTERFACE_SUPPLIER_ORDER_CONVERSION_GATE_V7", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R2_loop_207_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_sector_case_reused": true, "symbol": "061970", "trigger_type": "Stage4B"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "LG Energy Solution", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-10-28", "entry_ohlcv": {"a": 148639841500.0, "c": 416500.0, "h": 417500.0, "l": 403000.0, "m": "KOSPI", "mc": 97461000000000.0, "o": 403000.0, "s": 234000000, "v": 360352.0}, "entry_price": 416500.0, "evidence_summary": "3Q24 OP included KRW466bn IRA credit; ex-IRA loss KRW17.7bn; EV demand outlook/capex discipline.", "evidence_url": "https://news.lgensol.com/company-news/press-releases/3343/", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -36.13, "mae_30d_pct": -10.92, "mae_90d_pct": -21.37, "mfe_180d_pct": 4.56, "mfe_30d_pct": 4.56, "mfe_90d_pct": 4.56, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/373/373220.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|373220|Stage4B|2024-10-28", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_sector_case_reused": true, "symbol": "373220", "trigger_type": "Stage4B"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "Samsung SDI", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-07-30", "entry_ohlcv": {"a": 141982847000.0, "c": 330500.0, "h": 344500.0, "l": 330500.0, "m": "KOSPI", "mc": 22726677165000.0, "o": 333000.0, "s": 68764530, "v": 423808.0}, "entry_price": 330500.0, "evidence_summary": "2Q24 revenue down 24% YoY, EV utilization/sales declined, but ESS rebound and future projects offset.", "evidence_url": "https://www.samsungsdi.com/sdi-now/sdi-news/3862.html", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -48.56, "mae_30d_pct": -10.89, "mae_90d_pct": -28.74, "mfe_180d_pct": 19.06, "mfe_30d_pct": 14.98, "mfe_90d_pct": 19.06, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006400.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006400|Stage4B|2024-07-30", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_sector_case_reused": true, "symbol": "006400", "trigger_type": "Stage4B"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "SK IE Technology", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-04-30", "entry_ohlcv": {"a": 39337486300.0, "c": 59100.0, "h": 62200.0, "l": 58600.0, "m": "KOSPI", "mc": 4213687687200.0, "o": 62100.0, "s": 71297592, "v": 661182.0}, "entry_price": 59100.0, "evidence_summary": "1Q24 revenue -73% QoQ, operating loss KRW67.4bn, utilization/shipment collapse tied to SK On demand.", "evidence_url": "https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -63.03, "mae_30d_pct": -27.75, "mae_90d_pct": -48.73, "mfe_180d_pct": 5.25, "mfe_30d_pct": 5.25, "mfe_90d_pct": 5.25, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|361610|Stage4C|2024-04-30", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_sector_case_reused": true, "symbol": "361610", "trigger_type": "Stage4C"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "LOTTE Energy Materials", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-11-01", "entry_ohlcv": {"a": 5150177000.0, "c": 36300.0, "h": 37550.0, "l": 35600.0, "m": "KOSPI", "mc": 1673823310500.0, "o": 37300.0, "s": 46110835, "v": 141288.0}, "entry_price": 36300.0, "evidence_summary": "3Q24 operating loss KRW31.7bn after production/sales decline, FX and inventory valuation losses; North America growth only medium-term offset.", "evidence_url": "https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=108", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -46.39, "mae_30d_pct": -42.42, "mae_90d_pct": -44.21, "mfe_180d_pct": 3.44, "mfe_30d_pct": 3.44, "mfe_90d_pct": 3.44, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020150.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|020150|Stage4C|2024-11-01", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_sector_case_reused": true, "symbol": "020150", "trigger_type": "Stage4C"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "EcoPro BM", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-07-30", "entry_ohlcv": {"a": 173052220500.0, "c": 187500.0, "h": 190000.0, "l": 176100.0, "m": "KOSDAQ GLOBAL", "mc": 18337752000000.0, "o": 177100.0, "s": 97801344, "v": 927485.0}, "entry_price": 187500.0, "evidence_summary": "2Q24/2024 battery-material weakness, inventory valuation burden and downstream slowdown; no utilization/ex-margin bridge.", "evidence_url": "https://www.ecopro.co.kr/eng/ir", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -53.6, "mae_30d_pct": -20.69, "mae_90d_pct": -35.79, "mfe_180d_pct": 3.73, "mfe_30d_pct": 2.35, "mfe_90d_pct": 3.73, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/247/247540.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|247540|Stage4C|2024-07-30", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_sector_case_reused": true, "symbol": "247540", "trigger_type": "Stage4C"}
{"calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "company": "L&F", "dedupe_for_aggregate": true, "do_not_count_as_new_source_sector_case": true, "do_not_propose_new_weight_delta": true, "entry_date": "2024-11-04", "entry_ohlcv": {"a": 84784648800.0, "c": 112000.0, "h": 119000.0, "l": 108300.0, "m": "KOSPI", "mc": 4065189856000.0, "o": 114800.0, "s": 36296338, "v": 750031.0}, "entry_price": 112000.0, "evidence_summary": "High-nickel cathode supply route to Tesla/affiliates; direct customer bridge but severe forward MAE keeps Yellow/Green blocked.", "evidence_url": "https://www.kedglobal.com/batteries/newsView/ked202411030003", "evidence_url_pending": false, "fine_archetype_id": "R13_L2_L3_SUPPLIER_CONVERSION_HIGH_MAE_HOLDOUT_REFRESH_V1", "independent_evidence_weight_for_source_sector": 0.0, "is_new_independent_case_for_r13_scope": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "mae_180d_pct": -58.04, "mae_30d_pct": -17.68, "mae_90d_pct": -37.41, "mfe_180d_pct": 12.77, "mfe_30d_pct": 12.77, "mfe_90d_pct": 12.77, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv", "corporate_action_contamination_180D": false, "insufficient_forward_window_180D": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "primary_price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/066/066970.json", "stock_web_manifest_max_date": "2026-02-20"}, "production_scoring_changed": false, "r13_holdout_bucket": "high_mae_escalation_brake", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md", "residual_contribution": {"hard_4c_requires_non_price_thesis_break": true, "label": "R13_high_MAE_supplier_conversion_is_stage_escalation_brake_not_stage2_deletion_v1", "stage2_preserved_if_direct_second_bridge_exists": true, "stage3_green_blocked_by_high_MAE_or_missing_cashflow_margin_bridge": true}, "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|066970|Stage2-Actionable|2024-11-04", "schema_version": "e2r_v12_r13_cross_case_v1", "selected_loop": 212, "selected_round": "R13", "shadow_weight_only": true, "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_proxy_only": false, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_sector_case_reused": true, "symbol": "066970", "trigger_type": "Stage2-Actionable"}
```

## 11. Batch Ingest Self-Audit

```text
required_filename_regex_pass: true
filename_round_matches_metadata_round: true
filename_loop_matches_metadata_loop: true
round_sector_consistency: pass
r13_large_sector_gate: pass
r13_scope_allowed: true
canonical_archetype_id_valid: true
large_sector_id_valid: true
selected_round: R13
selected_loop: 212
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / R13 representative high-MAE compression
hard_duplicate_key_schema: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL + symbol + trigger_type + entry_date
trigger_rows_missing_required_price_fields: 0
trigger_rows_missing_30_90_180_mfe_mae: 0
trigger_rows_with_invalid_price_source: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
usable_trigger_rows: 12
representative_trigger_rows: 12
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later coding-agent task:
1. Ingest this MD with the rest of docs/round using the v12 calibration pipeline.
2. Treat all rows as R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL representative holdout rows.
3. Do not count these rows as new C10 or C13 independent source-sector evidence.
4. Validate whether high MAE should remain a Stage3-Yellow/Stage3-Green escalation brake rather than a Stage2 deletion rule when direct second bridge survives.
5. Compare against existing axes:
   - stage2_required_bridge
   - local_4b_watch_guard
   - hard_4c_confirmation
   - stage3_green_not_loosened
6. Do not loosen Stage3-Green globally.
7. Do not use future MFE/MAE at runtime.
8. Production scoring remains unchanged until batch validation passes.
```

## 13. Next Research State

```text
completed_round: R13
completed_loop: 212
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / R13 high-MAE representative compression after C10/C13 refresh
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
