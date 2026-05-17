# Round-133 R1 Loop-8 Score -> Stage -> Price Alignment

## Base Score Weights

| component | points | direction | reason |
| --- | ---: | --- | --- |
| `eps_fcf_revision` | 25 | up | Stage 3 promotion depends on order/backlog becoming OP/EPS/FCF. |
| `contract_backlog_visibility` | 22 | hold_but_detail_required | Contract amount, period, counterparty, delivery, backlog, PPA, and slot reservation define Stage 2. |
| `bottleneck_pricing_power` | 18 | hold_with_price_path_check | Transformer lead time, turbine slot, grid bottleneck, and defense capacity matter only if they support margin. |
| `market_mispricing_gap` | 10 | cap_after_consensus | Old industrial frame must still be wrong, but crowded AI power or defense consensus lowers room. |
| `valuation_room_4b_runway` | 7 | cap_after_rerating | GE Vernova-style rerating needs explicit 4B watch after the market recognizes the power-equipment theme. |
| `capital_discipline_fcf_conversion` | 10 | up | FCF-funded buyback/dividend adds quality; dilution, FSS correction, and unclear CAPEX become hard RedTeam. |
| `information_confidence_disclosure_detail` | 8 | up | OpenDART list-only, MoU-only, PPA without approval, or missing detail caps Stage 3. |

## Stage Caps

| stage band | max score | evidence | examples | Green policy |
| --- | --- | --- | --- | --- |
| `Stage 1` | 45 | industry_news, policy_news, mou_or_moa, macro_shortage_without_company_contract, demand_narrative_without_cashflow | us_transformer_shortage_import_slots_case, hd_hyundai_huntington_us_navy_aux_case, oklo_smr_no_revenue_watch_case, ukraine_reconstruction_policy_case | Green blocked until company-level contract/backlog detail appears. |
| `Stage 2` | 70 | contract_amount, customer, period_or_delivery_schedule, backlog_or_guidance, ppa_or_slot_reservation_with_gate_status | ls_electric_525kv_us_datacenter_transformer_case, hyundai_rotem_morocco_rail_case, constellation_tmi_microsoft_restart_case | Green blocked until OP/EPS/FCF, margin, and price path confirm. |
| `Stage 3` | 100 | op_eps_fcf_revision, margin_or_fcf_conversion, price_path_alignment, cross_evidence | ge_vernova_data_center_orders_case, siemens_energy_fcf_buyback_case | Green possible only if not already saturated 4B and no hard RedTeam. |
| `Stage 4B` | monitoring | large_rerating, crowded_consensus, valuation_room_reduced, revision_slowdown_watch | ge_vernova_data_center_orders_case, siemens_energy_fcf_buyback_case | A good structure can be downgraded to watch when the new frame is widely priced. |
| `Stage 4C` | hard_gate | dilution, fss_correction_request, contract_cancel_or_delay, low_margin, permitting_or_policy_break, profit_miss, accounting_or_disclosure_shock | hanwha_aerospace_dilution_trim_case, siemens_orders_profit_miss_case, oklo_smr_no_revenue_watch_case, perth_data_center_withdrawal_case | Hard RedTeam overrides high order/backlog score. |

## Alignment Cases

| case | detected stage | price-path status | verdict | adjustment |
| --- | --- | --- | --- | --- |
| `ge_vernova_data_center_orders_case` | Stage 2 -> Stage 3 / 4B-watch | event-day price reaction confirmed in round note; longer MFE/MAE still needs official OHLCV backfill | score_to_stage_to_price_aligned | keep EPS/FCF, visibility, and bottleneck weights high; reduce valuation room through 4B watch |
| `siemens_energy_fcf_buyback_case` | Stage 3 candidate / 4B-watch | FCF and buyback evidence strong; price path requires OHLCV backfill | partially_confirmed | raise capital/FCF conversion weight but require price validation before Green |
| `ls_electric_525kv_us_datacenter_transformer_case` | Stage 2 | contract detail strong; price path requires backfill | stage2_not_green_yet | raise EHV visibility; keep EPS/FCF cap until margin and revisions appear |
| `hyundai_rotem_morocco_rail_case` | Stage 2 | large contract visible; price path and margin require backfill | stage2_not_green_yet | rail remains capped before margin, warranty, financing, FX, and OP/EPS evidence |
| `constellation_tmi_microsoft_restart_case` | Stage 2 | Q1 beat and Microsoft PPA context exist, but the round note recorded a negative price reaction and open FERC/grid-rights gates | stage2_with_approval_gate | existing nuclear PPA/restart stays capped until FERC/PJM grid rights, restart CAPEX, and guidance conversion are verified |
| `hanwha_aerospace_dilution_trim_case` | Stage 2 structure + 4C-watch | capital raise shock matched negative price-path warning in round note | redteam_alignment_confirmed | strengthen capital discipline penalty and stage_after_redteam downgrade |
| `hd_hyundai_huntington_us_navy_aux_case` | Stage 1~2 option | MoU/MoA only; any price move is event premium until contract economics appear | green_block_correct | strengthen MoU/MoA score cap and require vessel count, contract value, schedule, margin, and yard CAPEX |
| `siemens_orders_profit_miss_case` | Stage 2 capped / 4C-watch | orders and backlog looked strong, but sales and industrial profit miss matched the negative price reaction | orders_only_false_positive_contained | orders-only evidence is capped when profit/margin conversion is missing or negative |
| `oklo_smr_no_revenue_watch_case` | Stage 1~2 watch | regulatory progress did not offset no revenue, wider loss, and delayed commercialization in the round note | pre_revenue_smr_green_block_correct | SMR policy/news is capped before revenue, signed customer economics, financing, and commercial operation visibility |

## Interpretation

- GE Vernova is the cleanest Loop-8 example where score, stage, and short-term price reaction align, but it also turns on 4B-watch.
- LS Electric and Hyundai Rotem are Stage 2 examples: the contract evidence is strong, but Green waits for margin, OP/EPS/FCF, and official price-path backfill.
- Hanwha Aerospace shows why capital discipline is now a larger R1 weight: good defense backlog can be downgraded by dilution shock.
- HD Hyundai-Huntington remains event/watch while it is MoU/MoA-only.
