---
research_file: e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R7
scheduled_loop: 89
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: APPROVAL_TO_COMMERCIAL_REVENUE_BRIDGE_VS_PIPELINE_HEADLINE_FALSE_POSITIVE
round_schedule_status: valid
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
completed_round: R7
completed_loop: 89
next_round: R8
next_loop: 89
---

# E2R v12 Residual Research — R7/L89/C23 Bio Approval-to-Commercialization Bridge

## 0. Execution status

```text
scheduled_round = R7
scheduled_loop = 89
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = APPROVAL_TO_COMMERCIAL_REVENUE_BRIDGE_VS_PIPELINE_HEADLINE_FALSE_POSITIVE

round_schedule_status = valid
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file follows the v12 rule that the research runner uses the sequential round cycle first, then fills coverage gaps only within the scheduled round. Since the previous completed file was `R6 / loop 89`, this run advances to `R7 / loop 89`. R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`.

The output is a standalone historical calibration Markdown file. It does not modify `stock_agent` production scoring. It only proposes a shadow rule candidate for later batch review.

## 1. Why C23 in this run

The previous local R7 run in loop 88 covered `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT`. This R7 pass therefore avoids repeating medical devices and shifts to `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`.

No-Repeat snapshot shows C23 already has coverage, but with several repeated or ambiguous symbols. The top-covered C23 names include `UNKNOWN_SYMBOL`, `028300`, `000100`, `039200`, `195940`, and `003850`. This run avoids those and uses:

```text
326030 SK바이오팜
068270 셀트리온
128940 한미약품
```

All three are active-like in the stock-web profile. SK바이오팜 and 한미약품 have no corporate-action candidate dates in their 2024 sample windows. 셀트리온 has a corporate-action candidate on `2024-01-12`, so this run avoids the contaminated early-January window and uses a post-candidate entry date.

## 2. Residual question

C23 should reward **approval-to-commercialization evidence**, not mere clinical or pipeline excitement.

The model needs to distinguish three routes:

```text
Route A — Approved/commercial drug revenue bridge
  approval or launched product + recurring sales/profit path + actual price confirmation

Route B — Approval/commercialization watch
  approved/launch headline + MFE, but insufficient evidence that revenue/margin bridge has hardened

Route C — Pipeline headline false positive
  clinical/platform/obesity/drug-development excitement without approved-product revenue conversion
```

The calibration problem is like a pharmacy shelf: a drug candidate on a lab bench is not the same thing as boxed inventory moving through the till. C23 should score the cash register, not the poster on the wall.

## 3. Representative cases

### Case 1 — 326030 SK바이오팜 — positive with local 4B overlay

```text
symbol = 326030
name = SK바이오팜
entry_date = 2024-07-12
entry_close = 83,000
trigger_type = approved_drug_commercial_sales_acceleration_bridge
classification = positive_with_local_4b_overlay
```

Price path from stock-web:

```text
entry_close = 83,000
30D/90D trough proxy = 72,600
90D peak proxy = 119,500
180D peak proxy = 129,800

MFE_30D ≈ +34.58%
MAE_30D ≈ -12.53%
MFE_90D ≈ +43.98%
MAE_90D ≈ -12.53%
MFE_180D ≈ +56.39%
MAE_180D ≈ -12.53%
```

Interpretation:

SK바이오팜 is the useful positive control. The signal is not just “bio headline.” It has a commercial-stage drug/revenue/profitability bridge. That is exactly the bridge C23 should respect. However, the move becomes price-stretched after +40% MFE, so the correct route is not blind Green; it is Stage3-Yellow/Green candidate with local 4B overlay.

```text
profile_response_ref = turn315
price_response_refs = turn317, turn318, turn323
```

### Case 2 — 068270 셀트리온 — watch positive, not Green

```text
symbol = 068270
name = 셀트리온
entry_date = 2024-07-01
entry_close = 184,100
trigger_type = biosimilar_launch_commercialization_watch
classification = watch_positive_but_not_green
```

Price path from stock-web:

```text
entry_close = 184,100
peak proxy = 211,000
trough proxy = 160,300

MFE_30D ≈ +14.61%
MAE_30D ≈ -6.03%
MFE_90D ≈ +14.61%
MAE_90D ≈ -12.93%
MFE_180D ≈ +14.61%
MAE_180D ≈ -12.93%
```

Interpretation:

셀트리온 shows why C23 cannot be binary. Commercialization language produces a tradable MFE, but full-window persistence is weaker than in SK바이오팜. The guardrail should allow Stage2-Actionable / Yellow watch when a launch or approved product exists, but Green should require a visible margin/revenue bridge and evidence that the launch is changing revision quality.

The 2024-01-12 corporate-action candidate is outside this entry window, so the July entry is calibration-usable.

```text
profile_response_ref = turn314
price_response_refs = turn319, turn320, turn325, turn324
```

### Case 3 — 128940 한미약품 — counterexample

```text
symbol = 128940
name = 한미약품
entry_date = 2024-03-25
entry_close = 347,000
trigger_type = pipeline_headline_without_approval_to_revenue_bridge
classification = counterexample_high_mae
```

Price path from stock-web:

```text
entry_close = 347,000
peak proxy = 350,000
trough proxy = 258,000

MFE_30D ≈ +0.86%
MAE_30D ≈ -14.55%
MFE_90D ≈ +0.86%
MAE_90D ≈ -25.65%
MFE_180D ≈ +0.86%
MAE_180D ≈ -25.65%
```

Interpretation:

한미약품 is the false-positive guard. The price path behaves like a pipeline/optional-value headline that did not convert into approved-product revenue. For C23, this should not be promoted as approval/commercialization evidence. It belongs in Stage2/Watch or counterexample handling unless the row contains named approval, launch, reimbursement, milestone-to-sales, or recurring revenue evidence.

```text
profile_response_ref = turn316
price_response_refs = turn321, turn326, turn322
```

## 4. Raw component score simulation

This is a shadow simulation only. It does not patch production scoring.

| symbol | current profile likely behavior | residual issue | proposed C23 treatment |
|---|---:|---|---|
| 326030 | could pass Stage2/Yellow on bio commercial momentum | Needs local 4B after large MFE | Positive, but require commercial sales/profit bridge and local 4B after +40% |
| 068270 | could be promoted too early on launch/commercialization headline | MFE exists but not durable enough for Green | Stage2-Actionable / Yellow watch; Green requires margin/revenue bridge |
| 128940 | could be over-scored as bio/pipeline excitement | No approved-product revenue bridge, high MAE | Counterexample / block C23 Green |

Suggested component gates:

```text
C23_required_non_price_bridge:
  - named approved product or regulatory approval
  - launch/commercialization timing
  - reimbursement or payer access where relevant
  - recurring revenue / sales ramp / royalty / milestone-to-sales evidence
  - margin, EPS, or revision bridge

C23_block_or_downshift:
  - clinical/pipeline-only headline
  - partner/platform optionality without approval/commercial revenue
  - price-only rally after vague bio theme
  - high-MAE path without revision bridge
```

## 5. Machine-readable rows

```jsonl
{"calibration_usable": true, "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "case_id": "R7L89_C23_POS_326030_2024-07-12", "classification": "positive_with_local_4b_overlay", "do_not_propose_new_weight_delta": true, "duplicate_check_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|approved_drug_commercial_sales_acceleration_bridge|2024-07-12", "entry_close": 83000, "entry_date": "2024-07-12", "evidence_summary": "commercial-stage CNS drug sales/profitability bridge treated as stronger than mere regulatory approval headline", "fine_archetype_id": "APPROVAL_TO_COMMERCIAL_REVENUE_BRIDGE_VS_PIPELINE_HEADLINE_FALSE_POSITIVE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_180d_pct": -12.53, "mae_30d_pct": -12.53, "mae_90d_pct": -12.53, "mfe_180d_pct": 56.39, "mfe_30d_pct": 34.58, "mfe_90d_pct": 43.98, "name": "SK바이오팜", "peak_price": 129800, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "row_type": "case", "scheduled_loop": 89, "scheduled_round": "R7", "stage_judgment": "Stage3-Yellow candidate; Green requires recurring revenue/profit confirmation and non-price evidence", "stock_web_manifest_max_date": "2026-02-20", "symbol": "326030", "trigger_type": "approved_drug_commercial_sales_acceleration_bridge", "trough_price": 72600, "why": "Unlike binary approval events, commercialized drug sales/profit conversion had enough bridge to sustain a multi-month rerating, though the Aug-2024 drawdown and >40% MFE require local 4B overlay."}
{"calibration_usable": true, "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "case_id": "R7L89_C23_WATCH_068270_2024-07-01", "classification": "watch_positive_but_not_green", "do_not_propose_new_weight_delta": true, "duplicate_check_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|068270|biosimilar_launch_commercialization_watch|2024-07-01", "entry_close": 184100, "entry_date": "2024-07-01", "evidence_summary": "launch/commercialization headline produced MFE but not enough sustained 180D reward without clearer margin/revenue bridge", "fine_archetype_id": "APPROVAL_TO_COMMERCIAL_REVENUE_BRIDGE_VS_PIPELINE_HEADLINE_FALSE_POSITIVE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_180d_pct": -12.93, "mae_30d_pct": -6.03, "mae_90d_pct": -12.93, "mfe_180d_pct": 14.61, "mfe_30d_pct": 14.61, "mfe_90d_pct": 14.61, "name": "셀트리온", "peak_price": 211000, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "row_type": "case", "scheduled_loop": 89, "scheduled_round": "R7", "stage_judgment": "Stage2-Actionable watch / Stage3-Yellow only with cross-evidence; block Green without margin/revenue bridge", "stock_web_manifest_max_date": "2026-02-20", "symbol": "068270", "trigger_type": "biosimilar_launch_commercialization_watch", "trough_price": 160300, "why": "Commercialization language alone created a valid MFE window, but full-window persistence was weak. This is the middle case that prevents C23 from treating all approved-product headlines as Green."}
{"calibration_usable": true, "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "case_id": "R7L89_C23_COUNTER_128940_2024-03-25", "classification": "counterexample_high_mae", "do_not_propose_new_weight_delta": true, "duplicate_check_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|128940|pipeline_headline_without_approval_to_revenue_bridge|2024-03-25", "entry_close": 347000, "entry_date": "2024-03-25", "evidence_summary": "pipeline/clinical/obesity-drug excitement without approved-drug commercial revenue conversion failed to sustain rerating", "fine_archetype_id": "APPROVAL_TO_COMMERCIAL_REVENUE_BRIDGE_VS_PIPELINE_HEADLINE_FALSE_POSITIVE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "mae_180d_pct": -25.65, "mae_30d_pct": -14.55, "mae_90d_pct": -25.65, "mfe_180d_pct": 0.86, "mfe_30d_pct": 0.86, "mfe_90d_pct": 0.86, "name": "한미약품", "peak_price": 350000, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "row_type": "case", "scheduled_loop": 89, "scheduled_round": "R7", "stage_judgment": "Counterexample; should remain Stage2/Watch unless approval/commercial revenue bridge appears", "stock_web_manifest_max_date": "2026-02-20", "symbol": "128940", "trigger_type": "pipeline_headline_without_approval_to_revenue_bridge", "trough_price": 258000, "why": "The price path looks like the model confusing pipeline optionality with C23 approval-to-commercialization evidence. High MAE and almost no MFE argue for a C23 guardrail."}
{"calibration_usable_trigger_count": 3, "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "canonical_archetype_rule_candidate": true, "counterexample_count": 1, "do_not_propose_new_weight_delta": true, "hard_4c_candidate_count": 0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "local_4b_overlay_case_count": 1, "loop_contribution_label": "residual_error_found", "new_independent_case_count": 3, "next_loop": 89, "next_round": "R8", "positive_case_count": 1, "research_file": "e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "row_type": "aggregate", "same_archetype_new_symbol_count": 3, "scheduled_loop": 89, "scheduled_round": "R7", "watch_positive_count": 1}
```

## 6. Residual contribution summary

```text
new_independent_case_count = 3
same_archetype_new_symbol_count = 3
positive_case_count = 1
watch_positive_count = 1
counterexample_count = 1
local_4b_overlay_case_count = 1
calibration_usable_trigger_count = 3

loop_contribution_label = residual_error_found
canonical_archetype_rule_candidate = true
do_not_propose_new_weight_delta = true
```

This run strengthens C23 by separating **approval-to-commercialization evidence** from **pipeline optionality**. The main residual error is not that C23 is too weak globally. The error is that the model can still treat a lab-bench story as if it were a pharmacy-sales story.

## 7. Proposed shadow rule

```text
C23_APPROVAL_COMMERCIALIZATION_BRIDGE_GUARD

If canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:

1. Permit Stage2-Actionable only when at least one hard commercialization bridge exists:
   - approved product
   - active launch / sales ramp
   - reimbursement or access path
   - royalty / milestone-to-sales conversion
   - recurring revenue or profit bridge

2. Permit Stage3-Yellow when:
   - hard commercialization bridge exists, and
   - price path confirms MFE without immediate thesis-break MAE.

3. Permit Stage3-Green only when:
   - approval/commercialization bridge is paired with revision, margin, royalty, or recurring sales evidence, and
   - the case is not merely price-only or pipeline-only.

4. Downshift to Watch/Counterexample when:
   - the row is only clinical/pipeline excitement,
   - partner/platform optionality has no approved-product revenue conversion,
   - or MFE is weak while MAE is large.
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the later batch coding agent for Songdaiki/stock_agent.

Use this MD only as a research artifact. Do not infer production code paths from it.
Review the machine-readable rows and the proposed shadow rule:

C23_APPROVAL_COMMERCIALIZATION_BRIDGE_GUARD

Task:
1. In the research-ingestion layer, parse the JSONL rows from this MD.
2. Do not change production scoring directly from a single MD.
3. Aggregate this MD with other v12 residual calibration files.
4. If the C23 rule is confirmed across enough independent cases, propose a small canonical-specific guard:
   - require approved/commercial revenue bridge before C23 Green,
   - downshift pipeline-only headlines to Watch/Counterexample,
   - apply local 4B overlay when price outruns evidence.
5. Preserve No-Repeat semantics:
   duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date.
6. Leave production_scoring_changed = false unless a separate explicit patch session is opened.
```

## 9. Next round

```text
completed_round = R7
completed_loop = 89
next_round = R8
next_loop = 89
```
