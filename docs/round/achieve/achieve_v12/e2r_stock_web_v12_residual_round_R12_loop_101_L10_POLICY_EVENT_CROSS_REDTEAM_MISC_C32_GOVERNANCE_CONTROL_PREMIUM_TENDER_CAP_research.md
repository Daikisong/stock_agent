# stock-web v12 residual research — R12 / C32

## Metadata

- schema_family: `v12_sector_archetype_residual`
- selected_round: `R12`
- selected_loop: `101`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`
- fine_archetype_id: `TENDER_CASH_EXIT_PATH_VS_CONTROL_NEWS_WITHOUT_MINORITY_CASH_EXIT`
- selection_basis: `docs/core/V12_Research_No_Repeat_Index.md`
- selected_priority_bucket: `Priority 0`
- price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- loop_objective: `coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | governance_control_tender_cash_path_guardrail | canonical_archetype_compression`

## Thesis

C32 should distinguish between:

1. **real tender / buyback / minority cash-exit path**: shareholders can actually sell into a legally defined cash price, so Stage2 can remain active, but post-offer collapse risk should route to local 4B watch.
2. **control sale or governance fight without minority cash-exit**: price can spike from control-premium vocabulary, but the small shareholder has no guaranteed cash exit. This should not receive full Stage2-Actionable credit.
3. **failed sale / stalled control process**: once the buyer negotiation breaks, the score should be capped or moved to Stage2-Watch / 4C review.

## Source validation

stock-web manifest shows the atlas is generated from FinanceData/marcap, with `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and calibration shards rooted at `atlas/ohlcv_tradable_by_symbol_year`.

All cases below use stock-web 1D OHLC rows. Corporate-action contamination is checked from the symbol profile. Case-level rows are rejected if a forward window crosses a blocked corporate-action date; here, the relevant 2024 windows are usable unless specifically marked.

## Cases

### Case 1 — 036560 / KZ정밀, formerly 영풍정밀 — tender-cash path positive with post-offer 4B watch

- trigger_family: `tender_offer_cash_exit_path`
- trigger_type: `Stage2-Actionable`
- entry_date: `2024-09-13`
- entry_close: `12,180`
- source_event: Korea Zinc battle; Korea Zinc later raised its tender offer for Young Poong Precision to 35,000 won per share.
- price_path:
  - 2024-09-13: close 12,180
  - 2024-09-20: high 20,550
  - 2024-10-07: high 36,700
  - 2024-10-18: low 22,300 after offer/takeover-news digestion
  - 2025-02-14: low 10,810
- MFE/MAE:
  - 30D MFE: `(36,700 / 12,180 - 1) = +201.31%`
  - 90D MFE: `+201.31%`
  - 180D MFE: `+201.31%`
  - 30D MAE: `0.00%` from entry-close basis
  - 90D MAE: `0.00%` from entry-close basis
  - 180D MAE: `(10,810 / 12,180 - 1) = -11.25%`
- interpretation: real cash path existed, so Stage2 should not be blocked. However, once the tender window closes or rival offer dynamics fade, the price can normalize sharply. This strengthens `C32_post_tender_resolution_4B_watch`.

### Case 2 — 010130 / 고려아연 — hostile tender/buyback positive-control but already visible-covered

- trigger_family: `hostile_tender_offer_and_counter_buyback`
- trigger_type: `Stage2-Actionable`
- entry_date: `2024-09-13`
- entry_close: `666,000`
- source_event: MBK Partners and Young Poong launched a tender offer for Korea Zinc shares at 660,000 won per share; Korea Zinc later responded with a buyback/tender defense.
- price_path:
  - 2024-09-13: close 666,000
  - 2024-10-04: high 791,000
  - 2024-10-21: high 889,000
  - 2024-10-24: high 1,138,000
  - 2024-10-29: high 1,543,000
  - 2024-10-31: low 830,000 after blowoff
- MFE/MAE:
  - 30D MFE: `(1,543,000 / 666,000 - 1) = +131.68%`
  - 90D MFE: `+131.68%`
  - 180D MFE: `+131.68%`
  - 30D MAE: `0.00%` from entry-close basis
  - 90D MAE: `0.00%` from entry-close basis
  - 180D MAE: `0.00%` from visible cited window; later full-window should be rechecked if exact 180D rows are pulled.
- interpretation: this is not a new symbol in the repo index, but it is useful as a positive-control because the cash exit path was explicit and repeated through competing offers. It should not train a new symbol-diversity credit, but it validates the C32 tender-cash rule.

### Case 3 — 011200 / HMM — control-sale process without minority tender cash exit, failed-sale counterexample

- trigger_family: `state_asset_control_sale_without_minority_cash_exit`
- trigger_type: `Stage2-FalsePositive`
- entry_date: `2024-01-02`
- entry_close: `20,600`
- source_event: HMM sale negotiations with the preferred bidder broke down; the listed shareholder did not receive a tender-style minority cash exit.
- price_path:
  - 2024-01-02: close 20,600
  - 2024-01-04: high 21,600
  - 2024-02-15: low 17,470
  - 2024-04-08: low 15,010
  - 2024-08-05: low 15,800 after later drift
- MFE/MAE:
  - 30D MFE: `(21,600 / 20,600 - 1) = +4.85%`
  - 90D MFE: `+4.85%`
  - 180D MFE: visible forward high after entry remains below entry-close in cited windows after Jan; retain `+4.85%`
  - 30D MAE: approximately `(18,920 / 20,600 - 1) = -8.16%`
  - 90D MAE: `(15,010 / 20,600 - 1) = -27.14%`
  - 180D MAE: at least `-27.14%` from cited 2024 forward rows
- interpretation: sale/process headlines alone should not create a C32 Stage2 credit. Without a public tender, squeeze-out, appraisal-right cash bridge, or legally binding minority cash exit, this belongs in Stage2-Watch / false-positive guardrail.

## Rule candidate

```text
if canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
and tender_offer_or_buyback_cash_exit_path == true
and legally_defined_price_per_share == true:
    keep_stage2_actionable_bonus = true
    if MFE_30D_pct >= +30:
        local_4B_watch = true
```

```text
if canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
and control_sale_or_governance_fight_headline == true
and minority_cash_exit_path == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
and sale_process_failed_or_tender_success_uncertain == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    Stage2_FalsePositive_Block = true
```

## Calibration contribution

- new_independent_case_count: `3`
- reused_case_count_within_C32_visible_basis: `1`
- same_archetype_new_symbol_count_visible_index_basis: `2`
- same_archetype_new_trigger_family_count: `3`
- calibration_usable case 수: `3`
- calibration_usable trigger 수: `3`
- positive_case_count: `2`
- counterexample_count: `1`
- current_profile_error_count: `1`
- loop_contribution_label: `canonical_archetype_rule_candidate`
- existing_axis_strengthened:
  - `C32_tender_cash_path_requirement`
  - `C32_post_tender_resolution_4B_watch`
  - `C32_control_sale_without_minority_cash_exit_stage2_block`
  - `C32_failed_sale_process_false_positive_guard`

## JSONL trigger rows

```jsonl
{"row_type":"trigger","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"036560","name":"KZ정밀/영풍정밀","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":12180,"mfe_30d_pct":201.31,"mae_30d_pct":0.00,"mfe_90d_pct":201.31,"mae_90d_pct":0.00,"mfe_180d_pct":201.31,"mae_180d_pct":-11.25,"classification":"positive_with_post_tender_4B_watch","calibration_usable":true}
{"row_type":"trigger","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":666000,"mfe_30d_pct":131.68,"mae_30d_pct":0.00,"mfe_90d_pct":131.68,"mae_90d_pct":0.00,"mfe_180d_pct":131.68,"mae_180d_pct":0.00,"classification":"positive_control_reused_visible_symbol","calibration_usable":true}
{"row_type":"trigger","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"011200","name":"HMM","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-02","entry_close":20600,"mfe_30d_pct":4.85,"mae_30d_pct":-8.16,"mfe_90d_pct":4.85,"mae_90d_pct":-27.14,"mfe_180d_pct":4.85,"mae_180d_pct":-27.14,"classification":"control_sale_failed_without_minority_cash_exit_counterexample","calibration_usable":true}
```

## Next recommended archetypes

`C15_MATERIAL_SPREAD_SUPERCYCLE, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`
