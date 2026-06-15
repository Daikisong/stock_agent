# E2R Stock-Web v12 Residual Research — R7 / L7_BIO_HEALTHCARE_MEDICAL / C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

```text
filename = e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
selected_round = R7
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_guard | canonical_archetype_compression
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / No-Repeat Rationale

`V12_Research_No_Repeat_Index.md`에서 `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`은 12 rows / 9 symbols로 남아 있는 Priority 0 구역이다. 기존 대표 symbol은 `195940`, `145020`, `000100`, `009420`, `067630`, `068270` 쪽에 몰려 있다. 이번 loop는 기존 상위 반복 symbol을 피하고, C23 내부의 다른 commercialization route를 시험한다.

선택한 four-case basket:

| case | symbol | role | trigger family | duplicate risk |
|---|---:|---|---|---|
| C23_196170_20240221_STAGE2A | 196170 | structural success + 4B watch | partner regulatory commercialization royalty bridge | new symbol for C23 priority fill |
| C23_326030_20240229_STAGE2 | 326030 | mixed positive | approved drug sales commercialization bridge | new symbol for C23 priority fill |
| C23_069620_20240319_STAGE2 | 069620 | weak bridge / counterexample | exported approved product commercialization bridge | new symbol for C23 priority fill |
| C23_128940_20240115_STAGE2 | 128940 | counterexample | pipeline/regulatory label without near commercialization | new symbol for C23 priority fill |

## 2. Price Source Validation

Stock-web manifest confirms:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | name | profile status | corporate action overlap with 2024 entry~180D | calibration note |
|---:|---|---|---|---|
| 196170 | 알테오젠 | active_like | none in 2024 window | historical CA candidates are pre-2024; 2024 window clean |
| 326030 | SK바이오팜 | active_like | none | clean |
| 069620 | 대웅제약 | active_like | none | clean |
| 128940 | 한미약품 | active_like | none | clean |

Validation scope is intentionally narrow: **price path is verified from stock-web tradable shards; non-price evidence is marked `source_proxy_only` / `evidence_url_pending=true` for later URL repair**.

## 3. Case Notes

### 3.1 196170 / 알테오젠 — partner commercialization royalty route, but local 4B required

Entry is 2024-02-21 close 93,900. The next 180 trading days produce a very large MFE path. The path validates that C23 should not treat all biotech as binary C24 trial risk; partner/regulatory commercialization royalty route is a different bridge. But the same row also shows why C23 needs a local post-rerating 4B guard: the price ran vertically before long-form non-price commercialization proof could fully catch up.

```text
entry_date = 2024-02-21
entry_price = 93,900
MFE_30D / MAE_30D = +140.15% / -10.12%
MFE_90D / MAE_90D = +217.89% / -10.12%
MFE_180D / MAE_180D = +287.11% / -10.12%
case_role = structural_success_with_4b_watch
```

### 3.2 326030 / SK바이오팜 — commercial-stage drug sales bridge with painful pre-confirmation drawdown

Entry is 2024-02-29 close 96,900. The later path eventually reaches 119,500 high inside the 180D window, but only after a 72,600 trough. The current profile can be too permissive if it grants Stage2 simply because a drug is approved/commercial; it needs revenue acceleration and revision confirmation to reduce MAE.

```text
entry_date = 2024-02-29
entry_price = 96,900
MFE_30D / MAE_30D = +1.86% / -9.39%
MFE_90D / MAE_90D = +2.99% / -22.70%
MFE_180D / MAE_180D = +23.32% / -25.08%
case_role = mixed_positive
```

### 3.3 069620 / 대웅제약 — approved/exported product label is not enough

Entry is 2024-03-19 close 123,600. The path eventually makes a 152,000 high, but early/medium horizon quality is weak and the trough reaches 100,100. This is a C23 counterexample: approved product vocabulary needs a visible sales / revision / margin bridge, otherwise it acts like a price-only or narrative-only beta.

```text
entry_date = 2024-03-19
entry_price = 123,600
MFE_30D / MAE_30D = +3.24% / -8.90%
MFE_90D / MAE_90D = +3.24% / -18.93%
MFE_180D / MAE_180D = +22.98% / -18.93%
case_role = counterexample_or_weak_bridge
```

### 3.4 128940 / 한미약품 — pipeline/regulatory label without near commercial cash path

Entry is 2024-01-15 close 338,000. The same day high gives a shallow headline MFE, but the 180D trough reaches 258,000. The path is the clean negative control: C23 should not award positive-stage credit to “pipeline/regulatory” vocabulary unless the route is already approval-to-sales, royalty, reimbursement, or near commercial launch.

```text
entry_date = 2024-01-15
entry_price = 338,000
MFE_30D / MAE_30D = +11.39% / -7.84%
MFE_90D / MAE_90D = +11.39% / -9.62%
MFE_180D / MAE_180D = +11.39% / -23.67%
case_role = counterexample
```

## 4. Current Calibrated Profile Stress Test

The current calibrated profile already blocks broad price-only blowoff and requires non-price evidence for full 4B. This C23 loop does not re-propose that global rule. It adds a narrower canonical compression:

```text
C23 positive credit requires:
1. approved product sales bridge, or
2. partner royalty / milestone commercialization bridge, or
3. reimbursement / launch conversion bridge, or
4. export sales with margin/revision proof.

C23 positive credit should be blocked or capped when:
1. evidence is only pipeline/regulatory vocabulary,
2. approval is not linked to near-term revenue,
3. launch exists but revision/OPM/royalty path is absent,
4. MFE is mostly price proximity without commercial proof.
```

Residual errors found:

| residual | case |
|---|---|
| underweighted partner/royalty commercialization route | 196170 |
| Stage2 too early without revenue acceleration buffer | 326030 |
| approved product label overcredits visibility without revision follow-through | 069620 |
| pipeline/regulatory vocabulary receives too much InfoConfidence | 128940 |

## 5. Shadow Rule Candidate

```text
new_axis_proposed = C23_approval_label_to_revenue_royalty_commercialization_bridge_required

rule:
if canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:
    positive_stage_credit requires one of:
      - sales acceleration after approval/launch
      - royalty/milestone bridge tied to partner commercialization
      - reimbursement or launch conversion bridge
      - export product revenue + margin/revision proof

if evidence is only pipeline/regulatory vocabulary:
    cap at Stage2-watch or narrative-only
    do not unlock Stage2-Actionable / Stage3-Yellow without commercial bridge

if MFE_30D_pct > +80 and evidence has not upgraded:
    add local_4b_watch_guard
```

Existing axis status:

```text
existing_axis_strengthened =
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
```

## 6. Machine-readable JSONL Rows

```jsonl
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_196170_20240221_STAGE2A", "symbol": "196170", "name": "알테오젠", "case_role": "structural_success_with_4b_watch", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "trigger_family": "partner_regulatory_commercialization_royalty_bridge", "evidence_summary": "Partner/regulatory commercialization royalty route produced extreme MFE before a later volatility phase; C23 should reward commercialization bridge but attach a local 4B guard after vertical rerating.", "outcome_label": "positive_but_late_4b_needed", "calibration_usable": true}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_326030_20240229_STAGE2", "symbol": "326030", "name": "SK바이오팜", "case_role": "mixed_positive", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "trigger_family": "approved_drug_sales_commercialization_revenue_bridge", "evidence_summary": "Commercial-stage drug sales bridge eventually resolved upward, but early Stage2 carried deep MAE before the market accepted revenue durability.", "outcome_label": "slow_commercialization_positive_with_large_pre_uplift_drawdown", "calibration_usable": true}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_069620_20240319_STAGE2", "symbol": "069620", "name": "대웅제약", "case_role": "counterexample_or_weak_bridge", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "trigger_family": "exported_approved_product_commercialization_bridge", "evidence_summary": "Approved/export product label existed, but the 30D/90D path gave little upside and large interim MAE; C23 needs revenue/revision proof rather than product-label vocabulary.", "outcome_label": "weak_bridge_high_opportunity_cost", "calibration_usable": true}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_128940_20240115_STAGE2", "symbol": "128940", "name": "한미약품", "case_role": "counterexample", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "trigger_family": "pipeline_or_regulatory_label_without_near_commercialization", "evidence_summary": "Pipeline/regulatory vocabulary did not produce a near-term commercialization cash bridge; this is the clean counterexample for blocking C23 positives without approved-product sales or royalty visibility.", "outcome_label": "pipeline_label_false_positive_without_commercial_cash_bridge", "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "case_id": "C23_196170_20240221_STAGE2A", "symbol": "196170", "name": "알테오젠", "trigger_type": "Stage2-Actionable", "trigger_family": "partner_regulatory_commercialization_royalty_bridge", "case_role": "structural_success_with_4b_watch", "entry_date": "2024-02-21", "entry_price": 93900.0, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 140.15, "MAE_30D_pct": -10.12, "MFE_90D_pct": 217.89, "MAE_90D_pct": -10.12, "MFE_180D_pct": 287.11, "MAE_180D_pct": -10.12, "peak_180D_date": "2024-09-20", "peak_180D_price": 363500.0, "trough_180D_date": "2024-02-21", "trough_180D_price": 84400.0, "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|196170|Stage2-Actionable|2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Non-price event label is a proxy and must be URL-repaired by later coding/research batch; price path is verified from stock-web shard.", "outcome_label": "positive_but_late_4b_needed", "current_profile_error": true, "current_profile_error_type": "underweighted_partner_royalty_commercialization_bridge_then_4b_timing_risk", "raw_component_score_breakdown": {"EPS_FCF": 13, "Visibility": 23, "BottleneckPricing": 10, "Mispricing": 17, "ValuationRunway": 13, "CapitalAllocation": 4, "InfoConfidence": 12}, "simulated_total_score": 92, "new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "case_id": "C23_326030_20240229_STAGE2", "symbol": "326030", "name": "SK바이오팜", "trigger_type": "Stage2", "trigger_family": "approved_drug_sales_commercialization_revenue_bridge", "case_role": "mixed_positive", "entry_date": "2024-02-29", "entry_price": 96900.0, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 1.86, "MAE_30D_pct": -9.39, "MFE_90D_pct": 2.99, "MAE_90D_pct": -22.7, "MFE_180D_pct": 23.32, "MAE_180D_pct": -25.08, "peak_180D_date": "2024-08-29", "peak_180D_price": 119500.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 72600.0, "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|Stage2|2024-02-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Non-price event label is a proxy and must be URL-repaired by later coding/research batch; price path is verified from stock-web shard.", "outcome_label": "slow_commercialization_positive_with_large_pre_uplift_drawdown", "current_profile_error": true, "current_profile_error_type": "stage2_too_early_without_revenue_acceleration_buffer", "raw_component_score_breakdown": {"EPS_FCF": 11, "Visibility": 22, "BottleneckPricing": 8, "Mispricing": 14, "ValuationRunway": 12, "CapitalAllocation": 4, "InfoConfidence": 9}, "simulated_total_score": 80, "new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "case_id": "C23_069620_20240319_STAGE2", "symbol": "069620", "name": "대웅제약", "trigger_type": "Stage2", "trigger_family": "exported_approved_product_commercialization_bridge", "case_role": "counterexample_or_weak_bridge", "entry_date": "2024-03-19", "entry_price": 123600.0, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 3.24, "MAE_30D_pct": -8.9, "MFE_90D_pct": 3.24, "MAE_90D_pct": -18.93, "MFE_180D_pct": 22.98, "MAE_180D_pct": -18.93, "peak_180D_date": "2024-08-29", "peak_180D_price": 152000.0, "trough_180D_date": "2024-06-26", "trough_180D_price": 100100.0, "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|069620|Stage2|2024-03-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Non-price event label is a proxy and must be URL-repaired by later coding/research batch; price path is verified from stock-web shard.", "outcome_label": "weak_bridge_high_opportunity_cost", "current_profile_error": true, "current_profile_error_type": "approved_product_label_overcredits_visibility_without_revision_followthrough", "raw_component_score_breakdown": {"EPS_FCF": 8, "Visibility": 18, "BottleneckPricing": 7, "Mispricing": 11, "ValuationRunway": 10, "CapitalAllocation": 5, "InfoConfidence": 10}, "simulated_total_score": 69, "new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "case_id": "C23_128940_20240115_STAGE2", "symbol": "128940", "name": "한미약품", "trigger_type": "Stage2", "trigger_family": "pipeline_or_regulatory_label_without_near_commercialization", "case_role": "counterexample", "entry_date": "2024-01-15", "entry_price": 338000.0, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 11.39, "MAE_30D_pct": -7.84, "MFE_90D_pct": 11.39, "MAE_90D_pct": -9.62, "MFE_180D_pct": 11.39, "MAE_180D_pct": -23.67, "peak_180D_date": "2024-01-15", "peak_180D_price": 376500.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 258000.0, "corporate_action_window_status": "clean", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|128940|Stage2|2024-01-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Non-price event label is a proxy and must be URL-repaired by later coding/research batch; price path is verified from stock-web shard.", "outcome_label": "pipeline_label_false_positive_without_commercial_cash_bridge", "current_profile_error": true, "current_profile_error_type": "visibility_info_score_too_high_when_approval_to_sales_path_is_not_near_term", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 10, "ValuationRunway": 8, "CapitalAllocation": 5, "InfoConfidence": 12}, "simulated_total_score": 64, "new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_196170_20240221_STAGE2A", "symbol": "196170", "trigger_type": "Stage2-Actionable", "raw_component_score_breakdown": {"EPS_FCF": 13, "Visibility": 23, "BottleneckPricing": 10, "Mispricing": 17, "ValuationRunway": 13, "CapitalAllocation": 4, "InfoConfidence": 12}, "simulated_total_score": 92, "simulated_stage": "Stage2-Actionable", "current_profile_error_type": "underweighted_partner_royalty_commercialization_bridge_then_4b_timing_risk"}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_326030_20240229_STAGE2", "symbol": "326030", "trigger_type": "Stage2", "raw_component_score_breakdown": {"EPS_FCF": 11, "Visibility": 22, "BottleneckPricing": 8, "Mispricing": 14, "ValuationRunway": 12, "CapitalAllocation": 4, "InfoConfidence": 9}, "simulated_total_score": 80, "simulated_stage": "Stage2", "current_profile_error_type": "stage2_too_early_without_revenue_acceleration_buffer"}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_069620_20240319_STAGE2", "symbol": "069620", "trigger_type": "Stage2", "raw_component_score_breakdown": {"EPS_FCF": 8, "Visibility": 18, "BottleneckPricing": 7, "Mispricing": 11, "ValuationRunway": 10, "CapitalAllocation": 5, "InfoConfidence": 10}, "simulated_total_score": 69, "simulated_stage": "Stage2", "current_profile_error_type": "approved_product_label_overcredits_visibility_without_revision_followthrough"}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "case_id": "C23_128940_20240115_STAGE2", "symbol": "128940", "trigger_type": "Stage2", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 10, "ValuationRunway": 8, "CapitalAllocation": 5, "InfoConfidence": 12}, "simulated_total_score": 64, "simulated_stage": "Stage2", "current_profile_error_type": "visibility_info_score_too_high_when_approval_to_sales_path_is_not_near_term"}
{"row_type": "aggregate_metric", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "representative_trigger_count": 4, "calibration_usable_trigger_count": 4, "positive_case_count": 1, "mixed_positive_count": 2, "counterexample_count": 1, "local_4b_watch_count": 1, "current_profile_error_count": 4, "median_MFE_180D_pct": 23.15, "median_MAE_180D_pct": -21.3, "new_axis_proposed": "C23_approval_label_to_revenue_royalty_commercialization_bridge_required", "existing_axis_strengthened": "stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail"}
{"row_type": "shadow_weight", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "axis": "C23_approval_label_to_revenue_royalty_commercialization_bridge_required", "proposed_delta": "+1 Visibility, +1 InfoConfidence only when sales/royalty/reimbursement bridge is explicit; otherwise no positive-stage credit", "scope": "canonical_archetype_specific", "do_not_apply_now": true, "rationale": "Alteogen/SKBP show that commercialization bridges matter, while Daewoong/Hanmi show that label-only or pipeline vocabulary without near-term revenue/revision bridge creates high MAE or opportunity cost."}
{"row_type": "shadow_weight", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "axis": "C23_post_rerating_local_4b_guard", "proposed_delta": "add local 4B watch if MFE_30D > +80% and non-price commercialization evidence is not upgraded after entry", "scope": "canonical_archetype_specific", "do_not_apply_now": true, "rationale": "196170 produced large structural MFE but became a valuation/proximity timing problem; do not convert early positive to unguarded Green."}
{"row_type": "residual_contribution", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 100, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "loop_contribution_label": "canonical_archetype_rule_candidate", "residual_error_found": true, "new_independent_case_count": 4, "counterexample_count": 1, "current_profile_error_count": 4, "one_line_summary": "This loop adds 4 new independent cases, 1 counterexample, and 4 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION."}
```

## 7. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 8. Residual Contribution Summary

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
new_trigger_family_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 1
local_4b_watch_count = 1
current_profile_error_count = 4
diversity_score_summary = Priority 0 C23 shortage fill; existing top covered 195940/145020/000100/009420/067630/068270 avoided; 196170/326030/069620/128940 added
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C23 rows 12 → 16 if accepted; still Priority 0, need 14 to 30
```

This loop adds 4 new independent cases, 1 counterexample, and 4 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation/coding agent. Do not re-run the research. Read this MD as a v12 sector-archetype residual calibration artifact.

Target artifact:
- file: e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
- selected_round: R7
- selected_loop: 100
- large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
- canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
- fine_archetype_id: BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE

Use the JSONL rows in the Machine-readable section as the canonical data source. Validate:
1. standard v12 filename pattern
2. metadata-round-loop consistency
3. trigger_type is canonical Stage label
4. all trigger rows include entry_date, entry_price, MFE_30D/90D/180D, MAE_30D/90D/180D
5. price_source = Songdaiki/stock-web
6. price_basis = tradable_raw
7. price_adjustment_status = raw_unadjusted_marcap
8. corporate_action_window_status != contaminated

Potential patch candidate:
- Add or strengthen C23-specific bridge requirement:
  `C23_approval_label_to_revenue_royalty_commercialization_bridge_required`
- Do not alter global Stage2 bonus or global Green thresholds based on this file alone.
- Treat this as canonical-archetype-specific shadow evidence.
- Keep `evidence_url_pending=true` rows in a lower-trust bucket until official URL repair is completed.
```

## 10. Next Research State

```text
completed_round = R7
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C24_BIO_TRIAL_DATA_EVENT_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
