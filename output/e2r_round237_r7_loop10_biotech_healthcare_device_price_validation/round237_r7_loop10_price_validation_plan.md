# Round 237 R7 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- hard_4c_confirmed: false
- Do not invent OHLC, peak, MFE, MAE, stage prices, prescription volume, utilization, margin, FCF, or royalty values.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- relative_underperformance_pp
- transaction_value_or_facility_capacity
- launch_price_or_discount
- trial_size_or_exam_count
- approval_launch_validation_date
- commercialization_gate_status
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r7_loop10_jeisys_aesthetic_device_take_private | WSJ reported acquisition, price, and financial anchors | Deal value about $742M; FY2023 revenue $107M; adjusted pretax earnings $31M | reported_price_anchor_not_full_ohlc |
| r7_loop10_hugel_letybo_us_launch | Allure/New York Post product launch and price anchors | Letybo estimated $9-12/unit vs Botox $12-18/unit; potential 25-33.3% discount | price_data_unavailable_after_deep_search |
| r7_loop10_sk_bioscience_idt_cmo_mna | Reuters acquisition and event-return anchors | Shares +11.7% in morning trade after IDT Biologika acquisition announcement | reported_event_anchor_not_full_ohlc |
| r7_loop10_celltrion_us_manufacturing_tariff_hedge | Reuters transaction and investment anchors | ImClone acquisition $330M; expansion up to 700B KRW / $478.17M | price_data_unavailable_after_deep_search |
| r7_loop10_samsung_biologics_gsk_facility_price_failed | Reuters reported event return and facility capacity anchor | relative underperformance -2.4pp on GSK facility acquisition event | reported_event_anchor_not_full_ohlc |
| r7_loop10_hanall_immunovant_batoclimab_ted_failure | Reuters partner trial-failure anchor | Immunovant -4.8% after batoclimab failed two late-stage thyroid eye disease trials | hanall_stock_price_data_unavailable_after_deep_search |
| r7_loop10_lunit_medical_ai_external_validation | arXiv external validation evidence | AUC 0.91 overall; precision 0.08; weaker subgroup AUCs require commercialization gate | price_data_unavailable_after_deep_search |
