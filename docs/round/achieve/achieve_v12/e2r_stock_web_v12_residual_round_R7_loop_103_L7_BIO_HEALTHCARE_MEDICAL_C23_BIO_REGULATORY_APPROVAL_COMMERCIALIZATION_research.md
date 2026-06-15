# E2R v12 Stock-Web Residual Research — R7 Loop 103 — C23 Bio Regulatory Approval / Commercialization

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R7
selected_loop = 103
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
standard_v12_result_filename = e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

## 0. Selection and No-Repeat Check

The previous accepted conversation-local output ended at `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`. The visible No-Repeat index lists `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` as a remaining Priority 0 shortage at 12 rows, with 18 still needed to reach the 30-row floor. This loop adds four new independent C23 cases and avoids the previously used C23 basket (`196170`, `326030`, `069620`, `128940`) as well as the older representative cluster mentioned in the prior C23 run (`195940`, `145020`, `000100`, `009420`, `067630`, `068270`).

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
auto_selected_coverage_gap_static_index = C23 rows 12 -> 16 if accepted; still Priority 0, need 14 to 30
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

### Novelty / duplicate guard

| symbol | name | trigger date | trigger type | duplicate decision |
|---:|---|---:|---|---|
| 006280 | 녹십자 | 2024-07-09 | Stage2-Actionable | new C23 symbol/trigger family in this local ledger |
| 170900 | 동아에스티 | 2024-02-29 | Stage2 | new C23 symbol/trigger family in this local ledger |
| 185750 | 종근당 | 2024-07-10 | Stage2 | new C23 symbol/trigger family in this local ledger |
| 084990 | 헬릭스미스 | 2024-02-02 | Stage2 | new C23 symbol/trigger family in this local ledger |

## 1. Price Source Validation

The run used `Songdaiki/stock-web` symbol profiles and symbol-year shards only. Non-price evidence remains deliberately marked `source_proxy_only` / `evidence_url_pending=true`; this MD is a calibration handoff, not a final evidence URL repair pass.

| symbol | name | profile status | available 2024 shard | corporate-action overlap with selected 2024 window | validation note |
|---:|---|---|---|---|---|
| 006280 | 녹십자 | active_like | `atlas/ohlcv_tradable_by_symbol_year/006/006280/2024.csv` | no 2024 CA candidate in selected window | long listing history, raw/unadjusted; 2024 window usable |
| 170900 | 동아에스티 | active_like | `atlas/ohlcv_tradable_by_symbol_year/170/170900/2024.csv` | none | clean 2024 calibration window |
| 185750 | 종근당 | active_like | `atlas/ohlcv_tradable_by_symbol_year/185/185750/2024.csv` | none | clean 2024 calibration window |
| 084990 | 헬릭스미스 | active_like | `atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv` | historical CA candidates are pre-2024 | 2024 price path usable as negative control |

## 2. Case Notes

### 2.1 006280 / 녹십자 — approval-to-launch revenue bridge, but post-launch drawdown guard still required

This is the cleanest positive C23 sample in the loop. The entry is placed on 2024-07-09 close 124,900, after the market had begun to price an approval-to-commercial-launch bridge rather than a binary clinical-trial event. The 30D and 90D path is strong, with a peak at 181,800 by 2024-10-21. But the 180D path later gives back a large part of the move, so C23 needs two locks at once: reward approval-to-launch evidence, but still demand revenue/reimbursement proof after the rerating.

```text
entry_date = 2024-07-09
entry_price = 124,900
MFE_30D / MAE_30D = +33.71% / -2.32%
MFE_90D / MAE_90D = +45.56% / -2.32%
MFE_180D / MAE_180D = +45.56% / -10.49%
case_role = positive_commercialization_bridge_with_late_MAE
```

### 2.2 170900 / 동아에스티 — biosimilar/partner approval label is not enough without launch economics

The entry is 2024-02-29 close 74,900. The path gives an early high at 88,000, but then spends the rest of the window showing slow commercialization digestion and a trough near 59,900. That is not a failed idea; it is a slow bridge. C23 should keep this at Stage2 until the dossier moves from approval/partner vocabulary into royalty, supply, launch, or margin/revision evidence.

```text
entry_date = 2024-02-29
entry_price = 74,900
MFE_30D / MAE_30D = +17.49% / -11.35%
MFE_90D / MAE_90D = +17.49% / -20.03%
MFE_180D / MAE_180D = +17.49% / -20.03%
case_role = mixed_positive_slow_commercialization
```

### 2.3 185750 / 종근당 — regulatory/licensed pipeline label can rally, then decay

The entry is 2024-07-10 close 108,100. The 90D window reaches 130,200, but the later path slides to 94,500. This is exactly the residual error the C23 axis should compress: a label can be approved, licensed, or near-commercial, but unless there is visible revenue acceleration, reimbursement, royalty, or revision confirmation, the move behaves like a temporary pharma beta rather than a durable C23 positive.

```text
entry_date = 2024-07-10
entry_price = 108,100
MFE_30D / MAE_30D = +14.99% / -2.22%
MFE_90D / MAE_90D = +20.44% / -0.56%
MFE_180D / MAE_180D = +20.44% / -12.58%
case_role = mixed_false_positive_revenue_bridge_incomplete
```

### 2.4 084990 / 헬릭스미스 — price-only regulatory/pipeline spike is a negative control

The entry is 2024-02-02 close 4,410. The immediate 30D peak reaches 7,440, but the move is a price-only burst. The 180D trough later reaches about 3,020. This is the clean counterexample: C23 cannot be unlocked by regulatory/pipeline vocabulary if the asset is not already travelling through a credible approval-to-commercialization cash path.

```text
entry_date = 2024-02-02
entry_price = 4,410
MFE_30D / MAE_30D = +68.71% / -10.66%
MFE_90D / MAE_90D = +68.71% / -22.22%
MFE_180D / MAE_180D = +68.71% / -31.52%
case_role = counterexample_price_only_regulatory_spike
```

## 3. Current Calibrated Profile Stress Test

The current calibrated profile already blocks broad price-only blowoff and requires non-price evidence for full 4B. This loop does not re-propose that global rule. It proposes a narrower C23 compression:

```text
C23 positive credit should require at least one:
- approval -> launch -> sales bridge
- approval -> reimbursement -> prescription/procedure bridge
- partner approval -> royalty/milestone/supply bridge
- export launch -> revenue + margin/revision bridge

C23 positive credit should be capped when:
- evidence is only pipeline/regulatory vocabulary
- approval is not tied to near-term commercialization
- launch exists but sales/reimbursement/royalty path is unverified
- the MFE is mostly a price spike before commercial evidence arrives
```

Residual errors found:

| residual | case |
|---|---|
| underweighted approval-to-launch commercial route | 006280 |
| approval/partner label promoted too early before launch economics | 170900 |
| licensed/regulatory vocabulary treated as durable revenue bridge without revision proof | 185750 |
| price-only regulatory spike overcredited as positive stage | 084990 |

## 4. Local 4B / Full 4B Split

| symbol | local 4B condition | full-window 4B status | rule interpretation |
|---:|---|---|---|
| 006280 | not price-only; has commercialization bridge proxy | no full 4B block, but late-MAE guard required | positive C23 allowed only with post-launch proof |
| 170900 | no vertical blowoff | no full 4B block | keep Stage2 until launch economics show |
| 185750 | moderate rally, no vertical blowoff | no full 4B block | Stage2 only; do not upgrade to Stage3 without revision |
| 084990 | strong short-window price spike before cash bridge | full positive C23 blocked | route to local 4B watch / narrative-only cap |

## 5. Shadow Rule Candidate

```text
new_axis_proposed = C23_approval_to_commercial_cash_bridge_required

rule:
if canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:
    require at least one commercial cash bridge before Stage2-Actionable:
      - approval_to_launch_sales_bridge
      - reimbursement_or_prescription_conversion
      - partner_royalty_milestone_or_supply_bridge
      - export_sales_with_margin_revision_confirmation

    if evidence is only pipeline/regulatory vocabulary:
        cap at Stage2-watch or narrative-only
        block Stage3-Yellow and Stage3-Green

    if 30D MFE > +50% and commercial bridge is missing:
        route to local_4b_watch_guard
        do not allow full positive 4B without non-price commercial evidence

existing_axis_strengthened =
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
```

## 6. Machine-readable JSONL Rows

```jsonl
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "006280", "name": "녹십자", "case_id": "C23_006280_20240709_STAGE2A", "trigger_family": "approved_product_US_launch_revenue_bridge", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "case", "case_role": "positive_commercialization_bridge_with_late_MAE", "outcome_label": "positive_with_commercial_bridge_and_late_drawdown_guard", "evidence_summary": "C23 can under-reward approval-to-launch revenue bridge if evidence is treated as generic bio headline; still needs post-launch revenue confirmation after vertical rerating."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "170900", "name": "동아에스티", "case_id": "C23_170900_20240229_STAGE2", "trigger_family": "biosimilar_regulatory_approval_to_partner_launch_bridge", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "case", "case_role": "mixed_positive_slow_commercialization", "outcome_label": "mixed_positive_with_long_MAE_before_revenue_bridge", "evidence_summary": "Regulatory approval/partner vocabulary is not enough when launch economics and royalty/supply revenue are not yet visible."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "185750", "name": "종근당", "case_id": "C23_185750_20240710_STAGE2", "trigger_family": "licensed_or_approved_pipeline_label_without_revision_confirmation", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "case", "case_role": "mixed_false_positive_revenue_bridge_incomplete", "outcome_label": "mixed_positive_then_decay", "evidence_summary": "A near-term rally can occur on regulatory/commercial vocabulary, but without revenue acceleration and revision bridge it decays back into ordinary pharma beta."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "084990", "name": "헬릭스미스", "case_id": "C23_084990_20240202_STAGE2", "trigger_family": "pipeline_regulatory_label_without_commercialization_path", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "case", "case_role": "counterexample_price_only_regulatory_spike", "outcome_label": "counterexample_price_only_blowoff_then_decay", "evidence_summary": "This is the negative control: price spike around regulatory/pipeline vocabulary must not unlock C23 positive credit without commercial launch, reimbursement, or sales bridge."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "006280", "name": "녹십자", "case_id": "C23_006280_20240709_STAGE2A", "trigger_family": "approved_product_US_launch_revenue_bridge", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "trigger", "trigger_id": "C23_006280_20240709_STAGE2A_TRIGGER", "trigger_type": "Stage2-Actionable", "entry_date": "2024-07-09", "entry_price": 124900, "mfe_30d_pct": 33.71, "mae_30d_pct": -2.32, "mfe_90d_pct": 45.56, "mae_90d_pct": -2.32, "mfe_180d_pct": 45.56, "mae_180d_pct": -10.49, "peak_180d_date": "2024-10-21", "peak_180d_price": 181800, "trough_180d_date": "2025-04-09", "trough_180d_price": 111800, "local_4b_watch": false, "full_4b_positive_allowed": null, "raw_component_score_breakdown": "Info 17 / Supply 9 / Execution 15 / Revision 12 / Price 15 / Risk -6 = 62 before bridge; Stage2A after commercial bridge bonus", "current_calibrated_profile_error": "C23 can under-reward approval-to-launch revenue bridge if evidence is treated as generic bio headline; still needs post-launch revenue confirmation after vertical rerating."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "170900", "name": "동아에스티", "case_id": "C23_170900_20240229_STAGE2", "trigger_family": "biosimilar_regulatory_approval_to_partner_launch_bridge", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "trigger", "trigger_id": "C23_170900_20240229_STAGE2_TRIGGER", "trigger_type": "Stage2", "entry_date": "2024-02-29", "entry_price": 74900, "mfe_30d_pct": 17.49, "mae_30d_pct": -11.35, "mfe_90d_pct": 17.49, "mae_90d_pct": -20.03, "mfe_180d_pct": 17.49, "mae_180d_pct": -20.03, "peak_180d_date": "2024-03-07", "peak_180d_price": 88000, "trough_180d_date": "2024-06-14", "trough_180d_price": 59900, "local_4b_watch": false, "full_4b_positive_allowed": null, "raw_component_score_breakdown": "Info 15 / Supply 7 / Execution 12 / Revision 7 / Price 8 / Risk -8 = 41; should remain Stage2 until commercialization proof", "current_calibrated_profile_error": "Regulatory approval/partner vocabulary is not enough when launch economics and royalty/supply revenue are not yet visible."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "185750", "name": "종근당", "case_id": "C23_185750_20240710_STAGE2", "trigger_family": "licensed_or_approved_pipeline_label_without_revision_confirmation", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "trigger", "trigger_id": "C23_185750_20240710_STAGE2_TRIGGER", "trigger_type": "Stage2", "entry_date": "2024-07-10", "entry_price": 108100, "mfe_30d_pct": 14.99, "mae_30d_pct": -2.22, "mfe_90d_pct": 20.44, "mae_90d_pct": -0.56, "mfe_180d_pct": 20.44, "mae_180d_pct": -12.58, "peak_180d_date": "2024-08-28", "peak_180d_price": 130200, "trough_180d_date": "2024-11-18", "trough_180d_price": 94500, "local_4b_watch": false, "full_4b_positive_allowed": null, "raw_component_score_breakdown": "Info 14 / Supply 5 / Execution 10 / Revision 6 / Price 11 / Risk -7 = 39; no Stage3 without revenue/revision proof", "current_calibrated_profile_error": "A near-term rally can occur on regulatory/commercial vocabulary, but without revenue acceleration and revision bridge it decays back into ordinary pharma beta."}
{"research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "084990", "name": "헬릭스미스", "case_id": "C23_084990_20240202_STAGE2", "trigger_family": "pipeline_regulatory_label_without_commercialization_path", "source_proxy_only": true, "evidence_url_pending": true, "calibration_usable": true, "row_type": "trigger", "trigger_id": "C23_084990_20240202_STAGE2_TRIGGER", "trigger_type": "Stage2", "entry_date": "2024-02-02", "entry_price": 4410, "mfe_30d_pct": 68.71, "mae_30d_pct": -10.66, "mfe_90d_pct": 68.71, "mae_90d_pct": -22.22, "mfe_180d_pct": 68.71, "mae_180d_pct": -31.52, "peak_180d_date": "2024-02-06", "peak_180d_price": 7440, "trough_180d_date": "2024-11-15", "trough_180d_price": 3020, "local_4b_watch": true, "full_4b_positive_allowed": false, "raw_component_score_breakdown": "Info 12 / Supply 3 / Execution 4 / Revision 2 / Price 18 / Risk -18 = 21; local 4B watch and cap at narrative-only", "current_calibrated_profile_error": "This is the negative control: price spike around regulatory/pipeline vocabulary must not unlock C23 positive credit without commercial launch, reimbursement, or sales bridge."}
```

## 7. Aggregate Metrics

```json
{
  "row_type": "aggregate_metric",
  "research_file": "e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 2,
  "counterexample_count": 1,
  "local_4b_watch_count": 1,
  "current_profile_error_count": 4,
  "auto_selected_coverage_gap_static_index": "C23 rows 12 -> 16 if accepted; still Priority 0, need 14 to 30",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false
}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute this section during research generation.

You are the later batch implementation agent for stock_agent.

Input MD:
- e2r_stock_web_v12_residual_round_R7_loop_103_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Implement only after multiple v12 residual MDs have been reviewed together.

Candidate axis:
- C23_approval_to_commercial_cash_bridge_required

Implementation intent:
- Add C23-specific guard/bonus logic that distinguishes approval-to-commercialization cash bridge from pipeline/regulatory vocabulary.
- Positive C23 credit requires approval->launch sales, reimbursement/prescription conversion, partner royalty/milestone/supply bridge, or export sales with margin/revision confirmation.
- If C23 evidence is only regulatory/pipeline vocabulary, cap at Stage2-watch/narrative-only and block Stage3.
- If short-window price MFE is large while commercial evidence is missing, route to local 4B watch and require non-price commercial proof for full 4B.

Do not change production scoring from this single MD alone.
Batch with other C23/C24/C25 bio/healthcare residual outputs first.
```

## 9. Residual Contribution Summary

```text
selected_round = R7
selected_loop = 103
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_REIMBURSEMENT_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 1
local_4b_watch_count = 1
current_profile_error_count = 4
new_axis_proposed = C23_approval_to_commercial_cash_bridge_required
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C24_BIO_TRIAL_DATA_EVENT_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN
```
