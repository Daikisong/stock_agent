# Round-207 R3 Loop-8 Stage 4B / 4C Review

## 4B Watch Triggers

- `battery_supply_chain_lithium_event_group_rally`
- `ess_lfp_contract_announcement_rally_without_delivery_margin`
- `battery_materials_valuation_expansion_without_calloff`
- `ipo_or_vertical_integration_price_ahead_of_evidence`
- `ampc_included_earnings_surprise_only`

## Hard 4C Gates

- `contract_cancellation`
- `contract_value_collapse`
- `customer_ev_model_cancellation`
- `customer_strategy_pullback`
- `take_or_pay_absence_confirmed`
- `gwh_calloff_failure`
- `utilization_delay`
- `negative_fcf`
- `debt_burden_or_emergency_management`
- `subsidy_quality_profit_collapse`
- `share_issuance_or_dilution_under_weak_demand`

## R3 Loop-8 Interpretation

- ESS/LFP contract rally는 delivery·utilization·OPM·FCF 전까지 4B-watch도 함께 본다.
- 계약 취소와 계약가치 붕괴는 R3에서 가장 강한 4C gate다.
- 리튬 가격 이벤트와 IPO/전구체 narrative는 Green이 아니라 event premium 또는 overheat로 분리한다.
- AMPC 포함 이익은 보조금 제외 이익 품질을 확인하기 전까지 confidence cap을 둔다.

## Case Review

| case | 4B status | hard 4C confirmed | interpretation |
| --- | --- | --- | --- |
| `r3_loop8_lges_ess_pivot_contract_break` | `none` | true | ESS LFP contract is Stage 2; Ford/Freudenberg cancellations and AMPC-dependent profit create 4C-watch/hard 4C evidence. |
| `r3_loop8_lnf_tesla_contract_collapse` | `watch` | true | Tesla contract value collapse is a hard 4C benchmark. Customer name and contract value headline are not enough for Green. |
| `r3_loop8_samsung_sdi_ess_lfp_stage2` | `watch` | false | ESS contract is Stage 2; EV demand weakness and capital raise pressure block Stage 3-Green until operating proof appears. |
| `r3_loop8_sk_innovation_skon_failed_rerating` | `watch` | true | SK On loss/debt burden makes SK Innovation a restructuring relief case, not an EV battery Green case. |
| `r3_loop8_skiet_separator_demand_break` | `watch` | false | Separator demand broke with EV weakness and SK On financial stress; essential material status alone is not E2R visibility. |
| `r3_loop8_posco_future_m_lithium_event` | `watch` | false | Lithium price shock can move the stock, but commodity/event sensitivity is not structural Stage 3 evidence. |
| `r3_loop8_ecopro_materials_precursor_overheat` | `watch` | false | IPO/precursor/vertical integration story is insufficient without external customers, utilization, OPM, and FCF. |
