# Round-134 R2 Loop-8 Score -> Stage -> Price Alignment

Round 134 uses the R2 v8 score table to test whether AI/semiconductor evidence produced the right stage and whether that stage matched the observed price path in the source note.

## R2 v8 Base Score Weights

| component | points | direction | reason |
| --- | ---: | --- | --- |
| `eps_fcf_revision` | 25 | up | SK Hynix, Applied Materials, and Broadcom show price paths follow OP/EPS/FCF evidence. |
| `customer_shipment_revenue_visibility` | 22 | up | Customer names, shipments, AI orders, and guidance create Stage 2 signal. |
| `bottleneck_pricing_power` | 19 | hold_up | HBM, NAND, TSMC capacity, optical PCB, and photonics bottlenecks still matter. |
| `market_mispricing_gap` | 10 | cap_after_recognition | The old memory/cyclical or generic server frame must still be wrong, but SK Hynix/Kioxia-like rerating quickly reduces the gap. |
| `valuation_room_4b_runway` | 8 | cap_after_rerating | SK Hynix, Kioxia, and IPO cases show good structures can already be 4B. |
| `capital_discipline_fcf_stability` | 8 | up | CoreWeave, Cerebras, and Ecolab-CoolIT make FCF, debt, circular financing, and M&A price central. |
| `information_confidence_disclosure_detail` | 8 | up | Supermicro and list-only AI disclosures require accounting, customer, amount, period, and parser confidence checks. |

## Stage Caps

| stage | cap | required evidence | examples | Green policy |
| --- | --- | --- | --- | --- |
| Stage 1 | 45 | ai_hbm_custom_asic_cxl_glass_theme|narrative_without_customer_contract_shipment_revenue | cxl_glass_substrate_theme_case|furiosa_ai_related_stock_case | Green blocked until customer, shipment, revenue, or guidance evidence exists. |
| Stage 2 | 70 | customer_name|shipment|contract|revenue_guidance|ai_order_or_deal_amount | samsung_hbm4_shipping_case|tower_photonics_ai_datacenter_deal_case|cisco_ai_networking_orders_case | Green blocked until OP/EPS/FCF, margin, and price-path alignment confirm. |
| Stage 3 | 100 | op_eps_fcf_revision|margin_or_capital_return|price_path_alignment|cross_evidence | sk_hynix_record_profit_buyback_case|applied_materials_ai_packaging_growth_case|broadcom_custom_ai_asic_100b_case | Green possible only before 4B saturation and without RedTeam hard gates. |
| Stage 4B | monitoring | large_rerating|valuation_saturation|crowded_ai_consensus|price_outruns_new_evidence | sk_hynix_hbm_trillion_case|kioxia_ai_nand_profit_case|cerebras_ai_accelerator_ipo_case | A correct AI structure can become a monitoring case when price has already rerated heavily. |
| Stage 4C | hard_gate | auditor_resignation|filing_delay|circular_financing|fcf_negative_high_debt|labor_or_production_disruption | supermicro_ey_resignation_case|coreweave_nvidia_circular_financing_case|samsung_labor_strike_execution_case | Hard RedTeam overrides AI growth narratives. |

## Alignment Cases

| case_id | detected_stage | price_path_status | verdict | normalization_adjustment |
| --- | --- | --- | --- | --- |
| `sk_hynix_hbm_trillion_case` | Stage 3 -> 4B-watch | Q4 reaction and multi-year rerating are cited in round note; full OHLCV backfill still required | score_to_stage_to_price_aligned_but_4b | raise HBM EPS/FCF and bottleneck credit, but cut valuation room after large rerating |
| `samsung_hbm4_shipping_case` | Stage 2 | HBM4 shipment price reaction aligned with Stage 2, not Stage 3 | stage2_detection_aligned | raise catch-up visibility but require qualification, yield, volume shipment, and EPS conversion |
| `applied_materials_ai_packaging_growth_case` | Stage 2 -> Stage 3 candidate | Guidance beats and price reactions support equipment Stage 2/3 calibration | stage_detection_price_aligned | raise equipment EPS/visibility while preserving order-pushout and export-control overlays |
| `broadcom_custom_ai_asic_100b_case` | Stage 2 -> Stage 3 candidate | AI revenue guide and supply bottleneck evidence aligned with price reaction | custom_asic_independent_archetype_confirmed | promote custom ASIC as its own axis; keep margin, customer, startup-credit, and capacity risks |
| `cisco_ai_networking_orders_case` | Stage 2 -> Stage 3 candidate | AI infrastructure and switching orders aligned with price reaction | networking_stage_detection_aligned | raise AI networking visibility, but require margin, FCF, and repeat order conversion |
| `tower_photonics_ai_datacenter_deal_case` | Stage 2 | Photonic AI data-center deal amount supported Stage 2 price reaction | photonics_stage2_aligned | raise photonics deal visibility, but require delivery, revenue recognition, and margin before Green |
| `foxconn_ai_server_rack_growth_case` | Stage 2 | AI server revenue/profit evidence works, but ODM margin power remains capped | revenue_aligned_margin_capped | keep server ODM revenue credit while lowering bottleneck/pricing score |
| `kioxia_ai_nand_profit_case` | Stage 3 -> 4B-watch | Profit guidance validates AI storage NAND, but 20x stock move is 4B-heavy | structure_aligned_valuation_crowded | raise NAND EPS evidence and sharply reduce valuation/mispricing after large price path |
| `supermicro_ey_resignation_case` | Stage 4C | Auditor resignation matched severe negative price reaction in round note | redteam_hard_gate_aligned | strengthen accounting trust hard gate across AI server and adjacent names |
| `coreweave_nvidia_circular_financing_case` | Stage 2 visibility + 4B/4C-watch | Contract visibility is not clean demand when supplier/customer/investor loops exist | green_block_correct | lower capital/FCF score and require clean FCF, leverage, utilization, and customer diversification |
| `cerebras_ai_accelerator_ipo_case` | IPO event premium / 4B-watch | First-day surge and next-day decline fit event-premium rather than structural Green | valuation_watch_aligned | cap pure-play accelerator valuation until repeat orders, margin, ecosystem, and FCF appear |
| `ecolab_coolit_liquid_cooling_case` | Stage 2 M&A + valuation watch | AI cooling deal still had negative price reaction due to M&A multiple/accretion delay | mna_redteam_aligned | penalize M&A overpay, debt financing, and delayed EPS accretion |

## Interpretation

- HBM and AI storage can be structurally right while already requiring 4B-watch after a large rerating.
- HBM catch-up, photonics, networking, and equipment can reach Stage 2 when customer, shipment, order, or guidance evidence exists.
- AI server ODM, neocloud, and AI accelerator IPO cases need capital, margin, accounting, and customer-concentration checks before any Green discussion.
- Simple example: `Samsung HBM4 shipped` can be Stage 2; it is not Stage 3-Green until qualification, yield, volume shipment, and EPS conversion are verified.
