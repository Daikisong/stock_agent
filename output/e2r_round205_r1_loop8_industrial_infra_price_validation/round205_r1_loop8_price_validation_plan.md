# Round-205 R1 Loop-8 Price Validation Plan

## Required Fields

- `price_data_source`
- `full_ohlc_available`
- `reported_price_anchor`
- `reported_return_anchor`
- `stage2_price`
- `stage3_price`
- `stage4b_price`
- `stage4c_price`
- `peak_price`
- `reported_mfe_minimum_pct`
- `mfe_1d`
- `mfe_1d_secondary`
- `mae_1d`
- `price_validation_status`

## Case Anchors

| case | price data source | reported anchor | status |
| --- | --- | --- | --- |
| `r1_loop8_hyundai_rotem_k2_aligned` | WSJ/FT reported price and return anchors | FT reported more than sixfold one-year subperiod | `reported_price_anchor_not_full_ohlc` |
| `r1_loop8_hanwha_aerospace_mfe_4b` | reported market price path anchor | reported MFE +665.3%; one-day MAE -13% | `reported_price_anchor_not_full_ohlc` |
| `r1_loop8_lig_nex1_cheongung_watch` | reported event and war-period return anchors | +3.6% one day; +47% war-period | `reported_return_anchor_not_full_ohlc` |
| `r1_loop8_kai_fa50_stage2` | reported one-year return anchor | reported MFE about +200% | `reported_return_anchor_not_full_ohlc` |
| `r1_loop8_hd_hyundai_marine_ipo_premium` | reported IPO first-day price anchor | first-day close +96.5% | `reported_price_anchor_not_full_ohlc` |
| `r1_loop8_hanwha_ocean_china_sanction` | reported sanction-event one-day return anchor | -5.8% one day | `reported_return_anchor_not_full_ohlc` |
| `r1_loop8_hd_hyundai_heavy_mipo_merger_4b` | reported merger-event one-day return anchors | +11.3% and +14.6% one day | `reported_return_anchor_not_full_ohlc` |

## Backfill Rule

- Use reported media anchors only for fields they explicitly support.
- Keep full OHLC unavailable until official or adjusted daily price backfill is done.
- Separate Stage 2 watch, Stage 3 anchor, 4B event, and 4C-watch event.
- Do not promote event price jumps to Green without backlog, delivery, margin, and OP/EPS evidence.
