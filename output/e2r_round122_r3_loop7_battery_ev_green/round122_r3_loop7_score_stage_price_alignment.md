# Round-122 R3 Loop-7 Score / Stage / Price Alignment

Round 122 checks whether the score table's stage interpretation matches the observed operating and price path.
This is calibration material only; it does not change production scoring.

| case | score-stage view | price-path signal | verdict | normalization adjustment |
| --- | --- | --- | --- | --- |
| `tesla_lges_megapack3_lansing_case` | Stage 2 | LGES +0.6% around contract confirmation | visibility confirmed but not Stage 3 | give contract detail credit; keep EPS/FCF, utilization, and ESS OPM cap |
| `sk_on_flatiron_ess_7_2gwh_case` | Stage 2 | contract value undisclosed; price backfill needed | Stage 2 cap is appropriate | strengthen contract_value_missing and margin_unverified penalty |
| `ford_energy_storage_pivot_case` | EV-to-ESS Stage 2 | Ford +20% over two days and +6.7% on event day | EV-to-ESS pivot price path is confirmed | raise EV_TO_ESS watch weight, but do not generalize to battery suppliers without direct contracts |
| `redwood_recycling_energy_storage_case` | structural reference | private company; public price validation unavailable | archetype reference only | require direct listed-company exposure before scoring public equities |
| `quantumscape_vw_solid_state_license_case` | Stage 2 + 4B-watch | premarket +40% | event premium confirmed; Green not confirmed | keep solid-state license cap until mass production, royalty revenue, yield, and cost are visible |
| `ford_lges_ev_contract_cancel_case` | Stage 4C | LGES intraday drawdown up to -7.6% | RedTeam gate aligned with price path | strengthen contract_cancellation and expected_revenue_loss gate |
| `lges_freudenberg_contract_cancel_case` | Stage 4C | expected revenue loss after Ford and Freudenberg cancellations around KRW 13.5T | 4C reinforced | make expected_revenue_loss an explicit field |
| `gm_lg_ultium_ohio_idle_case` | Stage 4C | operating status downgraded; restart uncertain | EV CAPA false Green | strengthen plant_idle and utilization penalty; treat Tennessee ESS conversion separately as Watch |
| `qcells_customs_detention_furlough_case` | Stage 4C | 1,000-worker furlough from stalled shipments | solar supply-chain risk confirmed | strengthen UFLPA/customs/FEOC gate |
| `orsted_sunrise_wind_impairment_case` | Stage 4C | maximum price-path loss around -18% | project economics RedTeam aligned | strengthen financing_cost, foundation_cost, delay, and impairment fields |
| `moss_landing_bess_fire_case` | 4C-watch | sector safety/permitting gate | BESS demand needs safety cap | raise BESS safety, permitting, insurance, and local-opposition gate |
| `battery_soh_transparency_case` | 4C-watch | not a direct price event | second-life valuation cap | require independent SOH and residual-capacity validation |

## Loop-7 Takeaway

- Stage 2 visibility and Stage 3 operating confirmation are intentionally separated.
- Raise ESS contract visibility and EV-to-ESS redeployment Watch credit when customer, GWh, contract period, production date, and use case are explicit.
- Keep Stage 3 capped until revenue recognition, ESS OPM, utilization, FCF, EPS revision, and price path confirm the operating transition.
- Strengthen 4C gates for contract cancellation, expected revenue loss, idle plant, customs/UFLPA, project impairment, BESS fire, and SOH opacity.
- Do not treat EV CAPA growth, policy manufacturing narrative, wind PPA, or solid-state license as Green by name alone.
