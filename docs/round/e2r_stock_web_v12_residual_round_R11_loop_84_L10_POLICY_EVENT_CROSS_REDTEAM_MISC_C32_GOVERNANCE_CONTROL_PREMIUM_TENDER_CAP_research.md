# E2R Stock-Web v12 Residual Research — R11 Loop 84 / L10 / C32

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 84,
  "computed_next_round": "R12",
  "computed_next_loop": 84,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "governance_control_premium_tender_cap_guardrail",
    "tender_floor_vs_theme_squeeze_split",
    "control_premium_price_cap_and_local_4B_timing",
    "hard_4C_non_price_thesis_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 84
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R12
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R11 is the policy / event / cross-redteam slot. This run selects C32 rather than repeating C31 because loop83 and loop84 already covered many policy/subsidy rows, while the governance / control-premium / tender-cap bucket still needs a cleaner floor-vs-theme split.

The tested mechanism:

```text
governance / control-premium / tender-offer headline
→ tender or transaction floor
→ binding terms and buyer / competing-bid quality
→ acceptance ratio, closing path or capital-return execution
→ durable rerating or local 4B / asset-value theme fade
```

C32 is the auction room. A headline can open the door, but the model should only price a floor when the bid terms, closing path and residual value are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C32 top-covered symbols include `010130`, `041510`, `008930`, `011200`, `UNKNOWN_SYMBOL`, and `003920`. This run avoids that top-covered set and uses:

```text
036560 / 영풍정밀
001750 / 한양증권
003240 / 태광산업
```

All three are treated as new independent C32 governance/control-premium cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company at trigger | profile path | corporate-action caveat |
|---|---|---|---|
| 036560 | 영풍정밀 | `atlas/symbol_profiles/036/036560.json` | old 2008 CA candidate; selected 2024/2025 forward window clean |
| 001750 | 한양증권 | `atlas/symbol_profiles/001/001750.json` | no profile-level CA candidate |
| 003240 | 태광산업 | `atlas/symbol_profiles/003/003240.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R11L84-C32-01 | 036560 | 2024-09-13 | 12,180 | 180D | clean | true |
| R11L84-C32-02 | 001750 | 2024-07-15 | 15,000 | 180D | clean | true |
| R11L84-C32-03 | 003240 | 2024-01-25 | 636,000 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TENDER_OFFER_CONTROL_PREMIUM_FLOOR | keep Stage2 only with tender price, acceptance cap, residual-float path and competing-bid probability |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_STAKE_SALE_DEAL_RISKWATCH | allow Stage2 only with deal-closing / buyer-quality / regulatory RiskWatch |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | ASSET_VALUE_GOVERNANCE_THEME_BLOWOFF | reject or local-4B-watch when price MFE lacks binding floor or capital-return execution |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R11L84-C32-01 | 036560 | 영풍정밀 | Stage2-Actionable | 2024-09-13 | 12,180 | 201.31 | -15.76 | current_profile_4B_too_late_after_tender_MFE |
| R11L84-C32-02 | 001750 | 한양증권 | Stage2-Actionable | 2024-07-15 | 15,000 | 29.4 | -24.67 | current_profile_partially_correct_deal_riskwatch_needed |
| R11L84-C32-03 | 003240 | 태광산업 | Stage2-FalsePositive | 2024-01-25 | 636,000 | 56.29 | -19.81 | current_profile_false_positive_theme_blowoff |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C32 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: tender-offer filing, bid price, acceptance cap, competing bid, buyer quality, binding SPA, regulatory closing path, capital-return execution or official disclosure.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 036560 | `atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv` and `2025.csv` | `atlas/symbol_profiles/036/036560.json` |
| 001750 | `atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv` and `2025.csv` | `atlas/symbol_profiles/001/001750.json` |
| 003240 | `atlas/ohlcv_tradable_by_symbol_year/003/003240/2024.csv` | `atlas/symbol_profiles/003/003240.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 036560 / 영풍정밀

C32 tender/control-premium positive, but the price path is also the cleanest local-4B lesson. The MFE was extreme after the entry-date tender/control headline proxy. Once the stock trades materially above a deal floor or implied control premium, the model should carry a tender-cap local 4B watch instead of treating the whole move as clean Stage3.

### Case 2 — 001750 / 한양증권

C32 control-sale positive but high-MAE deal-risk case. The MFE was real, but the later drawdown shows that deal certainty matters. Buyer quality, binding terms, regulatory approval and closing probability should be repaired before any clean Green label.

### Case 3 — 003240 / 태광산업

C32 governance / asset-value theme blowoff counterexample. MFE was large, but there was no clear tender floor in this proxy row. Without binding transaction terms or capital-return execution, the original Stage2 should be demoted to local 4B / RiskWatch.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 036560 | 12,180 | 201.31 | 0.00 | 201.31 | -3.94 | 201.31 | -15.76 | 2024-10-07 / 36,700 | -72.04 |
| 001750 | 15,000 | 29.40 | -5.87 | 29.40 | -17.93 | 29.40 | -24.67 | 2024-08-05 / 19,410 | -41.78 |
| 003240 | 636,000 | 56.29 | -3.30 | 56.29 | -3.46 | 56.29 | -19.81 | 2024-01-30 / 994,000 | -48.69 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R11L84-C32-01 | Stage2-Actionable if tender/control bridge exists | extreme MFE then large post-peak drawdown | 4B too late after tender MFE |
| R11L84-C32-02 | Stage2-Actionable if control-sale path exists | MFE then high MAE | deal-closing RiskWatch needed |
| R11L84-C32-03 | risk of treating governance asset-value theme as Stage2 | high MFE but high later MAE | false positive / theme blowoff |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C32, the residual is not Green lateness. The residual is whether governance/control-premium MFE becomes clean Stage2/Green before tender floor, binding terms, closing path and residual-value bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R11L84-C32-01 | 0.95 | 0.85 | local 4B watch required when price exceeds tender floor or control-premium cap |
| R11L84-C32-02 | 0.80 | 0.70 | local 4B and deal-closing RiskWatch when control-sale MFE outruns binding terms |
| R11L84-C32-03 | 0.35 | 0.30 | asset-value governance MFE rejected or local-4B-watch without tender/capital-return bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_deal_break_or_tender_withdrawal
hard_4c_price_only_allowed = false
```

A governance/tender row can drop sharply after a deal premium unwinds. That is not enough for hard 4C unless the source-repair pass confirms tender withdrawal, deal break, regulatory block, or failure of the capital-return/governance thesis.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L10/C32 rows need tender/transaction floor, binding terms, buyer quality, closing path and capital-return execution before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
candidate_axis = C32_tender_transaction_floor_binding_terms_closing_bridge_required
effect = keep tender/control positives with local 4B or deal-risk watch; demote asset-value governance theme blowoffs
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 95.67 | -8.44 | may over-credit governance/control-premium MFE | needs C32 floor/closing bridge repair |
| P1 canonical shadow bridge profile | 3 | 115.36 on kept positives | keeps positives under tender-cap/deal-risk watch | demotes 003240 asset-value theme blowoff | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R11L84-C32-01 | 82 | Stage2-Actionable | 78 | Stage2-Actionable + tender-cap/local 4B watch | partially aligned |
| R11L84-C32-02 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + deal-closing/high-MAE RiskWatch | partially aligned |
| R11L84-C32-03 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Governance-theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
residual_error_types_found:
  - governance_asset_value_theme_false_positive_high_MAE
  - tender_transaction_floor_binding_terms_required
  - local_4B_late_after_control_premium_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_deal_break_not_price_only
new_axis_proposed: false
existing_axis_strengthened:
  - C32_tender_transaction_floor_binding_terms_closing_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C32_tender_transaction_floor_binding_terms_closing_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- tender-offer price and acceptance cap
- binding SPA / deal-closing path
- buyer or competing-bid quality
- capital-return execution
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_tender_transaction_floor_binding_terms_closing_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Require tender/transaction floor, binding terms, buyer or competing-bid quality, closing path and capital-return execution before clean Stage2/Green","keeps 036560/001750 with tender-cap or deal-risk watch; demotes 003240","R11L84-C32-01-S2A-20240913|R11L84-C32-02-S2A-20240715|R11L84-C32-03-S2FP-20240125",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L84-C32-01", "symbol": "036560", "company_name": "영풍정밀", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE", "case_type": "tender_offer_control_premium_positive_with_price_cap_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L84-C32-01-S2A-20240913", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "extreme_control_premium_MFE_but_tender_cap_and_local_4B_required", "current_profile_verdict": "current_profile_4B_too_late_after_tender_MFE", "price_source": "Songdaiki/stock-web", "notes": "C32 tender/control cases need tender price, acceptance cap, competing-bid probability and residual float path; price above tender floor requires local 4B watch."}
{"row_type": "trigger", "trigger_id": "R11L84-C32-01-S2A-20240913", "case_id": "R11L84-C32-01", "symbol": "036560", "company_name": "영풍정밀", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail|tender_floor_vs_theme_squeeze_split|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "tender offer / control premium / strategic stake contest proxy; primary tender terms and acceptance-ratio evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["control_premium_proxy", "tender_or_transaction_floor_proxy", "governance_catalyst_proxy"], "stage3_evidence_fields": ["binding_terms", "buyer_quality", "acceptance_probability", "closing_path", "capital_return_execution"], "stage4b_evidence_fields": ["price_above_tender_floor", "governance_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_deal_break_or_tender_withdrawal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv", "profile_path": "atlas/symbol_profiles/036/036560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 12180, "MFE_30D_pct": 201.31, "MFE_90D_pct": 201.31, "MFE_180D_pct": 201.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": -3.94, "MAE_180D_pct": -15.76, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 36700, "drawdown_after_peak_pct": -72.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "local_4B_watch_required_when_price_exceeds_tender_floor_or_control_premium_cap", "four_b_evidence_type": ["price_above_tender_floor_or_deal_cap", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_deal_break_or_tender_withdrawal", "trigger_outcome_label": "extreme_control_premium_MFE_but_tender_cap_and_local_4B_required", "current_profile_verdict": "current_profile_4B_too_late_after_tender_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2008_CA_candidate", "same_entry_group_id": "R11L84-C32-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L84-C32-01", "trigger_id": "R11L84-C32-01-S2A-20240913", "symbol": "036560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"control_premium_specificity_score": 55, "tender_or_transaction_floor_score": 45, "binding_term_quality_score": 35, "buyer_or_competing_bid_quality_score": 40, "acceptance_or_closing_probability_score": 35, "capital_return_execution_score": 20, "governance_catalyst_score": 55, "relative_strength_score": 80, "valuation_blowoff_risk_score": 85, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"control_premium_specificity_score": 55, "tender_or_transaction_floor_score": 45, "binding_term_quality_score": 35, "buyer_or_competing_bid_quality_score": 40, "acceptance_or_closing_probability_score": 35, "capital_return_execution_score": 20, "governance_catalyst_score": 55, "relative_strength_score": 80, "valuation_blowoff_risk_score": 90, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 90}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable + tender-cap/local 4B watch", "changed_components": ["tender_or_transaction_floor_score", "binding_term_quality_score", "acceptance_or_closing_probability_score", "capital_return_execution_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C32 requires tender/transaction floor, binding terms, buyer or competing-bid quality, closing path and capital-return execution before clean Stage2/Green; asset-value theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 201.31, "MAE_90D_pct": -3.94, "score_return_alignment_label": "extreme_control_premium_MFE_but_tender_cap_and_local_4B_required", "current_profile_verdict": "current_profile_4B_too_late_after_tender_MFE"}
{"row_type": "case", "case_id": "R11L84-C32-02", "symbol": "001750", "company_name": "한양증권", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE", "case_type": "control_sale_premium_positive_but_high_MAE_risk", "positive_or_counterexample": "positive", "best_trigger": "R11L84-C32-02-S2A-20240715", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control_premium_MFE_but_high_MAE_and_deal_riskwatch", "current_profile_verdict": "current_profile_partially_correct_deal_riskwatch_needed", "price_source": "Songdaiki/stock-web", "notes": "Control-sale positives can stay Stage2 only with buyer quality, binding terms, regulatory/closing path and premium-floor bridge."}
{"row_type": "trigger", "trigger_id": "R11L84-C32-02-S2A-20240715", "case_id": "R11L84-C32-02", "symbol": "001750", "company_name": "한양증권", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail|tender_floor_vs_theme_squeeze_split|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-15", "evidence_available_at_that_date": "control-stake sale / M&A premium proxy; primary binding-bid, buyer-quality and transaction-floor evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["control_premium_proxy", "tender_or_transaction_floor_proxy", "governance_catalyst_proxy"], "stage3_evidence_fields": ["binding_terms", "buyer_quality", "acceptance_probability", "closing_path", "capital_return_execution"], "stage4b_evidence_fields": ["price_above_tender_floor", "governance_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_deal_break_or_tender_withdrawal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv", "profile_path": "atlas/symbol_profiles/001/001750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-15", "entry_price": 15000, "MFE_30D_pct": 29.4, "MFE_90D_pct": 29.4, "MFE_180D_pct": 29.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.87, "MAE_90D_pct": -17.93, "MAE_180D_pct": -24.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-05", "peak_price": 19410, "drawdown_after_peak_pct": -41.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "local_4B_and_deal_closing_RiskWatch_needed_when_control_sale_MFE_outruns_binding_terms", "four_b_evidence_type": ["price_above_tender_floor_or_deal_cap", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_deal_break_or_tender_withdrawal", "trigger_outcome_label": "control_premium_MFE_but_high_MAE_and_deal_riskwatch", "current_profile_verdict": "current_profile_partially_correct_deal_riskwatch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_no_profile_CA_candidate", "same_entry_group_id": "R11L84-C32-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L84-C32-02", "trigger_id": "R11L84-C32-02-S2A-20240715", "symbol": "001750", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"control_premium_specificity_score": 55, "tender_or_transaction_floor_score": 35, "binding_term_quality_score": 35, "buyer_or_competing_bid_quality_score": 40, "acceptance_or_closing_probability_score": 35, "capital_return_execution_score": 20, "governance_catalyst_score": 55, "relative_strength_score": 60, "valuation_blowoff_risk_score": 65, "execution_risk_score": 65, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"control_premium_specificity_score": 55, "tender_or_transaction_floor_score": 35, "binding_term_quality_score": 35, "buyer_or_competing_bid_quality_score": 40, "acceptance_or_closing_probability_score": 35, "capital_return_execution_score": 20, "governance_catalyst_score": 55, "relative_strength_score": 60, "valuation_blowoff_risk_score": 75, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + deal-closing/high-MAE RiskWatch", "changed_components": ["tender_or_transaction_floor_score", "binding_term_quality_score", "acceptance_or_closing_probability_score", "capital_return_execution_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C32 requires tender/transaction floor, binding terms, buyer or competing-bid quality, closing path and capital-return execution before clean Stage2/Green; asset-value theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 29.4, "MAE_90D_pct": -17.93, "score_return_alignment_label": "control_premium_MFE_but_high_MAE_and_deal_riskwatch", "current_profile_verdict": "current_profile_partially_correct_deal_riskwatch_needed"}
{"row_type": "case", "case_id": "R11L84-C32-03", "symbol": "003240", "company_name": "태광산업", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE", "case_type": "governance_asset_value_theme_blowoff_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R11L84-C32-03-S2FP-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "governance_theme_blowoff_high_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff", "price_source": "Songdaiki/stock-web", "notes": "Asset-value/governance MFE is not enough; C32 requires tender floor, binding transaction terms, capital-return execution, or governance action path."}
{"row_type": "trigger", "trigger_id": "R11L84-C32-03-S2FP-20240125", "case_id": "R11L84-C32-03", "symbol": "003240", "company_name": "태광산업", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_VALUEUP_FLOOR_BRIDGE_VS_ASSET_VALUE_THEME_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail|tender_floor_vs_theme_squeeze_split|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "governance / asset-value / value-up theme proxy without tender floor, binding catalyst or capital-return execution bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["control_premium_proxy", "tender_or_transaction_floor_proxy", "governance_catalyst_proxy"], "stage3_evidence_fields": ["binding_terms", "buyer_quality", "acceptance_probability", "closing_path", "capital_return_execution"], "stage4b_evidence_fields": ["price_above_tender_floor", "governance_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_deal_break_or_tender_withdrawal_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003240/2024.csv", "profile_path": "atlas/symbol_profiles/003/003240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 636000, "MFE_30D_pct": 56.29, "MFE_90D_pct": 56.29, "MFE_180D_pct": 56.29, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.3, "MAE_90D_pct": -3.46, "MAE_180D_pct": -19.81, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 994000, "drawdown_after_peak_pct": -48.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "asset_value_governance_MFE_rejected_or_local_4B_watch_without_tender_floor_or_capital_return_bridge", "four_b_evidence_type": ["price_above_tender_floor_or_deal_cap", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_deal_break_or_tender_withdrawal", "trigger_outcome_label": "governance_theme_blowoff_high_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R11L84-C32-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L84-C32-03", "trigger_id": "R11L84-C32-03-S2FP-20240125", "symbol": "003240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"control_premium_specificity_score": 15, "tender_or_transaction_floor_score": 0, "binding_term_quality_score": 0, "buyer_or_competing_bid_quality_score": 5, "acceptance_or_closing_probability_score": 5, "capital_return_execution_score": 10, "governance_catalyst_score": 30, "relative_strength_score": 75, "valuation_blowoff_risk_score": 85, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"control_premium_specificity_score": 15, "tender_or_transaction_floor_score": 0, "binding_term_quality_score": 0, "buyer_or_competing_bid_quality_score": 5, "acceptance_or_closing_probability_score": 0, "capital_return_execution_score": 0, "governance_catalyst_score": 30, "relative_strength_score": 75, "valuation_blowoff_risk_score": 85, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Governance-theme RiskWatch", "changed_components": ["tender_or_transaction_floor_score", "binding_term_quality_score", "acceptance_or_closing_probability_score", "capital_return_execution_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C32 requires tender/transaction floor, binding terms, buyer or competing-bid quality, closing path and capital-return execution before clean Stage2/Green; asset-value theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 56.29, "MAE_90D_pct": -3.46, "score_return_alignment_label": "governance_theme_blowoff_high_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff"}
{"row_type": "shadow_weight", "axis": "C32_tender_transaction_floor_binding_terms_closing_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Governance/control-premium rerating requires tender/transaction floor, binding terms, buyer or competing-bid quality, closing path and capital-return execution; governance/asset-value theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 036560/001750 with tender-cap or deal-risk watch; demotes 003240 governance theme blowoff", "trigger_ids": "R11L84-C32-01-S2A-20240913|R11L84-C32-02-S2A-20240715|R11L84-C32-03-S2FP-20240125", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R11", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["governance_asset_value_theme_false_positive_high_MAE", "tender_transaction_floor_binding_terms_required", "local_4B_late_after_control_premium_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_deal_break_not_price_only"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C32, test a canonical-archetype guard requiring tender/transaction floor, binding terms, buyer/competing-bid quality, acceptance/closing path and capital-return execution before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 84
next_round = R12
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
