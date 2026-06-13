# stock-web v12 residual research — R7 / L7 / C25 medical device export reimbursement

```yaml
selected_round: R7
selected_loop: 100
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: mixed_C25_medical_device_export_reimbursement_quality_holdout
mode: stock_web_v12_sector_archetype_residual_calibration
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection rationale

This execution follows the v12 coverage-index-first rule. Static `V12_Research_No_Repeat_Index.md` already shows C25 as a covered-but-not-finalized quality holdout bucket rather than a raw under-30 gap bucket. Earlier current-session work filled many Priority 0/1 canonical gaps, so this pass selects `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` as a quality holdout to stress-test whether approval, reimbursement, export channel, and hospital billing headlines should unlock Stage3 or remain capped at Stage2/4B watch.

C25 is mapped to `R7 / L7_BIO_HEALTHCARE_MEDICAL`. This file deliberately avoids the top-covered C25 symbols visible in the ledger where possible, and uses six independent trigger families with clean 180D Stock-Web forward windows.

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No production code or production scoring profile is changed in this research file.

## 2. Price-source validation

Stock-Web basis:

```yaml
price_source: Songdaiki/stock-web
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
entry_price_rule: entry_date close
MFE_MAE_rule: max_high_or_min_low from entry_date through N tradable rows
forward_windows: [30D, 90D, 180D]
corporate_action_policy: block contaminated 180D windows
```

A screened candidate, `328130 루닛`, was excluded from the representative rows because its 2023 Japan reimbursement trigger window intersects Stock-Web corporate-action candidate dates in the symbol profile. It should only be reconsidered with a clean post-action entry date.

## 3. Case set summary

|symbol|name|trigger_date|entry_date|trigger_type|role|MFE_180D_pct|MAE_180D_pct|post_rule_stage|
|---|---|---|---|---|---|---|---|---|
|214150|클래시스|2024-08-08|2024-08-09|Stage3-Yellow|positive_structural_success|48.8000|-20.0000|Stage3-Yellow|
|335890|비올|2024-03-22|2024-03-25|Stage2-Actionable|positive_with_local_4B_watch|16.2319|-35.9420|Stage2-Actionable + local_4B_watch|
|322510|제이엘케이|2023-10-31|2023-10-31|Stage2-Actionable|counterexample_high_MAE_4B|32.0755|-62.3061|Stage2-Watch + full_4B_overlay|
|338220|뷰노|2023-08-31|2023-09-01|Stage2-Actionable|counterexample_high_MAE_4B|32.3810|-54.4762|Stage2-Actionable + local_4B_watch|
|099190|아이센스|2024-04-29|2024-04-30|Stage2-Actionable|counterexample_stage2_watch|16.4035|-26.0316|Stage2-Watch + margin_bridge_gate|
|145720|덴티움|2023-07-03|2023-07-04|Stage2-Actionable|counterexample_margin_reimbursement_risk|3.7085|-39.4275|Stage2-Watch + ASP_margin_gate|

Aggregate path signal:

```yaml
case_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
positive_case_count: 2
counterexample_count: 4
local_4B_watch_case_count: 5
hard_4C_case_count: 0
avg_MFE_90D_pct: 21.1001
avg_MAE_90D_pct: -33.6018
avg_MFE_180D_pct: 24.9334
avg_MAE_180D_pct: -39.6972
rows_with_MFE180_above_25pct: 3
rows_with_MAE180_below_minus_30pct: 4
```

## 4. Evidence basis by case

### 4.1 214150 클래시스 — positive structural success

Classys is the cleanest C25 positive in this pass. The evidence is not a single approval event; it is export sales, aesthetic device demand, and operating performance. The 180D MFE is strong while 180D MAE remains materially shallower than the medical-AI blowoff names.

Interpretation:

```text
C25 Stage3-Yellow allowed
Stage3-Green still requires continued export revenue, margin bridge, and low drawdown persistence.
```

### 4.2 335890 비올 — NMPA approval with local 4B watch

Viol's Sylfirm X China NMPA approval is real C25 export optionality. However, the price path peaked quickly and later experienced a deep 180D MAE. Approval opens the door; it does not prove channel sales, utilization, distributor repeat order, or margin conversion.

Interpretation:

```text
Stage2-Actionable allowed
Stage3-Yellow blocked until export revenue and margin bridge appear
local 4B watch required after approval-driven spike
```

### 4.3 322510 제이엘케이 — reimbursement fee headline blowoff

JLK's JBS-01K non-covered fee event is the classic C25 reimbursement unlock. The problem is that reimbursement fee approval is not the same as recurring hospital usage, reimbursed volume, revenue recognition, and margin conversion. The path had strong early MFE but catastrophic full-window MAE.

Interpretation:

```text
Stage2-Actionable initially
Stage3 blocked
full 4B overlay if price outruns recurring revenue evidence
```

### 4.4 338220 뷰노 — hospital billing adoption but high MAE

VUNO DeepCARS hospital billing progress is better evidence than a pure approval headline because it references hospital adoption and billing. Still, the price path shows a high-MFE / high-MAE structure. That means the thesis should not be discarded, but position timing and Stage3 promotion need stricter profitability/retention gates.

Interpretation:

```text
Stage2-Actionable positive evidence retained
Stage3-Yellow requires hospital retention, billing durability, revenue scale, and margin path
local 4B watch required
```

### 4.5 099190 아이센스 — CGM channel evidence without enough adoption bridge

The i-SENS / Handok CareSens Air sales contract provides a concrete domestic distribution route. However, the trigger did not yet confirm adoption velocity, reimbursement stickiness, or margin bridge. The result was a modest MFE and significant drawdown.

Interpretation:

```text
Stage2-Watch
do not promote to Stage3 until adoption and reimbursed recurring sales are visible
```

### 4.6 145720 덴티움 — China VBP volume thesis with ASP/margin risk

Dentium's China VBP volume thesis is a medical-device reimbursement/export case, but volume policy is not automatically margin-positive. ASP, inventory, and channel margin evidence must be separately validated. The price path shows low MFE and large MAE.

Interpretation:

```text
Stage2 cap
Stage3 blocked until China volume growth converts to export revenue and margin durability
```

## 5. Price-path table

|symbol|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|DD_after_peak|
|---|---|---|---|---|---|---|---|---|---|
|214150|50000.00|15.8000|-8.7000|25.8000|-20.0000|48.8000|-20.0000|2025-05-12|-15.0538|
|335890|10350.00|16.2319|-12.3671|16.2319|-12.3671|16.2319|-35.9420|2024-04-01|-44.8878|
|322510|23850.00|32.0755|-15.0943|32.0755|-49.3082|32.0755|-62.3061|2023-11-06|-71.4603|
|338220|52500.00|32.3810|-50.2857|32.3810|-54.4762|32.3810|-54.4762|2023-09-07|-65.6115|
|099190|19630.00|9.7809|-10.2394|16.4035|-26.0316|16.4035|-26.0316|2024-07-10|-36.4551|
|145720|153700.00|3.7085|-14.3136|3.7085|-39.4275|3.7085|-39.4275|2023-07-05|-41.5935|

## 6. Current-profile residual error

Current C25-like logic can over-promote four kinds of evidence:

```text
1. approval headline without channel revenue
2. reimbursement fee headline without hospital usage or billing retention
3. export policy / volume thesis without ASP-margin bridge
4. distribution contract without adoption velocity and recurring revenue
```

The residual error is not that these events are worthless. They are valid Stage2 evidence. The error is allowing them to behave like Stage3 rerating evidence before the recurring revenue / reimbursement / export-sales / margin bridge has appeared.

## 7. Shadow rule candidate

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP
```

Rule intent:

```yaml
stage2_allowed_if:
  - regulatory_approval
  - reimbursement_fee_or_noncovered_billing_route
  - named_distributor_or_export_channel
  - hospital_billing_or_install_base_growth
  - China/overseas volume policy route

stage3_yellow_allowed_only_if_at_least_two:
  - recurring_revenue_or_billing_volume_confirmed
  - export_channel_sales_confirmed
  - hospital_retention_or_repeat_usage_confirmed
  - reimbursement route converts to realized revenue
  - margin bridge or OP leverage visible
  - drawdown remains controlled after trigger window

stage3_green_allowed_only_if:
  - stage3_yellow conditions pass
  - information_confidence high
  - 90D/180D MAE not structurally excessive
  - price path is not a single approval/reimbursement blowoff

force_local_4B_watch_if_any:
  - MFE_30D or MFE_90D opens quickly but MAE_90D/180D collapses
  - approval/reimbursement is not followed by realized revenue
  - hospital count grows but profitability/retention remains unconfirmed
  - volume policy improves units while ASP/margin risk remains open
```

## 8. Profile comparison table

|symbol|P0_total_before|P0_total_after_shadow|stage_before|stage_after_shadow|main_delta_reason|
|---|---|---|---|---|---|
|214150|78.5|82.0|Stage3-Yellow|Stage3-Yellow|missed_strength_if_export_margin_bridge_underweighted|
|335890|77.0|68.0|Stage3-Yellow_candidate|Stage2-Actionable + local_4B_watch|approval_headline_over_promotes_without_channel_revenue|
|322510|76.0|61.5|Stage3-Yellow_candidate|Stage2-Watch + full_4B_overlay|reimbursement_fee_headline_over_promotes_without_usage_revenue_bridge|
|338220|78.0|69.0|Stage3-Yellow_candidate|Stage2-Actionable + local_4B_watch|hospital_count_adoption_over_promotes_without_retention_margin|
|099190|72.5|64.5|Stage2-Actionable|Stage2-Watch + margin_bridge_gate|distribution_contract_without_adoption_revenue_margin_gate|
|145720|74.0|60.0|Stage3-Yellow_candidate|Stage2-Watch + ASP_margin_gate|VBP_volume_over_promotes_without_ASP_margin_confirmation|

## 9. Machine-readable rows

```jsonl
{"row_type": "price_source_validation", "selected_round": "R7", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "214150", "entry_date": "2024-08-09", "entry_price": 50000.0, "price_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/214/214150/2025.csv"], "symbol_profile": "atlas/symbol_profiles/214/214150.json", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "price_source_validation", "selected_round": "R7", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "335890", "entry_date": "2024-03-25", "entry_price": 10350.0, "price_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/335/335890/2025.csv"], "symbol_profile": "atlas/symbol_profiles/335/335890.json", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "price_source_validation", "selected_round": "R7", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "322510", "entry_date": "2023-10-31", "entry_price": 23850.0, "price_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/322/322510/2024.csv"], "symbol_profile": "atlas/symbol_profiles/322/322510.json", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "price_source_validation", "selected_round": "R7", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "338220", "entry_date": "2023-09-01", "entry_price": 52500.0, "price_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/338/338220/2024.csv"], "symbol_profile": "atlas/symbol_profiles/338/338220.json", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "price_source_validation", "selected_round": "R7", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "099190", "entry_date": "2024-04-30", "entry_price": 19630.0, "price_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/099/099190/2025.csv"], "symbol_profile": "atlas/symbol_profiles/099/099190.json", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "price_source_validation", "selected_round": "R7", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "145720", "entry_date": "2023-07-04", "entry_price": 153700.0, "price_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/145/145720/2024.csv"], "symbol_profile": "atlas/symbol_profiles/145/145720.json", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "case", "case_id": "C25_214150_CLASSYS_2024-08-09_EXPORT_EQUIPMENT_MARGIN_BRIDGE", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "export_device_sales_margin_bridge", "deep_sub_archetype": "global_aesthetic_device_export_growth_with_margin_bridge", "symbol": "214150", "company_name": "클래시스", "trigger_date": "2024-08-08", "entry_date": "2024-08-09", "entry_price": 50000.0, "trigger_type": "Stage3-Yellow", "case_role": "positive_structural_success", "evidence_summary": "글로벌 미용의료기기 매출 성장과 장비 수출/마진 bridge가 확인된 C25 positive holdout. 단순 허가 뉴스가 아니라 판매·실적·영업레버리지 축이 함께 보였다.", "source_url": "https://www.mk.co.kr/news/stock/11088038", "calibration_usable": true, "dedupe_key": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214150|Stage3-Yellow|2024-08-09", "representative_row": true}
{"row_type": "case", "case_id": "C25_335890_VIOL_2024-03-25_NMPA_APPROVAL_HIGH_MAE_WATCH", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "regulatory_export_approval_to_channel_conversion", "deep_sub_archetype": "china_NMPA_device_approval_without_confirmed_revenue_margin_bridge", "symbol": "335890", "company_name": "비올", "trigger_date": "2024-03-22", "entry_date": "2024-03-25", "entry_price": 10350.0, "trigger_type": "Stage2-Actionable", "case_role": "positive_with_local_4B_watch", "evidence_summary": "Sylfirm X 중국 NMPA 승인으로 export/reimbursement optionality는 열렸지만, 승인 headline만으로 Stage3를 열면 180D MAE가 컸다.", "source_url": "https://www.newspim.com/news/view/20240322000617", "calibration_usable": true, "dedupe_key": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|335890|Stage2-Actionable|2024-03-25", "representative_row": true}
{"row_type": "case", "case_id": "C25_322510_JLK_2023-10-31_NONCOVERED_FEE_REIMBURSEMENT_BLOWOFF", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "medical_ai_noncovered_fee_reimbursement", "deep_sub_archetype": "single_ai_product_fee_unlock_without_recurring_hospital_usage_margin_bridge", "symbol": "322510", "company_name": "제이엘케이", "trigger_date": "2023-10-31", "entry_date": "2023-10-31", "entry_price": 23850.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_high_MAE_4B", "evidence_summary": "JBS-01K 비급여 수가 확정은 C25 Stage2 근거였지만, 실제 병원 사용량·반복매출·마진 bridge가 확인되기 전 price path는 빠른 MFE 후 깊은 MAE로 붕괴했다.", "source_url": "https://www.jlkgroup.com/news/pr?uid=123&mod=document", "calibration_usable": true, "dedupe_key": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|322510|Stage2-Actionable|2023-10-31", "representative_row": true}
{"row_type": "case", "case_id": "C25_338220_VUNO_2023-09-01_DEEPCARS_BILLING_TARGET_HIGH_MAE", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "medical_ai_hospital_billing_adoption", "deep_sub_archetype": "hospital_billing_rollout_without_stage3_profitability_confirmation", "symbol": "338220", "company_name": "뷰노", "trigger_date": "2023-08-31", "entry_date": "2023-09-01", "entry_price": 52500.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_high_MAE_4B", "evidence_summary": "DeepCARS 병원 청구 목표 달성은 adoption evidence였지만, entry 후 price path는 MFE와 MAE가 동시에 크게 열리는 고위험 구조였다.", "source_url": "https://www.vuno.co/news/press-release/?idx=18331638&bmode=view", "calibration_usable": true, "dedupe_key": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|338220|Stage2-Actionable|2023-09-01", "representative_row": true}
{"row_type": "case", "case_id": "C25_099190_ISENS_2024-04-30_CGM_DISTRIBUTION_REIMBURSEMENT_WATCH", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "domestic_CGM_distribution_and_reimbursement_channel", "deep_sub_archetype": "CGM_distribution_contract_without_adoption_margin_bridge", "symbol": "099190", "company_name": "아이센스", "trigger_date": "2024-04-29", "entry_date": "2024-04-30", "entry_price": 19630.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_stage2_watch", "evidence_summary": "CareSens Air 판매계약은 국내 CGM channel evidence였지만, adoption velocity·reimbursement stickiness·margin bridge가 확인되기 전에는 MAE가 커졌다.", "source_url": "https://www.sedaily.com/NewsView/2D840C8BFU", "calibration_usable": true, "dedupe_key": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|099190|Stage2-Actionable|2024-04-30", "representative_row": true}
{"row_type": "case", "case_id": "C25_145720_DENTIUM_2023-07-04_CHINA_VBP_MARGIN_COUNTEREXAMPLE", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "dental_implant_export_reimbursement_volume_policy", "deep_sub_archetype": "china_VBP_volume_growth_without_ASP_margin_inventory_bridge", "symbol": "145720", "company_name": "덴티움", "trigger_date": "2023-07-03", "entry_date": "2023-07-04", "entry_price": 153700.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_margin_reimbursement_risk", "evidence_summary": "중국 VBP 이후 임플란트 volume/export thesis는 있었지만, ASP·재고·마진 bridge가 약하면 Stage3가 아니라 Stage2 cap과 4B watch가 맞았다.", "source_url": "https://dailyinvest.kr/news/articleView.html?idxno=52504", "calibration_usable": true, "dedupe_key": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|145720|Stage2-Actionable|2023-07-04", "representative_row": true}
{"row_type": "trigger", "case_id": "C25_214150_CLASSYS_2024-08-09_EXPORT_EQUIPMENT_MARGIN_BRIDGE", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "214150", "company_name": "클래시스", "trigger_date": "2024-08-08", "entry_date": "2024-08-09", "entry_price": 50000.0, "trigger_type": "Stage3-Yellow", "MFE_30D_pct": 15.8, "MAE_30D_pct": -8.7, "MFE_90D_pct": 25.8, "MAE_90D_pct": -20.0, "MFE_180D_pct": 48.8, "MAE_180D_pct": -20.0, "peak_date": "2025-05-12", "peak_price": 74400.0, "drawdown_after_peak_pct": -15.0538, "four_b_timing_verdict": "no_4B_required_but_monitor", "four_c_timing_verdict": "no_hard_4C_thesis_break", "corporate_action_window_status": "clean_180D_window", "insufficient_forward_window": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false}
{"row_type": "trigger", "case_id": "C25_335890_VIOL_2024-03-25_NMPA_APPROVAL_HIGH_MAE_WATCH", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "335890", "company_name": "비올", "trigger_date": "2024-03-22", "entry_date": "2024-03-25", "entry_price": 10350.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 16.2319, "MAE_30D_pct": -12.3671, "MFE_90D_pct": 16.2319, "MAE_90D_pct": -12.3671, "MFE_180D_pct": 16.2319, "MAE_180D_pct": -35.942, "peak_date": "2024-04-01", "peak_price": 12030.0, "drawdown_after_peak_pct": -44.8878, "four_b_timing_verdict": "local_4B_watch_required", "four_c_timing_verdict": "no_hard_4C_thesis_break", "corporate_action_window_status": "clean_180D_window", "insufficient_forward_window": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false}
{"row_type": "trigger", "case_id": "C25_322510_JLK_2023-10-31_NONCOVERED_FEE_REIMBURSEMENT_BLOWOFF", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "322510", "company_name": "제이엘케이", "trigger_date": "2023-10-31", "entry_date": "2023-10-31", "entry_price": 23850.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 32.0755, "MAE_30D_pct": -15.0943, "MFE_90D_pct": 32.0755, "MAE_90D_pct": -49.3082, "MFE_180D_pct": 32.0755, "MAE_180D_pct": -62.3061, "peak_date": "2023-11-06", "peak_price": 31500.0, "drawdown_after_peak_pct": -71.4603, "four_b_timing_verdict": "local_4B_watch_required", "four_c_timing_verdict": "no_hard_4C_thesis_break", "corporate_action_window_status": "clean_180D_window", "insufficient_forward_window": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false}
{"row_type": "trigger", "case_id": "C25_338220_VUNO_2023-09-01_DEEPCARS_BILLING_TARGET_HIGH_MAE", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "338220", "company_name": "뷰노", "trigger_date": "2023-08-31", "entry_date": "2023-09-01", "entry_price": 52500.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 32.381, "MAE_30D_pct": -50.2857, "MFE_90D_pct": 32.381, "MAE_90D_pct": -54.4762, "MFE_180D_pct": 32.381, "MAE_180D_pct": -54.4762, "peak_date": "2023-09-07", "peak_price": 69500.0, "drawdown_after_peak_pct": -65.6115, "four_b_timing_verdict": "local_4B_watch_required", "four_c_timing_verdict": "no_hard_4C_thesis_break", "corporate_action_window_status": "clean_180D_window", "insufficient_forward_window": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false}
{"row_type": "trigger", "case_id": "C25_099190_ISENS_2024-04-30_CGM_DISTRIBUTION_REIMBURSEMENT_WATCH", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "099190", "company_name": "아이센스", "trigger_date": "2024-04-29", "entry_date": "2024-04-30", "entry_price": 19630.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 9.7809, "MAE_30D_pct": -10.2394, "MFE_90D_pct": 16.4035, "MAE_90D_pct": -26.0316, "MFE_180D_pct": 16.4035, "MAE_180D_pct": -26.0316, "peak_date": "2024-07-10", "peak_price": 22850.0, "drawdown_after_peak_pct": -36.4551, "four_b_timing_verdict": "no_4B_required_but_monitor", "four_c_timing_verdict": "no_hard_4C_thesis_break", "corporate_action_window_status": "clean_180D_window", "insufficient_forward_window": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false}
{"row_type": "trigger", "case_id": "C25_145720_DENTIUM_2023-07-04_CHINA_VBP_MARGIN_COUNTEREXAMPLE", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "145720", "company_name": "덴티움", "trigger_date": "2023-07-03", "entry_date": "2023-07-04", "entry_price": 153700.0, "trigger_type": "Stage2-Actionable", "MFE_30D_pct": 3.7085, "MAE_30D_pct": -14.3136, "MFE_90D_pct": 3.7085, "MAE_90D_pct": -39.4275, "MFE_180D_pct": 3.7085, "MAE_180D_pct": -39.4275, "peak_date": "2023-07-05", "peak_price": 159400.0, "drawdown_after_peak_pct": -41.5935, "four_b_timing_verdict": "local_4B_watch_required", "four_c_timing_verdict": "no_hard_4C_thesis_break", "corporate_action_window_status": "clean_180D_window", "insufficient_forward_window": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "future_data_leakage_detected": false}
{"row_type": "score_simulation", "case_id": "C25_214150_CLASSYS_2024-08-09_EXPORT_EQUIPMENT_MARGIN_BRIDGE", "profile_before": "e2r_2_2_rolling_calibrated", "shadow_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "symbol": "214150", "total_score_before": 78.5, "stage_before": "Stage3-Yellow", "raw_component_scores_before": {"eps_fcf_explosion": 72, "earnings_visibility": 74, "bottleneck_pricing": 70, "market_mispricing": 66, "valuation_rerating": 68, "capital_allocation": 55, "information_confidence": 78}, "total_score_after_shadow_rule": 82.0, "stage_after_shadow_rule": "Stage3-Yellow", "raw_component_scores_after": {"eps_fcf_explosion": 76, "earnings_visibility": 78, "bottleneck_pricing": 72, "market_mispricing": 68, "valuation_rerating": 70, "capital_allocation": 55, "information_confidence": 82}, "delta_summary": "missed_strength_if_export_margin_bridge_underweighted"}
{"row_type": "score_simulation", "case_id": "C25_335890_VIOL_2024-03-25_NMPA_APPROVAL_HIGH_MAE_WATCH", "profile_before": "e2r_2_2_rolling_calibrated", "shadow_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "symbol": "335890", "total_score_before": 77.0, "stage_before": "Stage3-Yellow_candidate", "raw_component_scores_before": {"eps_fcf_explosion": 64, "earnings_visibility": 62, "bottleneck_pricing": 68, "market_mispricing": 72, "valuation_rerating": 74, "capital_allocation": 50, "information_confidence": 76}, "total_score_after_shadow_rule": 68.0, "stage_after_shadow_rule": "Stage2-Actionable + local_4B_watch", "raw_component_scores_after": {"eps_fcf_explosion": 58, "earnings_visibility": 55, "bottleneck_pricing": 64, "market_mispricing": 66, "valuation_rerating": 58, "capital_allocation": 50, "information_confidence": 72}, "delta_summary": "approval_headline_over_promotes_without_channel_revenue"}
{"row_type": "score_simulation", "case_id": "C25_322510_JLK_2023-10-31_NONCOVERED_FEE_REIMBURSEMENT_BLOWOFF", "profile_before": "e2r_2_2_rolling_calibrated", "shadow_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "symbol": "322510", "total_score_before": 76.0, "stage_before": "Stage3-Yellow_candidate", "raw_component_scores_before": {"eps_fcf_explosion": 60, "earnings_visibility": 63, "bottleneck_pricing": 70, "market_mispricing": 76, "valuation_rerating": 78, "capital_allocation": 45, "information_confidence": 74}, "total_score_after_shadow_rule": 61.5, "stage_after_shadow_rule": "Stage2-Watch + full_4B_overlay", "raw_component_scores_after": {"eps_fcf_explosion": 50, "earnings_visibility": 48, "bottleneck_pricing": 62, "market_mispricing": 58, "valuation_rerating": 42, "capital_allocation": 45, "information_confidence": 68}, "delta_summary": "reimbursement_fee_headline_over_promotes_without_usage_revenue_bridge"}
{"row_type": "score_simulation", "case_id": "C25_338220_VUNO_2023-09-01_DEEPCARS_BILLING_TARGET_HIGH_MAE", "profile_before": "e2r_2_2_rolling_calibrated", "shadow_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "symbol": "338220", "total_score_before": 78.0, "stage_before": "Stage3-Yellow_candidate", "raw_component_scores_before": {"eps_fcf_explosion": 62, "earnings_visibility": 66, "bottleneck_pricing": 72, "market_mispricing": 76, "valuation_rerating": 75, "capital_allocation": 45, "information_confidence": 76}, "total_score_after_shadow_rule": 69.0, "stage_after_shadow_rule": "Stage2-Actionable + local_4B_watch", "raw_component_scores_after": {"eps_fcf_explosion": 55, "earnings_visibility": 56, "bottleneck_pricing": 67, "market_mispricing": 64, "valuation_rerating": 48, "capital_allocation": 45, "information_confidence": 70}, "delta_summary": "hospital_count_adoption_over_promotes_without_retention_margin"}
{"row_type": "score_simulation", "case_id": "C25_099190_ISENS_2024-04-30_CGM_DISTRIBUTION_REIMBURSEMENT_WATCH", "profile_before": "e2r_2_2_rolling_calibrated", "shadow_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "symbol": "099190", "total_score_before": 72.5, "stage_before": "Stage2-Actionable", "raw_component_scores_before": {"eps_fcf_explosion": 58, "earnings_visibility": 62, "bottleneck_pricing": 64, "market_mispricing": 66, "valuation_rerating": 68, "capital_allocation": 50, "information_confidence": 74}, "total_score_after_shadow_rule": 64.5, "stage_after_shadow_rule": "Stage2-Watch + margin_bridge_gate", "raw_component_scores_after": {"eps_fcf_explosion": 54, "earnings_visibility": 55, "bottleneck_pricing": 62, "market_mispricing": 58, "valuation_rerating": 50, "capital_allocation": 50, "information_confidence": 70}, "delta_summary": "distribution_contract_without_adoption_revenue_margin_gate"}
{"row_type": "score_simulation", "case_id": "C25_145720_DENTIUM_2023-07-04_CHINA_VBP_MARGIN_COUNTEREXAMPLE", "profile_before": "e2r_2_2_rolling_calibrated", "shadow_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "symbol": "145720", "total_score_before": 74.0, "stage_before": "Stage3-Yellow_candidate", "raw_component_scores_before": {"eps_fcf_explosion": 60, "earnings_visibility": 64, "bottleneck_pricing": 66, "market_mispricing": 68, "valuation_rerating": 72, "capital_allocation": 50, "information_confidence": 72}, "total_score_after_shadow_rule": 60.0, "stage_after_shadow_rule": "Stage2-Watch + ASP_margin_gate", "raw_component_scores_after": {"eps_fcf_explosion": 50, "earnings_visibility": 50, "bottleneck_pricing": 60, "market_mispricing": 52, "valuation_rerating": 42, "capital_allocation": 50, "information_confidence": 66}, "delta_summary": "VBP_volume_over_promotes_without_ASP_margin_confirmation"}
{"row_type": "shadow_weight_candidate", "selected_round": "R7", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "proposed_direction": {"increase_weight": ["earnings_visibility", "information_confidence", "market_mispricing_when_export_revenue_visible"], "decrease_weight": ["single_approval_or_reimbursement_headline_without_revenue_bridge", "price_only_blowoff"], "add_gate": ["recurring_revenue_or_reimbursement_usage", "export_channel_sales", "margin_bridge", "hospital_or_distributor_repeat_order"]}, "avg_MFE_180D_pct": 24.9334, "avg_MAE_180D_pct": -39.6972, "rows_with_MAE180_below_minus_30pct": 4, "do_not_apply_production_now": true}
{"row_type": "residual_contribution", "selected_round": "R7", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "sector_specific_rule_candidate": "L7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REVENUE_REALIZATION_AND_4B_SPLIT", "canonical_archetype_rule_candidate": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP", "new_axis_proposed": "C25_reimbursement_export_revenue_margin_gate_with_high_MAE_4B_cap", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": null, "calibration_usable_rows": 6, "representative_rows": 6}
```

## 10. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
screened_out_corporate_action_contaminated_candidates:
  - 328130_LUNIT_2023_JAPAN_REIMBURSEMENT_WINDOW
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Read this markdown as a v12 residual calibration input only.

Target:
- canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
- rule_candidate: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REQUIRES_REIMBURSEMENT_OR_EXPORT_TO_RECURRING_REVENUE_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP

Do not patch production scoring immediately.
First ingest the JSONL rows, validate Stock-Web price fields, confirm no corporate-action contamination, and compare against existing C25 rows.

Suggested implementation test:
1. Add a shadow C25 gate that keeps approval/reimbursement/export-channel events at Stage2 unless recurring revenue, hospital billing retention, export sales, or margin bridge is visible.
2. Apply local 4B overlay when early MFE is accompanied by MAE90/MAE180 collapse.
3. Re-run v12 calibration aggregation and compare:
   - Stage3 false positive reduction
   - missed structural positive risk in Classys-like export-margin cases
   - high-MAE guardrail hit rate
4. Only promote if aggregate precision improves without blocking Classys-type positive export device rerating.
```

## 12. Next recommended archetypes

```yaml
next_recommended_archetypes:
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_holdout_only_if_new_reimbursement_or_export_revenue_path
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C24_BIO_TRIAL_DATA_EVENT_RISK_quality_holdout
```
