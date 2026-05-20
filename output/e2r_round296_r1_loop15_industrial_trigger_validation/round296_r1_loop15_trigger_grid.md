# Round 296 Trigger Grid

Trigger-level validation separates candidate quality from full OHLC completion. For example, a reported +9.3% event move can support Stage2-Actionable while full 90D/180D MFE is still marked missing.

| trigger | case | company | type | date | evidence | event return | relative | promote_to |
|---|---|---|---|---|---|---|---|---|
| r1l15_hyundai_rotem_T2 | r1_loop15_hyundai_rotem_k2_poland | Hyundai Rotem | Stage2-Actionable | 2024-04-09 | 18 K2 shipments to Poland, Q1 OP estimate +85% YoY, consensus beat, 270B won export revenue contribution | 9.3 | 9.6 | Stage3-Yellow |
| r1l15_lig_nex1_T2 | r1_loop15_lig_nex1_msam | LIG Nex1 | 4B-watch | 2024-07-02 | 1H share gain 69%, KOSPI 5.4%, downgrade to Hold | -11 |  | 4B_trim |
| r1l15_lig_nex1_T3 | r1_loop15_lig_nex1_msam | LIG Nex1 | Stage2-Actionable | 2024-09-20 | Iraq 3.71T won / $2.8B Cheongung-II order after Saudi $3.2B order | 3.6 | 2.7 | Stage2-Actionable |
| r1l15_hanwha_aero_T1 | r1_loop15_hanwha_aerospace_k9_backlog_dilution | Hanwha Aerospace | Stage2-Actionable | 2024-07-09 | Romania $1B K9/K10 order, backlog 5.1T to 30T won | 5 |  | Stage3-Yellow |
| r1l15_hanwha_aero_T4 | r1_loop15_hanwha_aerospace_k9_backlog_dilution | Hanwha Aerospace | 4B-watch | 2025-03-21 | 3.6T won share sale, 605,000 won issue price, 16% discount, YTD more than doubled | -13 |  | 4B |
| r1l15_shipbuilding_T1 | r1_loop15_shipbuilding_order_price_basket | Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy / HD Hyundai Mipo | Stage2-Actionable | 2024-03-14 | global shipbuilding orders +18% YoY, Korea 50% share, newbuilding price index up, 3-year backlog | Samsung Heavy +16 / Hanwha Ocean +13 / HD HHI +11 | 15.5/12.5/10.5 | Stage3-Yellow_candidate |
| r1l15_ls_electric_T2 | r1_loop15_ls_electric_us_grid | LS Electric | Stage2-Actionable_candidate | 2024-07-01 | U.S. revenue share forecast 20%, revenue forecast raised 4-22%, target raised 87% | -5.4 |  | pending_full_ohlc |
| r1l15_samsung_ena_T2 | r1_loop15_samsung_ena_fadhili | Samsung E&A | Stage3-Yellow_candidate | 2024-04-03 | $6B Fadhili order, +60% gas capacity, target upside 30.8%, event relative +9.9pp | 8.5 | 9.9 | Stage3-Yellow |
| r1l15_czech_nuclear_T1 | r1_loop15_czech_nuclear_doosan | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E | Stage2-Actionable_with_legal_watch | 2024-07-17 | KHNP preferred bidder, two reactors, first large overseas nuclear order since 2009, related names already +14 to +48 over 3 months | Doosan +48 3M / KEPCO E&C +41 3M / KEPCO Plant +14 3M |  | Stage2-Actionable_only |
