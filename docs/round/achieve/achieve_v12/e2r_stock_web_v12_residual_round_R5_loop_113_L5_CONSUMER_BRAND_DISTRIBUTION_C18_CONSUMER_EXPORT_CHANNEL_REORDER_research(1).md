# E2R Stock-Web V12 Residual Research — R5 Loop 113 / L5 / C18

```yaml
research_file: e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 113
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_MARGIN_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE
execution_date_kst: 2026-06-11
stock_web_manifest_max_date: 2026-02-20
price_basis: stock-web tradable_raw OHLCV, raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
symbol_profile_root: atlas/symbol_profiles
production_scoring_patch_applied: false
research_output_only: true
```

## 1. Scheduler / No-Repeat selection audit

`V12_Research_No_Repeat_Index.md` was used only as the duplicate-prevention and coverage-priority ledger. The highest-priority under-covered canonical was `C18_CONSUMER_EXPORT_CHANNEL_REORDER`: current representative coverage was only 3 rows, with top covered C18 symbols `003230`, `011150`, and `383220`. The loop registry showed existing C18 research through loop 112, so this execution uses loop 113.

This run intentionally avoids those already-dense/known C18 symbols and adds five new symbols:

- `005180` Binggrae
- `280360` Lotte Wellfood
- `271560` Orion
- `001680` Daesang
- `004370` Nongshim

Hard duplicate key checked conceptually: `canonical_archetype_id + symbol + trigger_type + entry_date`. No selected row is a duplicate of the three currently covered C18 symbols.

## 2. Research thesis

C18 should not treat every food or consumer export headline as a rerating trigger. The useful split is:

1. **Real repeat-demand + margin bridge:** overseas sales, local subsidiary growth, distribution expansion, and operating-profit/revision confirmation move together. These can support Stage3-Yellow or Stage3-Green.
2. **Export label without company-level conversion:** channel breadth or one product export headline appears, but no margin/FCF/revision bridge appears. These should remain Stage2 or become false-positive review rows.
3. **Export rerating after crowding:** the initial trigger is real and produces high MFE, but post-peak drawdown is large. These require a 4B local-peak guard rather than permanent positive-stage treatment.

## 3. Source evidence summary

|Symbol|Trigger date|Source summary|Source URL|
|---|---|---|---|
|005180|2024-05-17|Binggrae stock target lifted on overseas refrigerated/frozen export growth|https://www.asiae.co.kr/en/article/2024051707591021574|
|280360|2024-02-07|Lotte Wellfood 2023 operating profit rises on global operations and business improvement|https://www.asiae.co.kr/en/article/2024020715233725800|
|271560|2025-02-27|Orion Choco Pie global sales exceed 4 billion units in 2024|https://www.asiae.co.kr/en/article/2025022709121804606|
|001680|2024-06-13|Korean kimchi exports to US and Daesang/Jongga distribution expansion|https://www.investkorea.org/ik-en/bbs/i-5073/detail.do?ntt_sn=492578|
|004370|2024-03-14|Nongshim posts record sales/operating profit and overseas profit growth|https://www.mk.co.kr/en/business/10964315|

Additional validation source for `004370`: Yonhap, 2025-02-12, reported 2024 operating-profit pressure from higher costs, weak won, and sluggish domestic demand, which validates the post-spike 4B overlay rather than the initial trigger.

## 4. Stock-web price-path validation

Entry rule: first tradable close after trigger date. MFE/MAE rule: from entry close to highest high / lowest low in the following 30, 90, and 180 trading-day windows, inclusive of the entry row. All rows are `calibration_usable=true`, have complete 30D/90D/180D MFE and MAE fields, and have complete forward windows before the stock-web manifest max date `2026-02-20`.

|Symbol|Company|Role|Trigger|Entry|Entry close|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|Peak180|Peak price|DD after peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|005180|Binggrae Co., Ltd.|4B_after_positive_spike|2024-05-17|2024-05-20|87,200|35.78|-5.05|35.78|-32.11|35.78|-32.11|2024-06-11|118,400|-50.0|
|280360|Lotte Wellfood Co., Ltd.|positive_structural_success|2024-02-07|2024-02-08|123,000|11.79|-6.26|69.51|-6.26|69.51|-6.26|2024-06-18|208,500|-44.12|
|271560|Orion Corp.|positive_structural_success|2025-02-27|2025-02-28|101,900|21.2|-0.88|24.93|-0.88|24.93|-2.85|2025-05-09|127,300|-22.23|
|001680|Daesang Corp.|counterexample_failed_rerating|2024-06-13|2024-06-14|29,400|5.1|-18.37|5.1|-33.37|5.1|-37.79|2024-06-17|30,900|-40.81|
|004370|Nongshim Co., Ltd.|4B_after_positive_spike|2024-03-14|2024-03-15|362,500|10.9|-1.93|65.24|-1.93|65.24|-12.55|2024-06-13|599,000|-47.08|

### Corporate-action contamination check

- `005180`: symbol profile showed old corporate-action candidates only before 1999; 2024-2025 forward window treated as clean.
- `280360`: corporate-action candidate dates were 2019-01-04 and 2022-07-20; 2024 forward window treated as clean.
- `271560`: no corporate-action candidate dates in symbol profile; 2025 forward window treated as clean.
- `001680`: old corporate-action candidates were pre-2006; 2024-2025 forward window treated as clean.
- `004370`: old corporate-action candidates were 1997/2000/2003; 2024 forward window treated as clean.

## 5. Case-level interpretation

### 5.1 `280360` Lotte Wellfood — structural positive

The trigger had the right C18 structure: global operations were not merely a slogan; they were tied to operating-profit expansion and business-structure improvement. The 90D path was `MFE +69.51% / MAE -6.26%`, which is the cleanest C18 success row in this batch. The current profile should promote this faster when overseas subsidiary improvement and margin bridge appear together.

Recommended label: `Stage3-Green`.

### 5.2 `271560` Orion — structural positive / repeat-demand route

The Choco Pie row is a repeat-demand and global-localization case: high global unit volume, overseas sales concentration, and local production across China/Vietnam/Russia/India. The 90D path was `MFE +24.93% / MAE -0.88%`; the 180D MAE stayed only `-2.85%`. This is not a one-day export headline. It is a durable channel/repeat-demand row.

Recommended label: `Stage3-Yellow -> Stage3-Green candidate`.

### 5.3 `001680` Daesang — counterexample / false positive guard

The trigger looked attractive because US kimchi channel expansion and distribution breadth were visible. However, the price path was `MFE_90D +5.10% / MAE_90D -33.37%` and `MFE_180D +5.10% / MAE_180D -37.79%`. C18 should not award Stage3 merely because a brand is present in US retail channels. It must see company-level margin/revision/FCF confirmation.

Recommended label: `Stage2-Actionable only / false-positive review`.

### 5.4 `005180` Binggrae — real trigger, but 4B after spike

The export data were real enough to create `MFE_30D +35.78%`, but the same row had `MAE_90D -32.11%` and a `-50.00%` drawdown from the 180D peak. This is a classic C18 problem: the export trigger was not fake, but the model must stop carrying it as a clean positive after local-price crowding and drawdown appear.

Recommended label: `Stage3-Yellow + 4B-watch`.

### 5.5 `004370` Nongshim — structural success, then 4B overlay

This case confirms why the profile should not be binary. The initial evidence was excellent: overseas subsidiaries drove operating-profit growth and the path delivered `MFE_90D +65.24% / MAE_90D -1.93%`. But the same route later suffered a `-47.08%` drawdown from the 180D peak, and subsequent margin/cost pressure confirmed the need for a 4B overlay after the export-rerating spike.

Recommended label: `Stage3-Green initially; 4B-watch after peak/cost-pressure evidence`.

## 6. Score-return alignment

|Symbol|Stage before|Score before|Stage after|Score after|Profile verdict|Alignment|
|---|---|---|---|---|---|---|
|005180|Stage3-Yellow|78.0|Stage3-Yellow + 4B-watch|76.5|4B_too_late_if_export_label_not_peak_checked|high_MFE_but_high_MAE_requires_4B_watch|
|280360|Stage3-Yellow|79.0|Stage3-Green|88.0|missed_or_too_late_structural_promotion|strong_positive_low_MAE|
|271560|Stage3-Yellow|81.0|Stage3-Green_candidate|87.5|underweights_global_localized_repeat_demand|positive_low_MAE_structural_repeat_demand|
|001680|Stage3-Yellow_candidate|75.0|Stage2-Actionable_only|61.0|false_positive_if_channel_reach_overweighted|counterexample_high_MAE_low_MFE|
|004370|Stage3-Green_candidate|88.0|Stage3-Green_then_4B-watch|82.0|needs_peak_after_export_repricing_guard|strong_90D_positive_then_4B_needed|

### Aggregate read

```json
{
  "research_file": "e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md",
  "selected_round": "R5",
  "selected_loop": 113,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "pre_run_index_priority": "Priority 0 / #1 under-covered canonical; C18 rows=3, need_to_30=27, need_to_50=47",
  "previous_top_c18_symbols": [
    "003230",
    "011150",
    "383220"
  ],
  "new_symbols_added": [
    "005180",
    "280360",
    "271560",
    "001680",
    "004370"
  ],
  "positive_case_count": 2,
  "counterexample_count": 1,
  "stage4b_case_count": 2,
  "stage4c_case_count": 0,
  "calibration_usable_rows": 5,
  "representative_rows": 5,
  "avg_MFE_90D_pct_all": 40.11,
  "avg_MAE_90D_pct_all": -14.91,
  "stock_web_manifest_max_date": "2026-02-20",
  "next_recommended_archetype": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL"
}
```

## 7. Shadow rule proposal for C18

### 7.1 Promotion rule

Promote C18 from Stage2 to Stage3-Yellow/Green only when at least two of the following are present:

1. overseas channel expansion or channel reorder evidence;
2. repeat-demand evidence, not only initial shipment/export headlines;
3. operating-profit, margin, or revision bridge;
4. overseas subsidiary/local production/distribution route that reduces one-off export risk;
5. low channel-stuffing/inventory risk.

### 7.2 False-positive guard

Do not allow Stage3-Green when the only strong evidence is overseas retail footprint or category-level export data and the company-level margin/revision bridge is missing. This specifically blocks the Daesang-style row.

### 7.3 4B overlay

If a C18 row has already generated `MFE_30D >= +25%` or `MFE_90D >= +40%`, then trigger a 4B-watch overlay when any of the following occurs:

- post-peak drawdown exceeds `-35%`;
- subsequent earnings/cost evidence breaks the margin bridge;
- valuation repricing rises faster than confirmed repeat-demand/revision evidence;
- relative-strength reversal appears after export-label crowding.

This does not retroactively invalidate the initial Stage3 signal. It only prevents the model from carrying a stale positive-stage label after the local rerating has already matured.

## 8. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
selected_round: R5
selected_loop: 113
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
stock_web_manifest_max_date: 2026-02-20
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
positive_case_count: 2
counterexample_count: 1
stage4b_case_count: 2
stage4c_case_count: 0
source_proxy_only_rows: 0
future_data_leakage_detected: false
production_code_patch_included: false
production_scoring_patch_applied: false
```

## 9. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_date": "2024-09-09", "MAE_180D_pct": -32.11, "MAE_180D_price": 59200.0, "MAE_30D_date": "2024-06-03", "MAE_30D_pct": -5.05, "MAE_30D_price": 82800.0, "MAE_90D_date": "2024-09-09", "MAE_90D_pct": -32.11, "MAE_90D_price": 59200.0, "MFE_180D_date": "2024-06-11", "MFE_180D_pct": 35.78, "MFE_180D_price": 118400.0, "MFE_30D_date": "2024-06-11", "MFE_30D_pct": 35.78, "MFE_30D_price": 118400.0, "MFE_90D_date": "2024-06-11", "MFE_90D_pct": 35.78, "MFE_90D_price": 118400.0, "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_role": "4B_after_positive_spike", "company": "Binggrae Co., Ltd.", "corporate_action_contamination": false, "current_profile_verdict": "4B_too_late_if_export_label_not_peak_checked", "drawdown_after_peak_pct": -50.0, "entry_date": "2024-05-20", "entry_price": 87200.0, "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_MARGIN_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE", "forward_window_complete": true, "future_data_leakage_check": "trigger evidence dated <= trigger_date; price path used only for calibration labels", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "market": "KOSPI", "peak_180D_date": "2024-06-11", "peak_180D_price": 118400.0, "post_peak_trough_date": "2024-09-09", "post_peak_trough_price": 59200.0, "price_basis": "stock-web tradable_raw OHLCV; raw_unadjusted_marcap", "raw_component_scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 40, "channel_reorder_score": 84, "contract_score": 38, "customer_quality_score": 78, "dilution_cb_risk_score": 0, "execution_risk_score": 48, "inventory_or_channel_stuffing_risk_score": 56, "legal_or_contract_risk_score": 10, "margin_bridge_score": 69, "overseas_distribution_route_score": 76, "policy_or_regulatory_score": 10, "relative_strength_score": 95, "revision_score": 75, "valuation_repricing_score": 63}, "raw_component_scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 40, "channel_reorder_score": 84, "contract_score": 38, "customer_quality_score": 77, "dilution_cb_risk_score": 0, "execution_risk_score": 38, "inventory_or_channel_stuffing_risk_score": 42, "legal_or_contract_risk_score": 10, "margin_bridge_score": 67, "overseas_distribution_route_score": 76, "policy_or_regulatory_score": 10, "relative_strength_score": 91, "revision_score": 73, "valuation_repricing_score": 80}, "representative_row": true, "research_file": "e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "row_id": "R5L113-C18-005180-20240520", "score_return_alignment": "high_MFE_but_high_MAE_requires_4B_watch", "selected_loop": 113, "selected_round": "R5", "source_url": "https://www.asiae.co.kr/en/article/2024051707591021574", "stage_label_after": "Stage3-Yellow + 4B-watch", "stage_label_before": "Stage3-Yellow", "symbol": "005180", "trigger_date": "2024-05-17", "trigger_type": "Stage2-Actionable_to_4B_overlay", "weighted_score_after": 76.5, "weighted_score_before": 78.0, "window_180D_end_date": "2025-02-17", "window_30D_end_date": "2024-07-02", "window_90D_end_date": "2024-09-30"}
{"MAE_180D_date": "2024-03-21", "MAE_180D_pct": -6.26, "MAE_180D_price": 115300.0, "MAE_30D_date": "2024-03-21", "MAE_30D_pct": -6.26, "MAE_30D_price": 115300.0, "MAE_90D_date": "2024-03-21", "MAE_90D_pct": -6.26, "MAE_90D_price": 115300.0, "MFE_180D_date": "2024-06-18", "MFE_180D_pct": 69.51, "MFE_180D_price": 208500.0, "MFE_30D_date": "2024-02-28", "MFE_30D_pct": 11.79, "MFE_30D_price": 137500.0, "MFE_90D_date": "2024-06-18", "MFE_90D_pct": 69.51, "MFE_90D_price": 208500.0, "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_role": "positive_structural_success", "company": "Lotte Wellfood Co., Ltd.", "corporate_action_contamination": false, "current_profile_verdict": "missed_or_too_late_structural_promotion", "drawdown_after_peak_pct": -44.12, "entry_date": "2024-02-08", "entry_price": 123000.0, "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_MARGIN_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE", "forward_window_complete": true, "future_data_leakage_check": "trigger evidence dated <= trigger_date; price path used only for calibration labels", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "market": "KOSPI", "peak_180D_date": "2024-06-18", "peak_180D_price": 208500.0, "post_peak_trough_date": "2024-11-07", "post_peak_trough_price": 116500.0, "price_basis": "stock-web tradable_raw OHLCV; raw_unadjusted_marcap", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 38, "channel_reorder_score": 83, "contract_score": 25, "customer_quality_score": 75, "dilution_cb_risk_score": 0, "execution_risk_score": 18, "inventory_or_channel_stuffing_risk_score": 18, "legal_or_contract_risk_score": 5, "margin_bridge_score": 84, "overseas_distribution_route_score": 88, "policy_or_regulatory_score": 5, "relative_strength_score": 80, "revision_score": 82, "valuation_repricing_score": 72}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 35, "channel_reorder_score": 75, "contract_score": 25, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 22, "inventory_or_channel_stuffing_risk_score": 20, "legal_or_contract_risk_score": 5, "margin_bridge_score": 72, "overseas_distribution_route_score": 82, "policy_or_regulatory_score": 5, "relative_strength_score": 72, "revision_score": 76, "valuation_repricing_score": 66}, "representative_row": true, "research_file": "e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "row_id": "R5L113-C18-280360-20240208", "score_return_alignment": "strong_positive_low_MAE", "selected_loop": 113, "selected_round": "R5", "source_url": "https://www.asiae.co.kr/en/article/2024020715233725800", "stage_label_after": "Stage3-Green", "stage_label_before": "Stage3-Yellow", "symbol": "280360", "trigger_date": "2024-02-07", "trigger_type": "Stage3-Green", "weighted_score_after": 88.0, "weighted_score_before": 79.0, "window_180D_end_date": "2024-11-07", "window_30D_end_date": "2024-03-26", "window_90D_end_date": "2024-06-25"}
{"MAE_180D_date": "2025-11-04", "MAE_180D_pct": -2.85, "MAE_180D_price": 99000.0, "MAE_30D_date": "2025-03-05", "MAE_30D_pct": -0.88, "MAE_30D_price": 101000.0, "MAE_90D_date": "2025-03-05", "MAE_90D_pct": -0.88, "MAE_90D_price": 101000.0, "MFE_180D_date": "2025-05-09", "MFE_180D_pct": 24.93, "MFE_180D_price": 127300.0, "MFE_30D_date": "2025-03-19", "MFE_30D_pct": 21.2, "MFE_30D_price": 123500.0, "MFE_90D_date": "2025-05-09", "MFE_90D_pct": 24.93, "MFE_90D_price": 127300.0, "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_role": "positive_structural_success", "company": "Orion Corp.", "corporate_action_contamination": false, "current_profile_verdict": "underweights_global_localized_repeat_demand", "drawdown_after_peak_pct": -22.23, "entry_date": "2025-02-28", "entry_price": 101900.0, "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_MARGIN_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE", "forward_window_complete": true, "future_data_leakage_check": "trigger evidence dated <= trigger_date; price path used only for calibration labels", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "market": "KOSPI", "peak_180D_date": "2025-05-09", "peak_180D_price": 127300.0, "post_peak_trough_date": "2025-11-04", "post_peak_trough_price": 99000.0, "price_basis": "stock-web tradable_raw OHLCV; raw_unadjusted_marcap", "raw_component_scores_after": {"accounting_trust_risk_score": 4, "backlog_visibility_score": 38, "channel_reorder_score": 90, "contract_score": 20, "customer_quality_score": 86, "dilution_cb_risk_score": 0, "execution_risk_score": 14, "inventory_or_channel_stuffing_risk_score": 12, "legal_or_contract_risk_score": 5, "margin_bridge_score": 76, "overseas_distribution_route_score": 93, "policy_or_regulatory_score": 5, "relative_strength_score": 82, "revision_score": 78, "valuation_repricing_score": 73}, "raw_component_scores_before": {"accounting_trust_risk_score": 4, "backlog_visibility_score": 35, "channel_reorder_score": 87, "contract_score": 20, "customer_quality_score": 82, "dilution_cb_risk_score": 0, "execution_risk_score": 17, "inventory_or_channel_stuffing_risk_score": 14, "legal_or_contract_risk_score": 5, "margin_bridge_score": 65, "overseas_distribution_route_score": 90, "policy_or_regulatory_score": 5, "relative_strength_score": 78, "revision_score": 72, "valuation_repricing_score": 70}, "representative_row": true, "research_file": "e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "row_id": "R5L113-C18-271560-20250228", "score_return_alignment": "positive_low_MAE_structural_repeat_demand", "selected_loop": 113, "selected_round": "R5", "source_url": "https://www.asiae.co.kr/en/article/2025022709121804606", "stage_label_after": "Stage3-Green_candidate", "stage_label_before": "Stage3-Yellow", "symbol": "271560", "trigger_date": "2025-02-27", "trigger_type": "Stage3-Yellow_to_Green_candidate", "weighted_score_after": 87.5, "weighted_score_before": 81.0, "window_180D_end_date": "2025-11-25", "window_30D_end_date": "2025-04-14", "window_90D_end_date": "2025-07-14"}
{"MAE_180D_date": "2025-01-23", "MAE_180D_pct": -37.79, "MAE_180D_price": 18290.0, "MAE_30D_date": "2024-07-22", "MAE_30D_pct": -18.37, "MAE_30D_price": 24000.0, "MAE_90D_date": "2024-10-25", "MAE_90D_pct": -33.37, "MAE_90D_price": 19590.0, "MFE_180D_date": "2024-06-17", "MFE_180D_pct": 5.1, "MFE_180D_price": 30900.0, "MFE_30D_date": "2024-06-17", "MFE_30D_pct": 5.1, "MFE_30D_price": 30900.0, "MFE_90D_date": "2024-06-17", "MFE_90D_pct": 5.1, "MFE_90D_price": 30900.0, "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_role": "counterexample_failed_rerating", "company": "Daesang Corp.", "corporate_action_contamination": false, "current_profile_verdict": "false_positive_if_channel_reach_overweighted", "drawdown_after_peak_pct": -40.81, "entry_date": "2024-06-14", "entry_price": 29400.0, "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_MARGIN_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE", "forward_window_complete": true, "future_data_leakage_check": "trigger evidence dated <= trigger_date; price path used only for calibration labels", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "market": "KOSPI", "peak_180D_date": "2024-06-17", "peak_180D_price": 30900.0, "post_peak_trough_date": "2025-01-23", "post_peak_trough_price": 18290.0, "price_basis": "stock-web tradable_raw OHLCV; raw_unadjusted_marcap", "raw_component_scores_after": {"accounting_trust_risk_score": 6, "backlog_visibility_score": 25, "channel_reorder_score": 75, "contract_score": 18, "customer_quality_score": 70, "dilution_cb_risk_score": 0, "execution_risk_score": 62, "inventory_or_channel_stuffing_risk_score": 76, "legal_or_contract_risk_score": 6, "margin_bridge_score": 38, "overseas_distribution_route_score": 80, "policy_or_regulatory_score": 8, "relative_strength_score": 48, "revision_score": 42, "valuation_repricing_score": 42}, "raw_component_scores_before": {"accounting_trust_risk_score": 6, "backlog_visibility_score": 25, "channel_reorder_score": 78, "contract_score": 18, "customer_quality_score": 72, "dilution_cb_risk_score": 0, "execution_risk_score": 45, "inventory_or_channel_stuffing_risk_score": 62, "legal_or_contract_risk_score": 6, "margin_bridge_score": 42, "overseas_distribution_route_score": 82, "policy_or_regulatory_score": 8, "relative_strength_score": 62, "revision_score": 47, "valuation_repricing_score": 61}, "representative_row": true, "research_file": "e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "row_id": "R5L113-C18-001680-20240614", "score_return_alignment": "counterexample_high_MAE_low_MFE", "selected_loop": 113, "selected_round": "R5", "source_url": "https://www.investkorea.org/ik-en/bbs/i-5073/detail.do?ntt_sn=492578", "stage_label_after": "Stage2-Actionable_only", "stage_label_before": "Stage3-Yellow_candidate", "symbol": "001680", "trigger_date": "2024-06-13", "trigger_type": "Stage2_false_positive_review", "weighted_score_after": 61.0, "weighted_score_before": 75.0, "window_180D_end_date": "2025-03-14", "window_30D_end_date": "2024-07-26", "window_90D_end_date": "2024-10-29"}
{"MAE_180D_date": "2024-11-15", "MAE_180D_pct": -12.55, "MAE_180D_price": 317000.0, "MAE_30D_date": "2024-03-20", "MAE_30D_pct": -1.93, "MAE_30D_price": 355500.0, "MAE_90D_date": "2024-03-20", "MAE_90D_pct": -1.93, "MAE_90D_price": 355500.0, "MFE_180D_date": "2024-06-13", "MFE_180D_pct": 65.24, "MFE_180D_price": 599000.0, "MFE_30D_date": "2024-04-25", "MFE_30D_pct": 10.9, "MFE_30D_price": 402000.0, "MFE_90D_date": "2024-06-13", "MFE_90D_pct": 65.24, "MFE_90D_price": 599000.0, "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_role": "4B_after_positive_spike", "company": "Nongshim Co., Ltd.", "corporate_action_contamination": false, "current_profile_verdict": "needs_peak_after_export_repricing_guard", "drawdown_after_peak_pct": -47.08, "entry_date": "2024-03-15", "entry_price": 362500.0, "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_MARGIN_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE", "forward_window_complete": true, "future_data_leakage_check": "trigger evidence dated <= trigger_date; price path used only for calibration labels", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "market": "KOSPI", "peak_180D_date": "2024-06-13", "peak_180D_price": 599000.0, "post_peak_trough_date": "2024-11-15", "post_peak_trough_price": 317000.0, "price_basis": "stock-web tradable_raw OHLCV; raw_unadjusted_marcap", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 35, "channel_reorder_score": 88, "contract_score": 20, "customer_quality_score": 86, "dilution_cb_risk_score": 0, "execution_risk_score": 44, "inventory_or_channel_stuffing_risk_score": 42, "legal_or_contract_risk_score": 5, "margin_bridge_score": 74, "overseas_distribution_route_score": 88, "policy_or_regulatory_score": 5, "relative_strength_score": 92, "revision_score": 78, "valuation_repricing_score": 61}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 35, "channel_reorder_score": 89, "contract_score": 20, "customer_quality_score": 86, "dilution_cb_risk_score": 0, "execution_risk_score": 22, "inventory_or_channel_stuffing_risk_score": 20, "legal_or_contract_risk_score": 5, "margin_bridge_score": 79, "overseas_distribution_route_score": 88, "policy_or_regulatory_score": 5, "relative_strength_score": 87, "revision_score": 82, "valuation_repricing_score": 76}, "representative_row": true, "research_file": "e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "row_id": "R5L113-C18-004370-20240315", "score_return_alignment": "strong_90D_positive_then_4B_needed", "selected_loop": 113, "selected_round": "R5", "source_url": "https://www.mk.co.kr/en/business/10964315", "stage_label_after": "Stage3-Green_then_4B-watch", "stage_label_before": "Stage3-Green_candidate", "symbol": "004370", "trigger_date": "2024-03-14", "trigger_type": "Stage3_success_then_4B_overlay", "weighted_score_after": 82.0, "weighted_score_before": 88.0, "window_180D_end_date": "2024-12-10", "window_30D_end_date": "2024-04-29", "window_90D_end_date": "2024-07-26"}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are working in /home/eorb915/projects/stock_agent.
Ingest the new V12 research file:
  docs/round/e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Run the standard V12 calibration ingest pipeline without changing production scoring manually:
  PYTHONPATH=src python -m e2r.calibration.cli run-v12-calibration \
    --md-input-root docs/round \
    --data-directory data/e2r/calibration/v12 \
    --report-directory reports/e2r_calibration/v12

Expected audit points:
- The file must be recognized as standard V12 result filename.
- selected_round=R5, selected_loop=113, large_sector_id=L5_CONSUMER_BRAND_DISTRIBUTION, canonical_archetype_id=C18_CONSUMER_EXPORT_CHANNEL_REORDER must match filename and metadata.
- Five new rows should be calibration_usable=true.
- All five rows contain complete MFE/MAE 30D/90D/180D fields.
- Verify no duplicate key on canonical_archetype_id + symbol + trigger_type + entry_date.
- Review C18 shadow-rule implications: promotion should require repeat-demand + margin/revision bridge, and 4B overlay should fire after high MFE + post-peak drawdown/cost-pressure evidence.
```

## 11. Next recommended archetype

Next recommended primary target: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`, because it is also severely under-covered and needs positive/counterexample separation around traffic-to-monetization conversion.

Secondary target: `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`, because this C18 run produced two rows where the initial trigger was valid but post-peak drawdown was large. Those rows can become seed material for cross-archetype high-MAE guardrail research.
