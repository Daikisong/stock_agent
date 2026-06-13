---
title: E2R Stock-Web v12 Residual Research — R12 C32 Governance / Control Premium / Tender Cap
selected_round: R12
selected_loop: 100
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: mixed_C32_tender_control_premium_affiliate_restructuring_quality_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; C32 static rows 94, use only new trigger families / price-validation holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
---

# E2R v12 residual research — R12 / C32 governance control premium tender cap

## 0. Execution compliance

This file follows the v12 research mode: standalone historical calibration Markdown, no live candidate scan, no broker/API use, no `stock_agent` code patch, and no production scoring change. `docs/core/V12_Research_No_Repeat_Index.md` was used only as the duplicate/coverage ledger. `Songdaiki/stock-web` was used as the price source.

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R12
selected_loop = 100
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = mixed_C32_tender_control_premium_affiliate_restructuring_quality_holdout
loop_objective = holdout_validation | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_false_positive_mining
```

## 1. Selection rationale

Static No-Repeat Index shows `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` as a Priority 2 area with 94 representative rows, so this loop is not a raw quantity fill. It is a quality holdout pass. The current conversation has already filled most Priority 0/1 under-covered axes session-adjusted; C32 had not yet received a dedicated new pass in this chain. Therefore this run targets new C32 trigger families: K-pop tender auction, hostile tender with competing issuer buyback, failed family tender, state-owned control sale preferred bidder, pharma family recapitalization, and affiliate restructuring/minority fairness.

Hard duplicate check used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row below is intended to count as a duplicate of prior C32 R12 loop 92/99 files; loop 100 uses fresh event dates or fresh symbol/failure-mode combinations for this session.

## 2. Stock-Web manifest / schema check

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
price_basis: tradable_raw
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
manifest_max_date: '2026-02-20'
MFE_N_pct: '(max high from entry_date through N tradable rows / entry_price - 1) * 100'
MAE_N_pct: '(min low from entry_date through N tradable rows / entry_price - 1) * 100'
corporate_action_block_rule: block if candidate date overlaps entry_date through D+180 window
```

Checked profile caveats for the six symbols. The relevant entry→180D windows do not overlap listed corporate-action candidate dates in the profiles used for this pass. HMM has a corporate-action candidate on `2023-11-10`, but the HMM trigger entry is `2023-12-18`, so the candidate is outside the tested forward window.

## 3. Case matrix

| symbol | name | trigger | role | entry | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | peak / drawdown | read |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| 041510 | 에스엠 | 2023-03-07 Stage4B | counterexample | 149700 | 7.68/-41.48 | 7.68/-41.48 | 7.68/-41.48 | 2023-03-08 161200 / -45.66% | Stage4B |
| 010130 | 고려아연 | 2024-09-13 Stage3-Green | positive_with_local_4B | 666000 | 131.68/-1.65 | 261.41/-1.65 | 261.41/-3.45 | 2024-12-06 2407000 / -73.29% | Stage3-Green_with_local_4B_after_peak |
| 000240 | 한국앤컴퍼니 | 2023-12-06 Stage4B | counterexample | 20750 | 14.46/-28.43 | 14.46/-28.43 | 14.46/-29.78 | 2023-12-07 23750 / -38.65% | Stage4B |
| 011200 | HMM | 2023-12-18 Stage2-Actionable | positive_with_guardrail | 17540 | 32.84/-9.92 | 32.84/-18.76 | 32.84/-18.76 | 2023-12-20 23300 / -38.84% | Stage2-Actionable_with_4B_watch |
| 008930 | 한미사이언스 | 2024-01-15 Stage4B | counterexample | 43300 | 29.79/-10.62 | 29.79/-28.41 | 29.79/-40.53 | 2024-01-16 56200 / -54.18% | Stage4B |
| 241560 | 두산밥캣 | 2024-07-12 Stage4B | counterexample | 54600 | 8.97/-38.92 | 8.97/-38.92 | 8.97/-38.92 | 2024-07-12 59500 / -43.95% | Stage4B |


## 4. Findings by mechanism

### 4.1 Cash tender price is a ceiling, not automatically Stage3 durability

`041510 에스엠` shows the cleanest failure mode. Kakao's tender price gave a firm cash-exit reference, but the entry at KRW 149,700 already sat almost exactly on the tender price. The 30/90/180D MFE was only `+7.68%`, while every window eventually printed `-41.48%` MAE. In C32 terms, a tender price near spot should cap upside unless there is an actual arbitrage capture, competing bid, or post-deal capital allocation thesis.

### 4.2 Hostile tender plus competing issuer/buyback can be a true C32 positive — but needs an exit guard

`010130 고려아연` is the opposite holdout. The MBK/Young Poong tender launched at a control-premium price, and the later competing buyback / counter-tender path created scarcity in the free float. The row printed `+261.41%` 180D MFE with only `-3.45%` MAE from entry to the full-window low. However, the post-peak drawdown was `-73.29%`. That means the positive C32 score is real, but local 4B should activate once tender spread becomes parabolic or the price trades far beyond cash offer economics.

### 4.3 Failed tender / preferred bidder / shareholder vote risk should stay below Stage3

`000240 한국앤컴퍼니`, `011200 HMM`, and `008930 한미사이언스` are three flavors of the same bridge gap:

- fixed tender without price raise or subscription success;
- preferred bidder without signed SPA/closing and unresolved seller conditions;
- share-acquisition recapitalization without shareholder vote and board-control clearance.

All three had non-price evidence, but the evidence did not become final control transfer. C32 should keep these as Stage2-Actionable or Stage4B watch until final cash exit, control transfer, or governance clearance is confirmed.

### 4.4 Affiliate restructuring is not a tender premium

`241560 두산밥캣` is a different C32 species. It was not an external buyer cash tender; it was an affiliate share-exchange restructuring with minority-shareholder fairness concerns. The price row had `+8.97%` 180D MFE but `-38.92%` MAE. In C32, affiliate restructuring needs a fairness-ratio/minority-acceptance gate, not a control-premium boost.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R12", "selected_loop": 100, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "KPOP_TENDER_OFFER_PREMIUM_CAP", "symbol": "041510", "company_name": "에스엠", "trigger_date": "2023-03-07", "entry_date": "2023-03-07", "entry_price": 149700.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_family": "governance_control_premium_tender_or_affiliate_restructuring", "event_summary": "Kakao and Kakao Entertainment tender offer for up to 35% of SM at KRW 150,000/share after HYBE tender failed.", "evidence_url": "https://en.yna.co.kr/view/AEN20230307003251320", "evidence_quality": "verified_url", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "profile_ref": "atlas/symbol_profiles/041/041510.json", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "current_profile_error": "tender_offer_price_anchor_can_overstate_stage3_durability", "expected_stage_after_shadow_rule": "Stage4B", "current_score_proxy": 78.0, "shadow_score_proxy": 66.0, "raw_component_score_breakdown": {"eps_fcf_explosion": 35, "earnings_visibility": 42, "bottleneck_pricing": 30, "market_mispricing": 70, "valuation_rerating": 76, "capital_allocation": 72, "information_confidence": 88}, "thesis_summary": "Firm tender price created a near-cash-exit anchor, but once the control auction resolved the premium decayed; C32 should cap Stage3 unless cash exit is actually captured or durable post-deal capital allocation is visible.", "entry_timing_note": "Kakao tender offer announced before/through market session; use trigger-date close from Stock-Web.", "MFE_30D_pct": 7.682, "MAE_30D_pct": -41.483, "peak_30D_date": "2023-03-08", "peak_30D_price": 161200.0, "trough_30D_date": "2023-03-28", "trough_30D_price": 87600.0, "MFE_90D_pct": 7.682, "MAE_90D_pct": -41.483, "peak_90D_date": "2023-03-08", "peak_90D_price": 161200.0, "trough_90D_date": "2023-03-28", "trough_90D_price": 87600.0, "MFE_180D_pct": 7.682, "MAE_180D_pct": -41.483, "peak_180D_date": "2023-03-08", "peak_180D_price": 161200.0, "trough_180D_date": "2023-03-28", "trough_180D_price": 87600.0, "peak_date": "2023-03-08", "peak_price": 161200.0, "post_peak_trough_date": "2023-03-28", "post_peak_trough_price": 87600.0, "drawdown_after_peak_pct": -45.6576, "forward_window_last_date": "2023-11-27"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R12", "selected_loop": 100, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_COMPETING_BUYBACK_CONTROL_BATTLE", "symbol": "010130", "company_name": "고려아연", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000.0, "trigger_type": "Stage3-Green", "case_role": "positive_with_local_4B", "evidence_family": "governance_control_premium_tender_or_affiliate_restructuring", "event_summary": "MBK Partners and Young Poong launched a tender offer for Korea Zinc; subsequent competing buyback/tender escalation created an extreme control-premium path.", "evidence_url": "https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/", "evidence_quality": "verified_url", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "profile_ref": "atlas/symbol_profiles/010/010130.json", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "current_profile_error": "stage3_positive_is_real_but_peak_after_tender_escalation_requires_local_4b_exit_guard", "expected_stage_after_shadow_rule": "Stage3-Green_with_local_4B_after_peak", "current_score_proxy": 91.0, "shadow_score_proxy": 84.0, "raw_component_score_breakdown": {"eps_fcf_explosion": 45, "earnings_visibility": 62, "bottleneck_pricing": 78, "market_mispricing": 86, "valuation_rerating": 92, "capital_allocation": 95, "information_confidence": 91}, "thesis_summary": "This is the clean C32 positive holdout: named tender, competing buyer/issuer action, and observable control scarcity generated large MFE. But post-peak collapse means the shadow rule should keep a local 4B guard after tender spread goes parabolic.", "entry_timing_note": "MBK/Young Poong tender launch date; use same-day Stock-Web close.", "MFE_30D_pct": 131.6817, "MAE_30D_pct": -1.6517, "peak_30D_date": "2024-10-29", "peak_30D_price": 1543000.0, "trough_30D_date": "2024-09-13", "trough_30D_price": 655000.0, "MFE_90D_pct": 261.4114, "MAE_90D_pct": -1.6517, "peak_90D_date": "2024-12-06", "peak_90D_price": 2407000.0, "trough_90D_date": "2024-09-13", "trough_90D_price": 655000.0, "MFE_180D_pct": 261.4114, "MAE_180D_pct": -3.4535, "peak_180D_date": "2024-12-06", "peak_180D_price": 2407000.0, "trough_180D_date": "2025-04-09", "trough_180D_price": 643000.0, "peak_date": "2024-12-06", "peak_price": 2407000.0, "post_peak_trough_date": "2025-04-09", "post_peak_trough_price": 643000.0, "drawdown_after_peak_pct": -73.2862, "forward_window_last_date": "2025-06-18"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R12", "selected_loop": 100, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "FAILED_FAMILY_CONTROL_TENDER_PREMIUM", "symbol": "000240", "company_name": "한국앤컴퍼니", "trigger_date": "2023-12-06", "entry_date": "2023-12-06", "entry_price": 20750.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_family": "governance_control_premium_tender_or_affiliate_restructuring", "event_summary": "MBK tender offer for Hankook & Company amid family control dispute; offer price was fixed and later failed to secure enough subscriptions.", "evidence_url": "https://www.koreatimes.co.kr/business/banking-finance/20231211/mbk-partners-rules-out-possibility-of-raising-price-of-tender-offer-for-hankook-company", "evidence_quality": "verified_url", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "profile_ref": "atlas/symbol_profiles/000/000240.json", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "current_profile_error": "fixed_tender_without_price_raise_or_subscription_success_should_not_be_stage3", "expected_stage_after_shadow_rule": "Stage4B", "current_score_proxy": 74.0, "shadow_score_proxy": 61.0, "raw_component_score_breakdown": {"eps_fcf_explosion": 38, "earnings_visibility": 50, "bottleneck_pricing": 35, "market_mispricing": 68, "valuation_rerating": 76, "capital_allocation": 78, "information_confidence": 70}, "thesis_summary": "A fixed tender price below trading price turned the control story into an event premium ceiling. The failed tender shows C32 needs subscription-success/price-raise/final-control-transfer gates.", "entry_timing_note": "Use first full trading day after MBK public tender became visible; close from Stock-Web.", "MFE_30D_pct": 14.4578, "MAE_30D_pct": -28.4337, "peak_30D_date": "2023-12-07", "peak_30D_price": 23750.0, "trough_30D_date": "2024-01-17", "trough_30D_price": 14850.0, "MFE_90D_pct": 14.4578, "MAE_90D_pct": -28.4337, "peak_90D_date": "2023-12-07", "peak_90D_price": 23750.0, "trough_90D_date": "2024-01-17", "trough_90D_price": 14850.0, "MFE_180D_pct": 14.4578, "MAE_180D_pct": -29.7831, "peak_180D_date": "2023-12-07", "peak_180D_price": 23750.0, "trough_180D_date": "2024-08-07", "trough_180D_price": 14570.0, "peak_date": "2023-12-07", "peak_price": 23750.0, "post_peak_trough_date": "2024-08-07", "post_peak_trough_price": 14570.0, "drawdown_after_peak_pct": -38.6526, "forward_window_last_date": "2024-08-29"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R12", "selected_loop": 100, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PREFERRED_BIDDER_CONTROL_TRANSFER_UNCLOSED", "symbol": "011200", "company_name": "HMM", "trigger_date": "2023-12-18", "entry_date": "2023-12-18", "entry_price": 17540.0, "trigger_type": "Stage2-Actionable", "case_role": "positive_with_guardrail", "evidence_family": "governance_control_premium_tender_or_affiliate_restructuring", "event_summary": "Harim-led consortium was selected as preferred bidder for the HMM sale; later negotiations broke down and the acquisition did not close.", "evidence_url": "https://en.yna.co.kr/view/AEN20231218009052320", "evidence_quality": "verified_url", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "profile_ref": "atlas/symbol_profiles/011/011200.json", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "current_profile_error": "preferred_bidder_status_gives_stage2_mfe_but_stage3_requires_spa_closing_and_perpetual_bond_resolution", "expected_stage_after_shadow_rule": "Stage2-Actionable_with_4B_watch", "current_score_proxy": 77.0, "shadow_score_proxy": 68.0, "raw_component_score_breakdown": {"eps_fcf_explosion": 55, "earnings_visibility": 48, "bottleneck_pricing": 42, "market_mispricing": 72, "valuation_rerating": 80, "capital_allocation": 70, "information_confidence": 74}, "thesis_summary": "Preferred-bidder status gave a tradable MFE burst, but unresolved SPA terms, perpetual bond conversion and seller conditions kept the case below Stage3 durability.", "entry_timing_note": "Harim/Pan Ocean-JKL preferred bidder announcement; same-day close from Stock-Web.", "MFE_30D_pct": 32.8392, "MAE_30D_pct": -9.9202, "peak_30D_date": "2023-12-20", "peak_30D_price": 23300.0, "trough_30D_date": "2023-12-18", "trough_30D_price": 15800.0, "MFE_90D_pct": 32.8392, "MAE_90D_pct": -18.7571, "peak_90D_date": "2023-12-20", "peak_90D_price": 23300.0, "trough_90D_date": "2024-04-19", "trough_90D_price": 14250.0, "MFE_180D_pct": 32.8392, "MAE_180D_pct": -18.7571, "peak_180D_date": "2023-12-20", "peak_180D_price": 23300.0, "trough_180D_date": "2024-04-19", "trough_180D_price": 14250.0, "peak_date": "2023-12-20", "peak_price": 23300.0, "post_peak_trough_date": "2024-04-19", "post_peak_trough_price": 14250.0, "drawdown_after_peak_pct": -38.8412, "forward_window_last_date": "2024-09-10"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R12", "selected_loop": 100, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "FAMILY_CONTROL_RECAPITALIZATION_SHAREHOLDER_VOTE_RISK", "symbol": "008930", "company_name": "한미사이언스", "trigger_date": "2024-01-15", "entry_date": "2024-01-15", "entry_price": 43300.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_family": "governance_control_premium_tender_or_affiliate_restructuring", "event_summary": "OCI Holdings approved acquisition of a 27.03% Hanmi Science stake via old/new shares; shareholder vote later halted the integration plan.", "evidence_url": "https://web-static.oci-holdings.co.kr/ir/2024/01/15/982debb5-fcb6-400f-8d79-1cd0bda627e6.pdf", "evidence_quality": "verified_url", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "profile_ref": "atlas/symbol_profiles/008/008930.json", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "current_profile_error": "control_recapitalization_without_vote_clearance_or_board_settlement_should_route_to_4b", "expected_stage_after_shadow_rule": "Stage4B", "current_score_proxy": 79.0, "shadow_score_proxy": 63.0, "raw_component_score_breakdown": {"eps_fcf_explosion": 40, "earnings_visibility": 44, "bottleneck_pricing": 30, "market_mispricing": 74, "valuation_rerating": 82, "capital_allocation": 86, "information_confidence": 76}, "thesis_summary": "The transaction created an immediate governance premium, but the trigger had explicit shareholder-vote/control-dispute risk. It later broke at the vote, validating a C32 vote-clearance gate.", "entry_timing_note": "OCI Holdings investor deck was dated Jan. 15 after Jan. 12 board approval; use Jan. 15 close.", "MFE_30D_pct": 29.7921, "MAE_30D_pct": -10.6236, "peak_30D_date": "2024-01-16", "peak_30D_price": 56200.0, "trough_30D_date": "2024-01-31", "trough_30D_price": 38700.0, "MFE_90D_pct": 29.7921, "MAE_90D_pct": -28.4065, "peak_90D_date": "2024-01-16", "peak_90D_price": 56200.0, "trough_90D_date": "2024-05-24", "trough_90D_price": 31000.0, "MFE_180D_pct": 29.7921, "MAE_180D_pct": -40.5312, "peak_180D_date": "2024-01-16", "peak_180D_price": 56200.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 25750.0, "peak_date": "2024-01-16", "peak_price": 56200.0, "post_peak_trough_date": "2024-08-05", "post_peak_trough_price": 25750.0, "drawdown_after_peak_pct": -54.1815, "forward_window_last_date": "2024-10-11"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "selected_round": "R12", "selected_loop": 100, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "AFFILIATE_RESTRUCTURING_MINORUITY_SHAREHOLDER_VALUE_TRANSFER", "symbol": "241560", "company_name": "두산밥캣", "trigger_date": "2024-07-12", "entry_date": "2024-07-12", "entry_price": 54600.0, "trigger_type": "Stage4B", "case_role": "counterexample", "evidence_family": "governance_control_premium_tender_or_affiliate_restructuring", "event_summary": "Doosan Bobcat / Doosan Robotics comprehensive share exchange drew minority-shareholder and regulator pushback; the proposed share exchange was later withdrawn.", "evidence_url": "https://www.doosanbobcat.com/kr/investment/irData/irDataFile/view/271", "evidence_quality": "verified_url", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "profile_ref": "atlas/symbol_profiles/241/241560.json", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated": false, "insufficient_forward_window": false, "current_profile_error": "affiliate_restructuring_synergy_headline_without_fair_ratio_or_minority_acceptance_should_not_be_stage3", "expected_stage_after_shadow_rule": "Stage4B", "current_score_proxy": 73.0, "shadow_score_proxy": 58.0, "raw_component_score_breakdown": {"eps_fcf_explosion": 48, "earnings_visibility": 64, "bottleneck_pricing": 45, "market_mispricing": 66, "valuation_rerating": 62, "capital_allocation": 42, "information_confidence": 78}, "thesis_summary": "This is not a tender cash-exit; it is a stock-swap governance event. Minority-shareholder fairness concerns made the trigger a C32 4B rather than a positive rerating.", "entry_timing_note": "Comprehensive share exchange was announced July 11; use next tradable close after announcement.", "MFE_30D_pct": 8.9744, "MAE_30D_pct": -38.9194, "peak_30D_date": "2024-07-12", "peak_30D_price": 59500.0, "trough_30D_date": "2024-08-05", "trough_30D_price": 33350.0, "MFE_90D_pct": 8.9744, "MAE_90D_pct": -38.9194, "peak_90D_date": "2024-07-12", "peak_90D_price": 59500.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 33350.0, "MFE_180D_pct": 8.9744, "MAE_180D_pct": -38.9194, "peak_180D_date": "2024-07-12", "peak_180D_price": 59500.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 33350.0, "peak_date": "2024-07-12", "peak_price": 59500.0, "post_peak_trough_date": "2024-08-05", "post_peak_trough_price": 33350.0, "drawdown_after_peak_pct": -43.9496, "forward_window_last_date": "2025-04-10"}
```

## 6. Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "symbol": "041510", "entry_date": "2023-03-07", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "current_profile_stage_proxy": "Stage4B", "current_score_proxy": 78.0, "shadow_rule_stage_proxy": "Stage4B", "shadow_score_proxy": 66.0, "main_penalty_or_gate": "C32 cash-exit/final-control-transfer/minority-fairness gate", "score_delta_after_shadow_rule": -12.0}
{"row_type": "score_simulation", "symbol": "010130", "entry_date": "2024-09-13", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "current_profile_stage_proxy": "Stage3-Green", "current_score_proxy": 91.0, "shadow_rule_stage_proxy": "Stage3-Green_with_local_4B_after_peak", "shadow_score_proxy": 84.0, "main_penalty_or_gate": "C32 cash-exit/final-control-transfer/minority-fairness gate", "score_delta_after_shadow_rule": -7.0}
{"row_type": "score_simulation", "symbol": "000240", "entry_date": "2023-12-06", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "current_profile_stage_proxy": "Stage4B", "current_score_proxy": 74.0, "shadow_rule_stage_proxy": "Stage4B", "shadow_score_proxy": 61.0, "main_penalty_or_gate": "C32 cash-exit/final-control-transfer/minority-fairness gate", "score_delta_after_shadow_rule": -13.0}
{"row_type": "score_simulation", "symbol": "011200", "entry_date": "2023-12-18", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "current_profile_stage_proxy": "Stage2-Actionable", "current_score_proxy": 77.0, "shadow_rule_stage_proxy": "Stage2-Actionable_with_4B_watch", "shadow_score_proxy": 68.0, "main_penalty_or_gate": "C32 cash-exit/final-control-transfer/minority-fairness gate", "score_delta_after_shadow_rule": -9.0}
{"row_type": "score_simulation", "symbol": "008930", "entry_date": "2024-01-15", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "current_profile_stage_proxy": "Stage4B", "current_score_proxy": 79.0, "shadow_rule_stage_proxy": "Stage4B", "shadow_score_proxy": 63.0, "main_penalty_or_gate": "C32 cash-exit/final-control-transfer/minority-fairness gate", "score_delta_after_shadow_rule": -16.0}
{"row_type": "score_simulation", "symbol": "241560", "entry_date": "2024-07-12", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "current_profile_stage_proxy": "Stage4B", "current_score_proxy": 73.0, "shadow_rule_stage_proxy": "Stage4B", "shadow_score_proxy": 58.0, "main_penalty_or_gate": "C32 cash-exit/final-control-transfer/minority-fairness gate", "score_delta_after_shadow_rule": -15.0}
```

## 7. Aggregate JSON

```json
{
  "row_type": "aggregate",
  "selected_round": "R12",
  "selected_loop": 100,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "trigger_row_count": 6,
  "calibration_usable_rows": 6,
  "representative_rows": 6,
  "positive_case_count": 2,
  "counterexample_count": 4,
  "local_4B_watch_count": 6,
  "rows_with_MFE180_ge_20pct": 3,
  "rows_with_MAE180_le_minus_20pct": 4,
  "avg_MFE_180D_pct": 59.1928,
  "avg_MAE_180D_pct": -28.8212,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0,
  "current_profile_error_count": 5,
  "proposed_rule_candidate": "C32_CONTROL_PREMIUM_TENDER_REQUIRES_CASH_EXIT_FINAL_CONTROL_TRANSFER_OR_FAIR_RATIO_CLEARANCE_WITH_4B_CAP"
}
```

## 8. Shadow rule candidate

```text
C32_CONTROL_PREMIUM_TENDER_REQUIRES_CASH_EXIT_FINAL_CONTROL_TRANSFER_OR_FAIR_RATIO_CLEARANCE_WITH_4B_CAP
```

Rule compression:

```yaml
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
new_axis_proposed: C32_CONTROL_PREMIUM_TENDER_REQUIRES_CASH_EXIT_FINAL_CONTROL_TRANSFER_OR_FAIR_RATIO_CLEARANCE_WITH_4B_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
rule_logic:
  Stage3_Green_allowed_if:
    - firm cash tender or buyback price materially above entry
    - tender acceptance/subscription path or competing bid escalation is visible
    - final control transfer, treasury cancellation, or durable capital-return mechanism is plausible
    - legal/shareholder injunction risk is low or already cleared
  Stage2_Actionable_allowed_if:
    - named bidder or formal tender exists
    - but SPA/closing/shareholder vote/regulatory clearance remains unresolved
  Stage4B_required_if_any:
    - tender price is fixed and spot trades above or near it
    - subscription success is uncertain
    - family control dispute is unresolved
    - affiliate restructuring has minority-fairness objections
    - price trades far beyond cash tender economics
  Stage4C_required_if:
    - tender/merger/share exchange is formally withdrawn or blocked
    - control transfer fails and no replacement buyer exists
```

## 9. Residual contribution summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
residual_error_found: true
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
positive_case_count: 2
counterexample_count: 4
local_4B_watch_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
current_profile_error_count: 5
avg_MFE_180D_pct: 59.1928
avg_MAE_180D_pct: -28.8212
rows_with_MFE180_ge_20pct: 3
rows_with_MAE180_le_minus_20pct: 4
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation/coding agent. Do not treat this research file as a live trading signal. Ingest this Markdown only as v12 historical calibration evidence. Parse the trigger JSONL rows, validate all required price fields, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and compare against existing C32 rows. If accepted, consider a shadow rule candidate named C32_CONTROL_PREMIUM_TENDER_REQUIRES_CASH_EXIT_FINAL_CONTROL_TRANSFER_OR_FAIR_RATIO_CLEARANCE_WITH_4B_CAP. Apply only as a narrow C32-scoped candidate. Do not alter global stage thresholds from this single file.
```

## 11. Final research state

```yaml
completed_round: R12
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; C32 static rows 94
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_holdout_only_if_new_cash_exit_or_minorities_fairness_path
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER_quality_holdout_if_new_channel_reorder_path
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 12. Batch Ingest Self-Audit

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
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
