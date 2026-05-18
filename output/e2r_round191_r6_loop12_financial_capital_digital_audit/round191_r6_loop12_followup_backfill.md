# Round-191 R6 Loop-12 Follow-up Backfill Plan

Round191 confirms that the schema exists. The next step is evidence backfill, not production score changes.

## Required Backfill Groups

- Insurance NAV: `nav_discount`, `major_equity_stake_value`, `k_ics_ratio`, `csm`, `roe`, `dividend_per_share`.
- Shareholder return: `buyback_amount`, `cancelled_share_amount`, `total_shareholder_return_ratio`, `eps_accretion_from_buyback`.
- Digital asset bank option: `digital_asset_stake_value`, `equity_method_income`, `regulatory_approval_pending`, `exchange_security_incident_flag`.
- Stablecoin theme: `stablecoin_issuance_volume`, `reserve_income`, `take_rate`, `stablecoin_regulatory_status`.
- Biometric payment: `merchant_count`, `user_count`, `transaction_volume`, `biometric_data_risk_flag`.
- Financial cycle / policy risk: `relative_strength_vs_financial_basket`, `credit_cost`, `pf_exposure`, `tax_policy_shock_flag`.

## What Not To Change

- Do not lower Stage 3-Green thresholds to improve recall.
- Do not treat low-PBR, value-up, stablecoin, Dunamu, FacePay, or buyback headlines as structural evidence by themselves.
- Do not use Round190/Round191 case records as candidate-generation input.
- Do not invent missing ROE, capital-ratio, take-rate, issuance, security, or stage-price fields.
