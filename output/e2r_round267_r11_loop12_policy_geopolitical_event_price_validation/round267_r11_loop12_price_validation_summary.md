# Round 267 R11 Loop 12 Policy Geopolitical Disaster Event Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_267.md
- analyst_round_id: round_195
- analyst_large_sector: POLICY_GEOPOLITICAL_DISASTER_EVENT
- canonical_large_sector: POLICY_GEOPOLITICAL_EVENT
- cases: 8
- success_candidate: 2
- event_premium: 2
- overheat: 1
- failed_rerating: 2
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- 4C-watch cases: 3
- hard_4c_case_count: 1
- policy_relief_count: 3
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r11_loop12_samsung_strike_systemic_policy_4c_watch | Samsung Electronics strike / systemic chip policy risk | failed_rerating | 4c_watch_systemic_labor_policy_risk |  |  |  | 2026-05-15 | false | thesis_break_watch | Samsung strike risk is company operational risk that can become national export and AI supply-chain policy gate. |
| r11_loop12_middle_east_iran_energy_macro_hard_4c | Middle East / Iran geopolitical energy shock | 4c_thesis_break | macro_hard_4c | 2026-03-31 |  |  | 2026-03-04 | true | thesis_break | Confirmed R11 hard 4C: energy chokepoint shock hit index, FX, autos, airlines and chips simultaneously. |
| r11_loop12_energy_saving_oil_budget_policy_relief | Energy-saving campaign and oil-price supplementary budget | success_candidate | success_candidate_policy_relief | 2026-03-31 |  |  |  | false | success_candidate_policy_relief | Energy and fiscal response is relief; company Green requires margin and FCF bridge. |
| r11_loop12_kospi_7000_ai_capital_confidence_4b | KOSPI 7,000 AI capital-market confidence event | event_premium | event_premium_plus_4b_watch | 2026-05-06 |  | 2026-05-06 |  | false | event_premium_4B_watch | Index confidence is Stage 2; sidecar-level rally and chip concentration require 4B-watch. |
| r11_loop12_ai_fiscal_room_policy_relief | AI boom fiscal room / tax-windfall policy relief | success_candidate | success_candidate_policy_relief | 2026-05-13 |  |  |  | false | success_candidate_policy_relief | Fiscal room is macro relief, not company Green, until EPS/FCF bridge exists. |
| r11_loop12_stablecoin_fx_policy_overheat | Stablecoin policy overheat / FX gate | overheat | overheat_plus_4c_watch |  |  | 2025-06-01 | 2025-06-18 | false | price_moved_without_evidence | Stablecoin-related stocks moved 2~3x before regulated revenue; FX outflow risk remains 4C-watch. |
| r11_loop12_rare_earth_critical_minerals_policy_overlay | Rare-earth end-use restriction and critical-minerals policy relief | failed_rerating | 4c_watch_plus_policy_relief | 2026-02-05 |  |  | 2025-04-22 | false | thesis_break_watch_plus_policy_relief | Supply-chain restriction is 4C-watch; policy relief is not Green without actual supply contracts. |
| r11_loop12_hyundai_saemangeum_regional_capex_event | Hyundai Saemangeum AI/hydrogen regional CAPEX | event_premium | event_premium_success_candidate | 2026-02-25 |  | 2026-02-25 |  | false | event_premium_success_candidate | Regional CAPEX headline moved Hyundai/Kia before ROI, utilization or FCF bridge. |

## Interpretation
- Middle East / Iran energy shock is the confirmed hard 4C reference for this pack.
- Samsung strike, stablecoin FX, and rare-earth restriction are 4C-watch overlays, not positive Green evidence.
- Energy-saving, AI fiscal room, and critical-minerals policies are relief until company EPS/FCF bridges are visible.
- KOSPI 7,000 and Hyundai Saemangeum are event-premium examples: price moved before company evidence fully closed.
- Easy example: `10T won CAPEX headline + stock +10%` is 4B-watch; `CAPEX + customer contract + utilization + FCF` is the bundle required before deeper Stage review.
