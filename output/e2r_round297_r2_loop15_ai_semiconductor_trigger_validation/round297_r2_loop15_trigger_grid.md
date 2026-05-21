# Round 297 Trigger Grid

Trigger-level validation separates evidence timing from full OHLC completion. For example, `HBM3E mass production + +9% event move` can support Stage3-Yellow while 90D/180D MFE is still missing.

| trigger | case | company | type | date | evidence | event return | relative | promote_to |
|---|---|---|---|---|---|---|---|---|
| r2l15_skhynix_T0 | r2_loop15_sk_hynix_hbm_first_mover | SK Hynix | Stage2-Actionable | 2024-03-26 | AI/HBM rally, Daiwa EPS forecast +41%, HBM3E contribution, SK Hynix +4.3% vs KOSPI +0.7% | 4.3 | 3.6 | Stage2-Actionable |
| r2l15_skhynix_T1 | r2_loop15_sk_hynix_hbm_first_mover | SK Hynix | Stage2-Actionable | 2024-06-26 | HSBC 2Q OP estimate +12% to 5.2T won, HBM share 38% of DRAM revenue by end-2025, target 280,000 |  |  | Stage3-Yellow_candidate |
| r2l15_skhynix_T2 | r2_loop15_sk_hynix_hbm_first_mover | SK Hynix | Stage3-Yellow | 2024-09-26 | 12-layer HBM3E mass production, 50% capacity increase, supply to customers by year-end | 9 | 7.3 | Stage3-Yellow |
| r2l15_hanmi_T1 | r2_loop15_hanmi_semiconductor_hbm_equipment | Hanmi Semiconductor | Stage2-Actionable | 2024-03-26 | SK Hynix HBM packaging equipment, KRW21.48B supply deal, recent wins KRW200B | 16 | 15.3 | Stage2-Actionable |
| r2l15_samsung_T2 | r2_loop15_samsung_electronics_hbm_catchup_labor_watch | Samsung Electronics | Stage2-Actionable | 2025-10-02 | OpenAI partnership, AI data center memory demand, Samsung +4.7%, SK Hynix +12% | 4.7 | relative_to_SK_Hynix_-7.3pp | Stage2-Actionable_only |
| r2l15_skhynix_openai_T1 | r2_loop15_sk_hynix_openai_asml_4b | SK Hynix | Stage3-Green+4B-watch | 2025-10-02 | OpenAI Stargate partnership, Samsung +4.7%, SK Hynix +12%, KOSPI +3% | 12 | 9 | Stage3-Green+4B |
| r2l15_export_control_T1 | r2_loop15_memory_china_equipment_export_control | Samsung / SK Hynix / Hanmi / Hana Micron | 4C-watch | 2025-09-01 | U.S. revoked authorizations for China fab equipment; Samsung -2.6%, SK Hynix -5% | Samsung -2.6 / SK Hynix -5.0 |  | 4C-watch |
| r2l15_lginnotek_T1 | r2_loop15_lg_innotek_apple_ai_upgrade | LG Innotek | Stage2-Actionable | 2024-06-12 | Apple/OpenAI AI iPhone upgrade cycle, LG Innotek +19%, OP growth forecast +33% | 19 | 18.6 | Stage2-Actionable |
| r2l15_lgdisplay_T1 | r2_loop15_lg_display_apple_oled_recovery | LG Display | Stage2 | 2024-07-25 | Q2 loss 94B vs expected 308B, revenue +42%, Apple OLED orders, but no 2H profit guidance |  |  | Stage2_only |
| r2l15_samsung_labor_T2 | r2_loop15_samsung_labor_supply_chain_4c | Samsung Electronics | 4C-watch | 2026-05-19 | 48,000 workers, 18-day strike risk, DRAM supply impact 3-4%, NAND 2-3% |  |  | 4C-watch |
