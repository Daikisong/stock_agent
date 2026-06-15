# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| `mode` | `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12` |
| `research_session` | `post_calibrated_sector_archetype_residual_research` |
| `output_filename` | `e2r_stock_web_v12_residual_round_R9_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md` |
| `selected_round` | `R9` |
| `selected_loop` | `101` |
| `selection_basis` | `docs/core/V12_Research_No_Repeat_Index.md` |
| `selected_priority_bucket` | `Priority 2 / quality holdout after session-adjusted Priority-0 and Priority-1 fills` |
| `round_schedule_status` | `coverage_index_selected` |
| `round_sector_consistency` | `pass` |
| `large_sector_id` | `L3_BATTERY_EV_GREEN_MOBILITY` |
| `canonical_archetype_id` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` |
| `fine_archetype_id` | `mixed_C29_auto_parts_tire_margin_operating_leverage_quality_holdout` |
| `loop_objective` | `quality_holdout | counterexample_mining | 4B_high_MAE_guard | canonical_archetype_compression | margin_bridge_validation` |
| `production_scoring_changed` | `false` |
| `shadow_weight_only` | `true` |
| `stock_agent_code_access_allowed` | `false` |
| `stock_agent_code_patch_allowed` | `false` |
| `current_stock_discovery_allowed` | `false` |
| `price_source` | `Songdaiki/stock-web` |
| `stock_web_manifest_max_date` | `2026-02-20` |

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated`; active batch context: `e2r_2_2_rolling_calibrated`. This research does not repeat the global calibrated rule. It tests C29-specific residual behavior after the first C29 pass: scaled OEM/parts/tire evidence can work, but the gate must separate **volume/mix/margin bridge** from a simple mobility headline. The main residual is not whether mobility can rerate; it is whether the model can avoid chasing suppliers or tire-cycle rows after the initial vertical move when MAE180 opens deeply.

## 2. Round / Large Sector / Canonical Archetype Scope

| item | value |
|---|---|
| round | `R9` |
| large_sector_id | `L3_BATTERY_EV_GREEN_MOBILITY` |
| canonical_archetype_id | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` |
| canonical purpose | Mobility volume/mix/margin and operating leverage, including scaled suppliers, tire-cycle margin recovery, and xEV/HEV part conversion. |
| fine split | `OEM_CORE_PARTS_MIX_MARGIN_BRIDGE`, `TIRE_PREMIUM_MIX_OPERATING_LEVERAGE`, `LIGHTING_SUPPLIER_LED_MIX_MARGIN_BRIDGE`, `EV_BATTERY_CASE_ORDER_REVENUE_TIMING_HIGH_MAE`, `HEV_EOP_XEV_PARTS_REVENUE_RECOVERY` |

## 3. Coverage / Duplicate Avoidance Check

No-Repeat Index now marks C29 as Priority 2 with high absolute coverage, so this is not a raw row-count fill. It is a quality holdout. The previous C29 research in this session used `005380`, `000270`, `204320`, `018880`, and `118990`. This loop avoids those symbols and uses seven C29 symbols not previously used in the C29 session set.

Hard duplicate key checked as `canonical_archetype_id + symbol + trigger_type + entry_date`.

| candidate | symbol | trigger_type | entry_date | duplicate status |
|---|---:|---|---|---|
| 현대모비스 | `012330` | `Stage2-Actionable` | 2024-01-29 | new C29 symbol / not prior C29 session case |
| 현대위아 | `011210` | `Stage4B` | 2024-01-29 | new C29 symbol / not prior C29 session case |
| 한국타이어앤테크놀로지 | `161390` | `Stage2-Actionable` | 2024-02-05 | new C29 symbol / not prior C29 session case |
| 금호타이어 | `073240` | `Stage2-Actionable` | 2024-02-06 | new C29 symbol / not prior C29 session case |
| 에스엘 | `005850` | `Stage3-Yellow` | 2024-05-17 | new C29 symbol / not prior C29 session case |
| 화신 | `010690` | `Stage4B` | 2024-05-16 | new C29 symbol / not prior C29 session case |
| SNT모티브 | `064960` | `Stage2-Actionable` | 2025-03-18 | new C29 symbol / not prior C29 session case |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| `source` | `Songdaiki/stock-web` |
| `manifest_path` | `atlas/manifest.json` |
| `schema_path` | `atlas/schema.json` |
| `universe_path` | `atlas/universe/all_symbols.csv` |
| `manifest_max_date` | `2026-02-20` |
| `price_basis` | `tradable_raw` |
| `price_adjustment_status` | `raw_unadjusted_marcap` |
| `calibration_shard_root` | `atlas/ohlcv_tradable_by_symbol_year` |
| `raw_shard_root` | `atlas/ohlcv_raw_by_symbol_year` |
| `validation_status` | `usable_for_historical_calibration` |

MFE/MAE uses stock-web schema rule: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 5. Historical Eligibility Gate

| symbol | entry_date | forward_180D | window_end | corporate_action_window_status | calibration_usable |
|---:|---|---:|---|---|---|
| `012330` | 2024-01-29 | 180 | 2024-10-25 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |
| `011210` | 2024-01-29 | 180 | 2024-10-25 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |
| `161390` | 2024-02-05 | 180 | 2024-11-01 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |
| `073240` | 2024-02-06 | 180 | 2024-11-04 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |
| `005850` | 2024-05-17 | 180 | 2025-02-13 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |
| `010690` | 2024-05-16 | 180 | 2025-02-12 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |
| `064960` | 2025-03-18 | 180 | 2025-12-09 | clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate | true |

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | compressed canonical | calibration role |
|---|---|---|
| `OEM_CORE_PARTS_MIX_MARGIN_BRIDGE` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Positive gate: core parts/electrification/OEM mix and operating-profit bridge with low early MAE. |
| `AUTO_PARTS_SCALE_WITH_WEAK_DURABILITY` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Counterexample gate: auto-parts scale exists, but fast peak and 180D drawdown cap Stage3. |
| `TIRE_PREMIUM_MIX_OPERATING_LEVERAGE` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Positive-with-4B gate: tire-cycle mix and OP margin can rerate, but peak drawdown must be watched. |
| `TIRE_TURNAROUND_MARGIN_RECOVERY` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Turnaround positive gate with strong MFE but high full-window drawdown. |
| `LIGHTING_SUPPLIER_LED_MIX_MARGIN_BRIDGE` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Stage3-Yellow candidate when product mix, cost savings, and OPM bridge arrive together. |
| `EV_BATTERY_CASE_ORDER_REVENUE_TIMING_HIGH_MAE` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | 4B cap: vertical MFE from EV parts/order timing without durable margin bridge. |
| `HEV_EOP_XEV_PARTS_REVENUE_RECOVERY` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Delayed positive when HEV/EOP/xEV part conversion produces low-MAE follow-through. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | polarity | best_trigger |
|---|---:|---|---|---|---|
| `C29_R9_L101_012330_20240129_oem_core_parts_mix_margin_bridge` | `012330` | 현대모비스 | `structural_success` | `positive` | `Stage2-Actionable` |
| `C29_R9_L101_011210_20240129_auto_parts_scale_with_weak_durability` | `011210` | 현대위아 | `early_peak_counterexample` | `counterexample` | `Stage4B` |
| `C29_R9_L101_161390_20240205_tire_premium_mix_operating_leverage` | `161390` | 한국타이어앤테크놀로지 | `tire_cycle_positive_with_high_mae` | `positive_with_4B_watch` | `Stage2-Actionable` |
| `C29_R9_L101_073240_20240206_tire_turnaround_margin_recovery` | `073240` | 금호타이어 | `turnaround_positive_with_4B_watch` | `positive_with_4B_watch` | `Stage2-Actionable` |
| `C29_R9_L101_005850_20240517_lighting_supplier_led_mix_margin_bridge` | `005850` | 에스엘 | `supplier_margin_surprise_positive_with_4B_watch` | `positive` | `Stage3-Yellow` |
| `C29_R9_L101_010690_20240516_ev_battery_case_order_revenue_timing_high_mae` | `010690` | 화신 | `battery_case_ev_parts_high_mae_counterexample` | `counterexample` | `Stage4B` |
| `C29_R9_L101_064960_20250318_hev_eop_xev_parts_revenue_recovery` | `064960` | SNT모티브 | `hev_eop_xev_parts_recovery_positive` | `positive` | `Stage2-Actionable` |

## 8. Positive vs Counterexample Balance

- Positive and positive-with-watch case count: `5`
- Counterexample count: `2`
- Local 4B/high-MAE watch rows: `5`
- Hard 4C rows: `0`
- Average MFE180: `36.7138`
- Average MAE180: `-22.2988`

C29 is a clutch system, not a simple accelerator pedal. Volume/mix/margin evidence transfers engine torque to the equity price only when revenue recognition and operating leverage engage cleanly. If the clutch slips—fast peak, weak durability, financing/working-capital stress, or high-MAE drawdown—the model should keep the row in Stage4B or local 4B even when the first MFE is large.

## 9. Evidence Source Map

| symbol | trigger_date | evidence source | non-price evidence extracted |
|---:|---|---|---|
| `012330` | 2024-01-26 | https://www.mobis.com/en/ir/ircop.do | 2023 revenue KRW59.2544tn and operating profit KRW2.2953tn; electrification/core parts and high-value SUV/mix path made volume/mix/margin bridge visible. |
| `011210` | 2024-01-26 | https://en.hyundai-wia.com/investment/income_statement01.asp | 2023 revenue KRW8.166tn and operating profit KRW233bn made auto-parts scale visible, but the price path peaked quickly and failed to hold the 180D window. |
| `161390` | 2024-02-05 | https://www.hankooktire.com/global/ko/company/media-list/media-detail.629718.html | 2023 sales KRW8.9396tn and operating profit KRW1.3279tn; premium OE/EV/high-value product mix drove record profitability. |
| `073240` | 2024-01-30 | https://m.thebell.co.kr/m/newsview.asp?newskey=202401301713409800101922&svccode= | 2023 revenue KRW4.041tn and operating profit KRW388.3bn; 4Q OP margin 14.1% showed tire turnaround and margin recovery, but full-window drawdown was large. |
| `005850` | 2024-05-16 | https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024051618092158K_02_06.pdf&inlineYn=Y&saveKey=research.pdf | 1Q24 revenue grew despite Hyundai/Kia global production decline and OPM reached 11.1%; LED lamp mix, US/India cost savings, and new mood-lamp order supported margin bridge. |
| `010690` | 2024-05-16 | https://ssl.pstatic.net/imgstock/upload/research/company/1705370145067.pdf | 2024 battery-pack case revenue recognition and HMG EV production sequence were visible, but the 90D/180D path showed a vertical MFE followed by deep MAE. |
| `064960` | 2025-03-17 | https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2025031616114212K_02_07.pdf&inlineYn=Y&saveKey=research.pdf | 2025 auto-parts recovery was tied to HEV motor / electronic oil pump and xEV component revenue, giving a cleaner volume/mix/margin bridge after 2024 weakness. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | local source cache |
|---:|---|---|---|
| `012330` | `atlas/ohlcv_tradable_by_symbol_year/012/012330/{year}.csv` | `atlas/symbol_profiles/012/012330.json` | local stock-web cache: `012330_2023/2024/2025.csv` |
| `011210` | `atlas/ohlcv_tradable_by_symbol_year/011/011210/{year}.csv` | `atlas/symbol_profiles/011/011210.json` | local stock-web cache: `011210_2023/2024/2025.csv` |
| `161390` | `atlas/ohlcv_tradable_by_symbol_year/161/161390/{year}.csv` | `atlas/symbol_profiles/161/161390.json` | local stock-web cache: `161390_2023/2024/2025.csv` |
| `073240` | `atlas/ohlcv_tradable_by_symbol_year/073/073240/{year}.csv` | `atlas/symbol_profiles/073/073240.json` | local stock-web cache: `073240_2023/2024/2025.csv` |
| `005850` | `atlas/ohlcv_tradable_by_symbol_year/005/005850/{year}.csv` | `atlas/symbol_profiles/005/005850.json` | local stock-web cache: `005850_2024/2025.csv` |
| `010690` | `atlas/ohlcv_tradable_by_symbol_year/010/010690/{year}.csv` | `atlas/symbol_profiles/010/010690.json` | local stock-web cache: `010690_2024/2025.csv` |
| `064960` | `atlas/ohlcv_tradable_by_symbol_year/064/064960/{year}.csv` | `atlas/symbol_profiles/064/064960.json` | local stock-web cache: `064960_2024/2025.csv` |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | 4C fields |
|---:|---|---|---|---:|---|---|---|---|
| `012330` | `Stage2-Actionable` | 2024-01-26 | 2024-01-29 | 202500 | record revenue, core-parts/electrification demand, group OEM volume/mix evidence | operating profit growth, margin bridge, low early MAE | post-peak drawdown means Yellow not Green | - |
| `011210` | `Stage4B` | 2024-01-26 | 2024-01-29 | 58000 | auto-parts scale and profit evidence | insufficient durable margin/revision bridge | fast MFE followed by MAE180 below -20% | - |
| `161390` | `Stage2-Actionable` | 2024-02-05 | 2024-02-05 | 50000 | record profit, premium/EV tire mix, logistics/raw material relief | conditional only; 180D high-MAE argues against Green | MAE180 near -31% and peak drawdown over -45% | - |
| `073240` | `Stage2-Actionable` | 2024-01-30 | 2024-02-06 | 6140 | turnaround revenue/OP, margin recovery | conditional; needs sustained mix/replacement demand confirmation | MFE90 strong but MAE180 below -30% | - |
| `005850` | `Stage3-Yellow` | 2024-05-16 | 2024-05-17 | 35500 | new item/order plus OEM production exposure | OPM surprise, LED mix, cost savings, margin bridge | peak drawdown requires local 4B watch after Stage3-Yellow | - |
| `010690` | `Stage4B` | 2024-05-16 | 2024-05-16 | 10490 | battery-pack case, HMG EV production path, HMG sales guide | not yet; revenue/margin durability not confirmed | MFE30 above 50% but MAE180 below -40% | - |
| `064960` | `Stage2-Actionable` | 2025-03-17 | 2025-03-18 | 25550 | HEV/EOP/xEV parts recovery and revenue growth expectation | low MAE with 90D/180D MFE follow-through validates delayed Yellow | not primary; low MAE path | - |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| `012330` | 2024-01-29 | 202500 | 27.4074 | -0.4938 | 33.3333 | -0.4938 | 33.3333 | -0.9877 | 2024-03-18 | 270000 | -25.7407 |
| `011210` | 2024-01-29 | 58000 | 15.5172 | -2.5862 | 15.5172 | -6.0345 | 15.5172 | -21.6379 | 2024-02-05 | 67000 | -32.1642 |
| `161390` | 2024-02-05 | 50000 | 19.2000 | -4.1000 | 26.6000 | -15.7000 | 26.6000 | -31.0000 | 2024-04-16 | 63300 | -45.4976 |
| `073240` | 2024-02-06 | 6140 | 12.0521 | -9.1205 | 36.1564 | -9.6091 | 36.1564 | -33.7134 | 2024-05-07 | 8360 | -51.3158 |
| `005850` | 2024-05-17 | 35500 | 34.2254 | -5.7746 | 34.2254 | -14.3662 | 34.2254 | -23.6620 | 2024-06-17 | 47650 | -43.1270 |
| `010690` | 2024-05-16 | 10490 | 51.4776 | -2.7645 | 51.4776 | -24.9762 | 51.4776 | -41.3727 | 2024-06-27 | 15890 | -61.2964 |
| `064960` | 2025-03-18 | 25550 | 13.5029 | -3.7182 | 44.4227 | -3.7182 | 59.6869 | -3.7182 | 2025-12-08 | 40800 | -13.7255 |

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | proposed stage after C29 shadow gate | interpretation |
|---:|---|---|---|
| `012330` | `current_profile_correct_or_too_late` | `Stage3-Yellow` | MFE180 33.3% / MAE180 -1.0% |
| `011210` | `current_profile_false_positive_risk` | `Stage4B` | MFE180 15.5% / MAE180 -21.6% |
| `161390` | `current_profile_correct_or_too_late` | `Stage2-Actionable` | MFE180 26.6% / MAE180 -31.0% |
| `073240` | `current_profile_correct_or_too_late` | `Stage2-Actionable` | MFE180 36.2% / MAE180 -33.7% |
| `005850` | `current_profile_correct_or_too_late` | `Stage3-Yellow` | MFE180 34.2% / MAE180 -23.7% |
| `010690` | `current_profile_false_positive_risk` | `Stage4B` | MFE180 51.5% / MAE180 -41.4% |
| `064960` | `current_profile_correct_or_too_late` | `Stage3-Yellow` | MFE180 59.7% / MAE180 -3.7% |

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 valid? | Yellow valid? | Green valid? | reason |
|---:|---|---|---|---|
| `012330` | yes | yes | no | Low MAE and margin bridge support Yellow, but Green still needs durable revision and post-peak drawdown control. |
| `011210` | conditional | no | no | Auto-parts scale is real, but early peak and MAE180 below -20% require Stage4B. |
| `161390` | yes | conditional | no | Record tire margin is real; high MAE and large peak drawdown block Green. |
| `073240` | yes | conditional | no | Turnaround margin path is real but tire-cycle drawdown requires local 4B. |
| `005850` | yes | yes | no | OPM surprise and LED/product mix justify Yellow; full-window drawdown blocks Green. |
| `010690` | conditional | no | no | EV battery-case path produced very high MFE but the full-window failure is a 4B warning. |
| `064960` | yes | yes | no | HEV/EOP/xEV revenue recovery produced high MFE and low MAE; delayed Yellow is valid. |

## 15. 4B Local vs Full-window Timing Audit

| symbol | local 4B reason | full-window 4B reason | audit |
|---:|---|---|---|
| `012330` | post-peak drawdown from March peak | MAE180 shallow | not full 4B; keep Yellow not Green |
| `011210` | MFE peak within days | MAE180 -21.6379 | cap Stage4B |
| `161390` | peak by April | MAE180 -31.0000 | positive evidence but full-window local 4B required |
| `073240` | peak by May | MAE180 -33.7134 | turnaround positive but high-MAE 4B required |
| `005850` | 34% MFE in 30D | MAE180 -23.6620 | Yellow allowed, Green blocked |
| `010690` | MFE30 51.4776 | MAE180 -41.3727 | classic vertical MFE/high-MAE 4B cap |
| `064960` | no material early blowoff | MAE180 -3.7182 | positive delayed rerating path |

## 16. Sector-Specific Rule Candidate

`L3_C29_MOBILITY_VOLUME_MIX_MARGIN_AND_HIGH_MAE_SPLIT`:

```text
stage2_gate = mobility_volume_or_customer_growth + product_mix_or_order_visibility
stage3_yellow_gate = stage2_gate + realized_OPM_or_profit_growth + revenue_recognition_or_margin_bridge
stage3_green_gate = stage3_yellow_gate + low_MAE90 + low_MAE180 + no vertical local_4B_peak + no financing/restructuring/one-off reliance
4b_cap = MFE30_or_MFE90 >= 30 and MAE180 <= -20, or peak_drawdown_after_180D_window <= -30, unless durable margin bridge remains confirmed
4c_route = operating_loss_or_net_loss + volume slowdown + impairment/restructuring/interest burden
```

## 17. Canonical-Archetype Rule Candidate

`C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_REALIZED_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP`:

```text
positive_gate:
  volume_growth_or_customer_quality
  + product_mix_or_xEV_HEV_part_conversion
  + realized_OP_margin_or_profit_growth
  + evidence of revenue recognition or order conversion

cap_to_stage2_watch:
  mobility headline only
  or supplier order timing without margin bridge
  or tire/parts cycle row with MAE180 <= -20
  or peak_drawdown_after_peak_180D <= -30

upgrade_to_yellow:
  positive_gate true
  and MAE90 > -20
  and either low_MAE180 or delayed strong MFE after margin bridge confirmation

block_green:
  local vertical MFE without 180D drawdown control
```

## 18. Before / After Backtest Comparison

| profile proxy | expected accepted positives | expected blocked/capped rows | expected effect |
|---|---:|---:|---|
| P0 current calibrated proxy | 5 | 2 | Accepts most mobility/parts rows but risks over-reading early tire/supplier MFE. |
| P1 C29 shadow gate | 4 | 3 | Keeps Mobis/SL/SNT positive, allows tire rows only with 4B watch, caps Wia/Hwashin. |
| P2 overly strict high-MAE block | 2 | 5 | Overblocks tire-cycle and SL positive MFE paths. |
| P3 headline-growth naive | 7 | 0 | Overpromotes Wia/Hwashin and ignores post-peak drawdown. |

## 19. Score-Return Alignment Matrix

```jsonl
{"row_type": "score_simulation", "case_id": "C29_R9_L101_012330_20240129_oem_core_parts_mix_margin_bridge", "symbol": "012330", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 80, "stage_before": "Stage2-Actionable", "weighted_after": 84, "stage_after": "Stage3-Yellow", "MFE_90D_pct": 33.3333, "MAE_90D_pct": -0.4938, "alignment": "good_score_high_return"}
{"row_type": "score_simulation", "case_id": "C29_R9_L101_011210_20240129_auto_parts_scale_with_weak_durability", "symbol": "011210", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 74, "stage_before": "Stage4B", "weighted_after": 66, "stage_after": "Stage4B", "MFE_90D_pct": 15.5172, "MAE_90D_pct": -6.0345, "alignment": "high_mae_guard_required"}
{"row_type": "score_simulation", "case_id": "C29_R9_L101_161390_20240205_tire_premium_mix_operating_leverage", "symbol": "161390", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 80, "stage_before": "Stage2-Actionable", "weighted_after": 78, "stage_after": "Stage2-Actionable", "MFE_90D_pct": 26.6, "MAE_90D_pct": -15.7, "alignment": "good_score_high_return"}
{"row_type": "score_simulation", "case_id": "C29_R9_L101_073240_20240206_tire_turnaround_margin_recovery", "symbol": "073240", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 80, "stage_before": "Stage2-Actionable", "weighted_after": 78, "stage_after": "Stage2-Actionable", "MFE_90D_pct": 36.1564, "MAE_90D_pct": -9.6091, "alignment": "good_score_high_return"}
{"row_type": "score_simulation", "case_id": "C29_R9_L101_005850_20240517_lighting_supplier_led_mix_margin_bridge", "symbol": "005850", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 80, "stage_before": "Stage3-Yellow", "weighted_after": 84, "stage_after": "Stage3-Yellow", "MFE_90D_pct": 34.2254, "MAE_90D_pct": -14.3662, "alignment": "good_score_high_return"}
{"row_type": "score_simulation", "case_id": "C29_R9_L101_010690_20240516_ev_battery_case_order_revenue_timing_high_mae", "symbol": "010690", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 74, "stage_before": "Stage4B", "weighted_after": 66, "stage_after": "Stage4B", "MFE_90D_pct": 51.4776, "MAE_90D_pct": -24.9762, "alignment": "high_mae_guard_required"}
{"row_type": "score_simulation", "case_id": "C29_R9_L101_064960_20250318_hev_eop_xev_parts_revenue_recovery", "symbol": "064960", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "weighted_before": 80, "stage_before": "Stage2-Actionable", "weighted_after": 84, "stage_after": "Stage3-Yellow", "MFE_90D_pct": 44.4227, "MAE_90D_pct": -3.7182, "alignment": "good_score_high_return"}
```

## 20. Machine-Readable Trigger Rows

```jsonl
{"row_type": "trigger", "case_id": "C29_R9_L101_012330_20240129_oem_core_parts_mix_margin_bridge", "symbol": "012330", "company": "현대모비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_CORE_PARTS_MIX_MARGIN_BRIDGE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "entry_date": "2024-01-29", "entry_price": 202500.0, "case_type": "structural_success", "polarity": "positive", "current_profile_verdict": "current_profile_correct_or_too_late", "stage_after_shadow_rule": "Stage3-Yellow", "evidence_source": "https://www.mobis.com/en/ir/ircop.do", "evidence_summary": "2023 revenue KRW59.2544tn and operating profit KRW2.2953tn; electrification/core parts and high-value SUV/mix path made volume/mix/margin bridge visible.", "stage2_fields": "record revenue, core-parts/electrification demand, group OEM volume/mix evidence", "stage3_fields": "operating profit growth, margin bridge, low early MAE", "fourb_fields": "post-peak drawdown means Yellow not Green", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2024-10-25", "MFE_30D_pct": 27.4074, "MAE_30D_pct": -0.4938, "MFE_90D_pct": 33.3333, "MAE_90D_pct": -0.4938, "MFE_180D_pct": 33.3333, "MAE_180D_pct": -0.9877, "peak_date": "2024-03-18", "peak_price": 270000.0, "drawdown_after_peak_180D_pct": -25.7407}
{"row_type": "trigger", "case_id": "C29_R9_L101_011210_20240129_auto_parts_scale_with_weak_durability", "symbol": "011210", "company": "현대위아", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_SCALE_WITH_WEAK_DURABILITY", "trigger_type": "Stage4B", "trigger_date": "2024-01-26", "entry_date": "2024-01-29", "entry_price": 58000.0, "case_type": "early_peak_counterexample", "polarity": "counterexample", "current_profile_verdict": "current_profile_false_positive_risk", "stage_after_shadow_rule": "Stage4B", "evidence_source": "https://en.hyundai-wia.com/investment/income_statement01.asp", "evidence_summary": "2023 revenue KRW8.166tn and operating profit KRW233bn made auto-parts scale visible, but the price path peaked quickly and failed to hold the 180D window.", "stage2_fields": "auto-parts scale and profit evidence", "stage3_fields": "insufficient durable margin/revision bridge", "fourb_fields": "fast MFE followed by MAE180 below -20%", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2024-10-25", "MFE_30D_pct": 15.5172, "MAE_30D_pct": -2.5862, "MFE_90D_pct": 15.5172, "MAE_90D_pct": -6.0345, "MFE_180D_pct": 15.5172, "MAE_180D_pct": -21.6379, "peak_date": "2024-02-05", "peak_price": 67000.0, "drawdown_after_peak_180D_pct": -32.1642}
{"row_type": "trigger", "case_id": "C29_R9_L101_161390_20240205_tire_premium_mix_operating_leverage", "symbol": "161390", "company": "한국타이어앤테크놀로지", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_PREMIUM_MIX_OPERATING_LEVERAGE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-05", "entry_date": "2024-02-05", "entry_price": 50000.0, "case_type": "tire_cycle_positive_with_high_mae", "polarity": "positive_with_4B_watch", "current_profile_verdict": "current_profile_correct_or_too_late", "stage_after_shadow_rule": "Stage2-Actionable", "evidence_source": "https://www.hankooktire.com/global/ko/company/media-list/media-detail.629718.html", "evidence_summary": "2023 sales KRW8.9396tn and operating profit KRW1.3279tn; premium OE/EV/high-value product mix drove record profitability.", "stage2_fields": "record profit, premium/EV tire mix, logistics/raw material relief", "stage3_fields": "conditional only; 180D high-MAE argues against Green", "fourb_fields": "MAE180 near -31% and peak drawdown over -45%", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2024-11-01", "MFE_30D_pct": 19.2, "MAE_30D_pct": -4.1, "MFE_90D_pct": 26.6, "MAE_90D_pct": -15.7, "MFE_180D_pct": 26.6, "MAE_180D_pct": -31.0, "peak_date": "2024-04-16", "peak_price": 63300.0, "drawdown_after_peak_180D_pct": -45.4976}
{"row_type": "trigger", "case_id": "C29_R9_L101_073240_20240206_tire_turnaround_margin_recovery", "symbol": "073240", "company": "금호타이어", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_TURNAROUND_MARGIN_RECOVERY", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-30", "entry_date": "2024-02-06", "entry_price": 6140.0, "case_type": "turnaround_positive_with_4B_watch", "polarity": "positive_with_4B_watch", "current_profile_verdict": "current_profile_correct_or_too_late", "stage_after_shadow_rule": "Stage2-Actionable", "evidence_source": "https://m.thebell.co.kr/m/newsview.asp?newskey=202401301713409800101922&svccode=", "evidence_summary": "2023 revenue KRW4.041tn and operating profit KRW388.3bn; 4Q OP margin 14.1% showed tire turnaround and margin recovery, but full-window drawdown was large.", "stage2_fields": "turnaround revenue/OP, margin recovery", "stage3_fields": "conditional; needs sustained mix/replacement demand confirmation", "fourb_fields": "MFE90 strong but MAE180 below -30%", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2024-11-04", "MFE_30D_pct": 12.0521, "MAE_30D_pct": -9.1205, "MFE_90D_pct": 36.1564, "MAE_90D_pct": -9.6091, "MFE_180D_pct": 36.1564, "MAE_180D_pct": -33.7134, "peak_date": "2024-05-07", "peak_price": 8360.0, "drawdown_after_peak_180D_pct": -51.3158}
{"row_type": "trigger", "case_id": "C29_R9_L101_005850_20240517_lighting_supplier_led_mix_margin_bridge", "symbol": "005850", "company": "에스엘", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LIGHTING_SUPPLIER_LED_MIX_MARGIN_BRIDGE", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 35500.0, "case_type": "supplier_margin_surprise_positive_with_4B_watch", "polarity": "positive", "current_profile_verdict": "current_profile_correct_or_too_late", "stage_after_shadow_rule": "Stage3-Yellow", "evidence_source": "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024051618092158K_02_06.pdf&inlineYn=Y&saveKey=research.pdf", "evidence_summary": "1Q24 revenue grew despite Hyundai/Kia global production decline and OPM reached 11.1%; LED lamp mix, US/India cost savings, and new mood-lamp order supported margin bridge.", "stage2_fields": "new item/order plus OEM production exposure", "stage3_fields": "OPM surprise, LED mix, cost savings, margin bridge", "fourb_fields": "peak drawdown requires local 4B watch after Stage3-Yellow", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2025-02-13", "MFE_30D_pct": 34.2254, "MAE_30D_pct": -5.7746, "MFE_90D_pct": 34.2254, "MAE_90D_pct": -14.3662, "MFE_180D_pct": 34.2254, "MAE_180D_pct": -23.662, "peak_date": "2024-06-17", "peak_price": 47650.0, "drawdown_after_peak_180D_pct": -43.127}
{"row_type": "trigger", "case_id": "C29_R9_L101_010690_20240516_ev_battery_case_order_revenue_timing_high_mae", "symbol": "010690", "company": "화신", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_BATTERY_CASE_ORDER_REVENUE_TIMING_HIGH_MAE", "trigger_type": "Stage4B", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 10490.0, "case_type": "battery_case_ev_parts_high_mae_counterexample", "polarity": "counterexample", "current_profile_verdict": "current_profile_false_positive_risk", "stage_after_shadow_rule": "Stage4B", "evidence_source": "https://ssl.pstatic.net/imgstock/upload/research/company/1705370145067.pdf", "evidence_summary": "2024 battery-pack case revenue recognition and HMG EV production sequence were visible, but the 90D/180D path showed a vertical MFE followed by deep MAE.", "stage2_fields": "battery-pack case, HMG EV production path, HMG sales guide", "stage3_fields": "not yet; revenue/margin durability not confirmed", "fourb_fields": "MFE30 above 50% but MAE180 below -40%", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2025-02-12", "MFE_30D_pct": 51.4776, "MAE_30D_pct": -2.7645, "MFE_90D_pct": 51.4776, "MAE_90D_pct": -24.9762, "MFE_180D_pct": 51.4776, "MAE_180D_pct": -41.3727, "peak_date": "2024-06-27", "peak_price": 15890.0, "drawdown_after_peak_180D_pct": -61.2964}
{"row_type": "trigger", "case_id": "C29_R9_L101_064960_20250318_hev_eop_xev_parts_revenue_recovery", "symbol": "064960", "company": "SNT모티브", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HEV_EOP_XEV_PARTS_REVENUE_RECOVERY", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-03-17", "entry_date": "2025-03-18", "entry_price": 25550.0, "case_type": "hev_eop_xev_parts_recovery_positive", "polarity": "positive", "current_profile_verdict": "current_profile_correct_or_too_late", "stage_after_shadow_rule": "Stage3-Yellow", "evidence_source": "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2025031616114212K_02_07.pdf&inlineYn=Y&saveKey=research.pdf", "evidence_summary": "2025 auto-parts recovery was tied to HEV motor / electronic oil pump and xEV component revenue, giving a cleaner volume/mix/margin bridge after 2024 weakness.", "stage2_fields": "HEV/EOP/xEV parts recovery and revenue growth expectation", "stage3_fields": "low MAE with 90D/180D MFE follow-through validates delayed Yellow", "fourb_fields": "not primary; low MAE path", "fourc_fields": "-", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_window_status": "clean_180D_window_assumed_profile_no_overlap_checked_by_stockweb_ui_or_no_local_profile_candidate", "window_end": "2025-12-09", "MFE_30D_pct": 13.5029, "MAE_30D_pct": -3.7182, "MFE_90D_pct": 44.4227, "MAE_90D_pct": -3.7182, "MFE_180D_pct": 59.6869, "MAE_180D_pct": -3.7182, "peak_date": "2025-12-08", "peak_price": 40800.0, "drawdown_after_peak_180D_pct": -13.7255}
```

## 21. Aggregate / Residual Contribution Rows

```jsonl
{"row_type": "aggregate", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_usable_rows": 7, "positive_case_count": 5, "counterexample_count": 2, "four_b_watch_count": 5, "four_c_count": 0, "avg_MFE_180D_pct": 36.7138, "avg_MAE_180D_pct": -22.2988, "rule_candidate": "C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_REALIZED_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP"}
{"row_type": "shadow_weight", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "do_not_apply_now": true, "proposed_axis": "C29_volume_mix_margin_bridge_plus_high_MAE_cap", "direction": "increase margin_bridge and information_confidence weight; increase local_4b_watch penalty for MAE180<=-20", "reason": "C29 quality holdout shows good MFE can coexist with deep MAE unless realized margin/revenue bridge is present."}
{"row_type": "residual_contribution", "label": "residual_error_found", "current_profile_error_count": 5, "error_family": "C29_mobility_headline_or_fast_MFE_overpromotion", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": []}
```

## 22. Narrative Summary

This holdout strengthens C29 rather than merely adding more mobility rows. The best rows are not the ones with the loudest auto headline; they are the rows where **volume/mix/margin** enters the gearbox and comes out as realized operating leverage. Hyundai Mobis and SNT Motiv show low-MAE or delayed-clean positive paths. SL shows a good Yellow path but requires post-peak discipline. Hankook Tire and Kumho Tire prove that tire-cycle margin recovery can open MFE, yet full-window drawdown keeps the row from becoming Green. Hyundai Wia and Hwashin are the useful counterexamples: auto-parts scale, EV parts, or customer exposure can exist while the equity path still behaves like a failed late chase.

## 23. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent in a later batch implementation session. Do not execute this during the research run.

Input MD:
e2r_stock_web_v12_residual_round_R9_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Ingest the trigger JSONL rows only if all required entry/MFE/MAE fields are present.
2. Confirm canonical_archetype_id is C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE and large_sector_id is L3_BATTERY_EV_GREEN_MOBILITY.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add a C29 shadow rule candidate:
   C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_REALIZED_MARGIN_BRIDGE_WITH_HIGH_MAE_4B_CAP.
5. Do not change production scoring directly. Emit patch spec as shadow_weight_only candidate.
6. Preserve Stage2 bridge requirements and local 4B watch guard for MAE180 <= -20 or peak drawdown <= -30.
```

## 24. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 7
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 25. Next Research State

```text
completed_round = R9
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / quality holdout after session-adjusted Priority-0 and Priority-1 fills
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_holdout_only_if_new_volume_margin_path | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_quality_holdout
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
