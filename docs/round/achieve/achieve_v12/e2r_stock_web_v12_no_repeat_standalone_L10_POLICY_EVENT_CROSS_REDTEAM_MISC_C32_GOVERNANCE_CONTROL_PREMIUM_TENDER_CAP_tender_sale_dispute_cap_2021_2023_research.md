# E2R V12 No-Repeat Standalone Residual Research
## R13 / L10 / C32 — Governance control-premium tender-cap guard

metadata:
```text
selected_round: R13
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: TENDER_OFFER_CONTROL_SALE_DISPUTE_CAP_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_tender_sale_dispute_cap_2021_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP current coverage:
rows=64, symbols=10, date range=2020-11-16~2024-12-06, good/bad S2=22/13, 4B/4C=12/4
top covered symbols: 010130(18), 041510(14), 000240(5), 고려아연(5), 에스엠(4)
```

This run avoids those top-covered C32 symbols and adds 048260, 003920, and 009240.  
Each row uses a new `C32 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
048260 오스템임플란트: inactive/delisted-like; 2023 forward row available; corporate-action candidate is 2023-08-03, after the tender-cap test window used here.
003920 남양유업: 2021 forward window clean; corporate-action candidate is 2024-11-20.
009240 한샘: corporate_action_candidate_count=0.
```

## 3. Research thesis

C32 should not treat every control-premium headline as a rerating. It should classify the legal and cash mechanics of the event:

```text
governance / sale / tender attention
→ is there an enforceable tender or only a loose control-premium headline?
→ is there buyer funding, closing certainty, and legal enforceability?
→ is there a minority-holder exit floor?
→ if not, price premium should route to local 4B or counterexample, not Green
```

The useful distinction is between a real floor and a painted floor. A tender offer is a floor with bolts. A headline sale premium without closing certainty is a floor drawn on paper.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C32_048260_OSSTEM_20230125_TENDER_OFFER_PRICE_CAP_SUCCESS | 048260 | tender_cap_success | 2023-01-25 | 186300 | 190200 on 2023-04-12 | 175100 on 2023-02-24 | 1.4% | 2.09% | 2.09% | -6.01% | -1.95% |
| C32_003920_NAMYANG_20210528_CONTROL_SALE_DISPUTE_FALSE_GREEN | 003920 | control_sale_dispute_counterexample | 2021-05-28 | 570000 | 813000 on 2021-07-01 | 382000 on 2021-10-12 | 42.63% | 42.63% | 42.63% | -32.98% | -53.01% |
| C32_009240_HANSSEM_20210714_STRATEGIC_SALE_PRICE_PREMIUM_FALSE_GREEN | 009240 | strategic_sale_premium_counterexample | 2021-07-14 | 146500 | 149000 on 2021-07-14 | 69500 on 2022-01-27 | 1.71% | 1.71% | 1.71% | -52.56% | -53.36% |

## 5. Stage evidence split

### Stage2 / Stage3
- Governance and control-premium headlines are valid routing signals, not automatic positives.
- Stage3/Green requires closing certainty, enforceable terms, buyer funding, minority-holder treatment, and governance transition clarity.

### 4B
- 048260 is the clean tender-cap success: after the offer price became the anchor, upside behaved like a capped spread, not a new open-ended rerating.
- 003920 and 009240 show local 4B risk. The market capitalized sale headlines faster than it could verify closing certainty.

### 4C
- 003920 is the legal-dispute / deal-closing counterexample.
- 009240 is the no-tender-floor counterexample: a strategic sale headline may affect control value without giving minority holders a hard takeout floor.
- In both cases, once the deal mechanics fail to harden, the control premium evaporates like steam from a kettle.

## 6. Raw component score breakdown

```json
{
  "C32_003920_NAMYANG_20210528_CONTROL_SALE_DISPUTE_FALSE_GREEN": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 2,
    "eps_fcf_explosion": 2,
    "information_confidence": 3,
    "market_mispricing": 10,
    "total": 27,
    "valuation_rerating_runway": 3,
    "visibility_quality": 4
  },
  "C32_009240_HANSSEM_20210714_STRATEGIC_SALE_PRICE_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 3,
    "eps_fcf_explosion": 3,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C32_048260_OSSTEM_20230125_TENDER_OFFER_PRICE_CAP_SUCCESS": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 4,
    "eps_fcf_explosion": 2,
    "information_confidence": 5,
    "market_mispricing": 9,
    "total": 38,
    "valuation_rerating_runway": 2,
    "visibility_quality": 13
  }
}
```

## 7. Current calibrated profile stress test

Suggested C32 guard:
```text
if formal_tender_offer and tender_price_visible and delisting_or_takeout_path_clear:
    route_to_tender_cap = true
    block_fresh_green = true

if control_sale_headline and no closing_certainty_or_legal_enforceability:
    cap_stage = Stage3-Yellow
    route_to_local_4B_or_counterexample = true

if strategic_sale_premium and no minority_holder_tender_floor:
    block_stage3_green = true
    require_fundamental_or_cashflow_bridge_for_any_green = true
```

Residual errors:
```text
current_profile_error_count = 2
- 003920 / 2021-05-28: control-sale premium can be over-promoted if legal enforceability and closing certainty are not required.
- 009240 / 2021-07-14: strategic sale premium can be over-promoted if the model treats control value as minority-holder takeout value.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.01, "MAE_30D_pct": -6.01, "MAE_90D_pct": -6.01, "MFE_180D_pct": 2.09, "MFE_30D_pct": 1.4, "MFE_90D_pct": 2.09, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_048260_OSSTEM_20230125_TENDER_OFFER_PRICE_CAP_SUCCESS", "case_role": "tender_cap_success", "company_name": "오스템임플란트", "corporate_action_window_status": "clean_forward_window_or_event_specific_delisting_caveat", "current_profile_error": false, "current_profile_verdict": "Tender-cap logic worked: once the tender price and delisting path were visible, upside was capped near the offer price rather than a fresh Green rerating.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -1.95, "entry_date": "2023-01-25", "entry_price": 186300, "evidence_family": "private_equity_tender_offer_price_cap_and_delisting_path", "evidence_url_pending": false, "fine_archetype_id": "TENDER_OFFER_CONTROL_SALE_DISPUTE_CAP_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2023-02-24", "low_price_180d": 175100, "peak_date": "2023-04-12", "peak_price": 190200, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/048/048260.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 4, "eps_fcf_explosion": 2, "information_confidence": 5, "market_mispricing": 9, "total": 38, "valuation_rerating_runway": 2, "visibility_quality": 13}, "reuse_reason": null, "same_entry_group_id": "C32_048260_OSSTEM_20230125_TENDER_OFFER_PRICE_CAP_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["governance_or_control_event_attention", "sale_or_tender_price_reference", "minority_holder_exit_or_control_premium_claim"], "stage3_evidence_fields": ["closing_certainty_required", "legal_enforceability_or_buyer_funding_required", "minority_takeout_or_tender_floor_required"], "stage4b_evidence_fields": ["control_premium_price_run", "tender_price_cap_or_deal_premium_exhaustion", "post_peak_drawdown"], "stage4c_evidence_fields": ["deal_break_or_legal_dispute", "no_public_tender_floor", "governance_transition_failure"], "symbol": "048260", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/048/048260/2023.csv", "trigger_date": "2023-01-25", "trigger_type": "Tender-Cap", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.98, "MAE_30D_pct": -5.26, "MAE_90D_pct": -8.07, "MFE_180D_pct": 42.63, "MFE_30D_pct": 42.63, "MFE_90D_pct": 42.63, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_003920_NAMYANG_20210528_CONTROL_SALE_DISPUTE_FALSE_GREEN", "case_role": "control_sale_dispute_counterexample", "company_name": "남양유업", "corporate_action_window_status": "clean_forward_window_or_event_specific_delisting_caveat", "current_profile_error": true, "current_profile_verdict": "Control-sale premium should remain Yellow/4B-watch unless closing certainty, buyer funding, legal enforceability, and governance transition are confirmed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.01, "entry_date": "2021-05-28", "entry_price": 570000, "evidence_family": "control_sale_premium_without_closing_certainty_legal_dispute", "evidence_url_pending": false, "fine_archetype_id": "TENDER_OFFER_CONTROL_SALE_DISPUTE_CAP_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2021-10-12", "low_price_180d": 382000, "peak_date": "2021-07-01", "peak_price": 813000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003920.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 2, "eps_fcf_explosion": 2, "information_confidence": 3, "market_mispricing": 10, "total": 27, "valuation_rerating_runway": 3, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C32_003920_NAMYANG_20210528_CONTROL_SALE_DISPUTE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["governance_or_control_event_attention", "sale_or_tender_price_reference", "minority_holder_exit_or_control_premium_claim"], "stage3_evidence_fields": ["closing_certainty_required", "legal_enforceability_or_buyer_funding_required", "minority_takeout_or_tender_floor_required"], "stage4b_evidence_fields": ["control_premium_price_run", "tender_price_cap_or_deal_premium_exhaustion", "post_peak_drawdown"], "stage4c_evidence_fields": ["deal_break_or_legal_dispute", "no_public_tender_floor", "governance_transition_failure"], "symbol": "003920", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv", "trigger_date": "2021-05-28", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -52.56, "MAE_30D_pct": -27.99, "MAE_90D_pct": -27.99, "MFE_180D_pct": 1.71, "MFE_30D_pct": 1.71, "MFE_90D_pct": 1.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_009240_HANSSEM_20210714_STRATEGIC_SALE_PRICE_PREMIUM_FALSE_GREEN", "case_role": "strategic_sale_premium_counterexample", "company_name": "한샘", "corporate_action_window_status": "clean_forward_window_or_event_specific_delisting_caveat", "current_profile_error": true, "current_profile_verdict": "Strategic sale headline premium should not become Green when there is no public tender floor, no minority holder takeout certainty, and fundamentals are weakening.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.36, "entry_date": "2021-07-14", "entry_price": 146500, "evidence_family": "strategic_sale_event_premium_without_fundamental_or_tender_floor", "evidence_url_pending": false, "fine_archetype_id": "TENDER_OFFER_CONTROL_SALE_DISPUTE_CAP_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-01-27", "low_price_180d": 69500, "peak_date": "2021-07-14", "peak_price": 149000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009240.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 3, "eps_fcf_explosion": 3, "information_confidence": 3, "market_mispricing": 6, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C32_009240_HANSSEM_20210714_STRATEGIC_SALE_PRICE_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["governance_or_control_event_attention", "sale_or_tender_price_reference", "minority_holder_exit_or_control_premium_claim"], "stage3_evidence_fields": ["closing_certainty_required", "legal_enforceability_or_buyer_funding_required", "minority_takeout_or_tender_floor_required"], "stage4b_evidence_fields": ["control_premium_price_run", "tender_price_cap_or_deal_premium_exhaustion", "post_peak_drawdown"], "stage4c_evidence_fields": ["deal_break_or_legal_dispute", "no_public_tender_floor", "governance_transition_failure"], "symbol": "009240", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv", "trigger_date": "2021-07-14", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TENDER_OFFER_CONTROL_SALE_DISPUTE_CAP_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "governance_tender_cap_and_control_sale_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R13",
  "shadow_rule_candidate": "C32 governance/control-premium rows should distinguish hard tender-cap paths from loose sale-headline premiums; Green is blocked unless closing certainty, legal enforceability, buyer funding, minority takeout or tender floor, and governance transition are confirmed.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C32 + symbol + trigger_type + entry_date.
3. Add C32-specific tender-cap / sale-closing / minority-floor guard only as a shadow candidate until more rows exist.

Candidate rule:
- C32_TENDER_OFFER_PRICE_CAP_BLOCKS_FRESH_GREEN
- C32_CONTROL_SALE_PREMIUM_REQUIRES_CLOSING_CERTAINTY
- C32_STRATEGIC_SALE_WITHOUT_MINORity_TENDER_FLOOR_STAGE3_CAP
- C32_DEAL_DISPUTE_OR_LEGAL_ENFORCEABILITY_GAP_4C_WATCH

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

