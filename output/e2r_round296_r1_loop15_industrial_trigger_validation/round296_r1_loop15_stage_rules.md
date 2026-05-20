# Round 296 Stage2-Actionable / Stage3-Yellow Rules

Do not apply these weights to production scoring yet.

## Stage2-Actionable Promotion Rules

- shipment_delivery_calloff_or_revenue_contribution_confirmed
- op_estimate_or_revenue_forecast_beats_consensus_by_20pct_plus
- market_relative_strength_on_evidence_day_5pp_plus
- backlog_duration_or_repeat_order_visibility_confirmed
- asp_price_index_or_target_revision_confirmed
- binding_order_or_delivery_evidence_not_mou_or_preferred_bidder_only

## Stage3-Yellow Rules

- real_order_contract_shipment_or_approval_confirmed
- op_eps_or_revenue_contribution_quantified
- trigger_day_relative_strength_is_strong
- margin_cash_collection_final_delivery_or_legal_clearance_still_pending

## Green Blockers

- full_trigger_level_ohlc_missing
- delivery_margin_unconfirmed
- cash_collection_unconfirmed
- working_capital_or_claim_risk_unresolved
- final_contract_or_legal_clearance_pending
- 4b_overlay_requires_sizing_down_rule

## Easy Examples

- `preferred bidder` is Stage2 at most until final contract and legal clearance.
- `$6B EPC order` can be Yellow when price reacts strongly, but Green waits for completion margin and cash collection.
- `target +87%` with same-day -5.4% is not rejected; it needs full-window retest.
