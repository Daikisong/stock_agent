# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R1
selected_loop = 219
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C05 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status = coverage_index_selected; local C05 max loop 218 -> selected loop 219; 직전 C10 loop 219 반복 회피
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD
loop_objective = counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression
price_source = Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
output_file = e2r_stock_web_v12_residual_round_R1_loop_219_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

This loop adds 8 new independent C05 representative cases, 4 counterexamples, and 6 current-profile residual errors. It intentionally avoids the previous user-visible C10 loop 219 and avoids local C05 hard duplicate keys.

## 1. Current Calibrated Profile Assumption

The stress-test reference is the post-calibrated E2R profile family. For this MD the current proxy is `e2r_2_2_rolling_calibrated_proxy`, with rollback comparison to `e2r_2_0_baseline_reference`. No production scoring is changed. The exercise is a shadow-only C05 rule proposal.

Already-applied axes tested here:

- `stage2_required_bridge`
- `stage3_green_revision_min_by_margin_cash_freshness`
- `local_4b_watch_guard`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R1`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`
- fine_archetype_id: `C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD`
- valid mapping: `C01~C05 -> R1 / L1`

Scope boundary: this is not a live candidate scan and not an investment recommendation. It is a historical trigger-level calibration file using only already-observed historical evidence and Stock-Web OHLC paths.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C05 as a Priority 1 quality target for margin / working-capital failure counterexamples and 4C timing reinforcement. Local C05 files through loop 218 were checked. The hard key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All eight representative trigger rows in this loop are new hard keys under C05. The loop rotates away from direct shipyard mega-order repeats into supplier, engine, offshore-structure, fitting, pipe-spool, and plant-equipment rows.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "tradable_columns": [
    "d",
    "o",
    "h",
    "l",
    "c",
    "v",
    "a",
    "mc",
    "s",
    "m"
  ]
}
```

The entry OHLC row is the `c` column close on the first tradable row at or after `trigger_date`, unless evidence timing requires next-trading-day entry. MFE/MAE are calculated by the Stock-Web schema rule: max high and min low from entry row through 30/90/180 tradable rows.

## 5. Historical Eligibility Gate

All representative trigger rows pass:

- historical trigger date only
- actual Stock-Web tradable entry row exists
- 180 forward tradable rows available before manifest max date `2026-02-20`
- positive OHLCV values
- complete 30D / 90D / 180D MFE and MAE
- 180D corporate-action contamination screen clean under the 20% share-count threshold

## 6. Canonical Archetype Compression Map

C05 is compressed as:

```text
order/backlog/result headline
  -> direct issuer/customer route
  -> realized margin or cost-rate proof
  -> working-capital/cash conversion
  -> persistence and price-phase sanity
```

Order is the pipe. Margin and cash are the water. A beautiful pipe with no water should not get Green.

## 7. Case Selection Summary

| # | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | role | current_profile_verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 082740 | 한화엔진 | Stage3-Yellow | 2024-02-23 | 2024-02-26 | 8,170 | 25.09 / -1.71 | 107.96 / -1.71 | 110.04 / -1.71 | direct_engine_contract_margin_bridge_positive | current_profile_missed_structural_if_contract_route_capped_at_watch |
| 2 | 100090 | SK오션플랜트 | Stage2 | 2024-06-04 | 2024-06-05 | 15,470 | 4.59 / -14.03 | 4.72 / -33.42 | 4.72 / -33.42 | large_order_headline_without_margin_cash_counterexample | current_profile_false_positive_if_large_contract_promoted_without_cash_bridge |
| 3 | 086670 | 비엠티 | Stage2 | 2024-05-28 | 2024-05-28 | 13,180 | 7.21 / -9.33 | 7.21 / -31.94 | 7.21 / -47.65 | source_proxy_fitting_valve_counterexample | current_profile_false_positive_proxy_route_without_order_conversion |
| 4 | 333430 | 일승 | Stage3-Yellow | 2025-05-15 | 2025-05-16 | 4,605 | 27.25 / -10.53 | 126.49 / -14.44 | 126.49 / -14.44 | report_result_and_shipbuilding_equipment_positive_with_phase_watch | current_profile_missed_structural_or_too_low_if_report_cash_bridge_ignored |
| 5 | 099410 | 동방선기 | Stage2-Actionable | 2024-10-04 | 2024-10-07 | 2,885 | 13.52 / -6.59 | 22.7 / -10.92 | 41.07 / -10.92 | ship_pipe_report_actionable_but_not_green | current_profile_correct_stage2_actionable_if_kept_below_green |
| 6 | 023160 | 태광 | Stage3-Yellow | 2024-08-29 | 2024-08-30 | 14,700 | 2.04 / -13.81 | 48.3 / -19.18 | 83.67 / -19.18 | backlog_revenue_recognition_delay_positive_high_mae_guard | current_profile_4C_too_early_if_initial_mae_overweighted |
| 7 | 013030 | 하이록코리아 | Stage3-Green | 2025-05-15 | 2025-05-16 | 27,650 | 16.46 / -2.89 | 50.09 / -2.89 | 50.09 / -2.89 | direct_report_quality_margin_positive | current_profile_correct_or_missed_green_when_cash_bridge_visible |
| 8 | 014620 | 성광벤드 | Stage3-Yellow | 2025-03-20 | 2025-03-21 | 26,300 | 12.17 / -14.26 | 40.3 / -14.26 | 47.53 / -14.26 | business_report_yellow_with_4b_phase_watch | current_profile_false_green_if_report_result_lifted_without_phase_cap |


## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
positive_case_count = 4
counterexample_count = 4
current_profile_error_count = 6
new_independent_case_count = 8
reused_case_count = 0
new_symbol_count = 7
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 8
```

Positive rows are not unconditional Green. Counterexamples are not automatic hard 4C. The useful calibration edge is the middle door: Stage2/Yellow with 4B-watch when the route survives but price phase or cash conversion is not yet clean.

## 9. Evidence Source Map

| # | symbol | source_quality | proxy_only | evidence_url | evidence_summary |
|---|---|---|---|---|---|
| 1 | 082740 | news_with_contract_disclosure_summary | false | https://securities.miraeasset.com/bbs/download/2125659.pdf?attachmentId=2125659 | 2024-02-23 한화오션향 선박용 엔진 공급계약 보도/공시 요약. 계약금액과 납기 가시성이 있는 direct issuer route이며, 이후 OHLC 경로가 낮은 MAE와 큰 90/180D MFE로 이어졌다. |
| 2 | 100090 | news_with_contract_amount | false | https://v.daum.net/v/HRQs7KiBUy | 2024-06-04 해상풍력 하부구조물 대형 수주 headline은 direct order route를 제공하지만, 당시 가격경로는 90/180D MFE가 거의 없고 MAE가 깊어 margin/cash conversion 확인 전 Green 승격을 막는 반례다. |
| 3 | 086670 | kirs_report_proxy | true | https://w4.kirs.or.kr/download/research/240528_%EB%B9%84%EC%97%A0%ED%8B%B0.pdf | 조선·반도체 피팅/밸브 노출은 보이지만 issuer-level order conversion이나 margin/cash bridge가 약한 proxy row다. 180D MAE가 매우 깊어 Stage2-required-bridge를 강화한다. |
| 4 | 333430 | direct_krx_quarterly_report | false | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002665&docno=&method=searchInitInfo | 2025년 분기보고서가 조선기자재 집중과 사업구조 개편을 확인하는 row다. 90/180D MFE가 크지만 peak 이후 drawdown이 커 Green보다는 Yellow+phase watch가 더 맞다. |
| 5 | 099410 | kirs_report_direct_business_profile | true | https://w4.kirs.or.kr/download/research/241004_%EB%8F%99%EB%B0%A9%EC%84%A0%EA%B8%B0.pdf | 선박용 배관 조선기자재 route는 뚜렷하지만 직접 수주·현금전환 row는 아니다. Actionable은 가능하나 Green으로 올리기 전 margin/cash freshness가 필요하다. |
| 6 | 023160 | broker_report_with_backlog_recognition_timing | true | https://stock.pstatic.net/stock-research/company/53/20240829_company_188003000.pdf | 수주잔고와 3~6개월 매출인식 lag가 동시에 언급된 fitting row다. 초기 MAE가 컸지만 90/180D MFE가 살아 있어 hard 4C가 아니라 Yellow+high-MAE watch가 적합하다. |
| 7 | 013030 | direct_krx_quarterly_report | false | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515001059&docno=&method=searchInitInfo | 분기보고서 기반의 fittings/valves issuer route와 양호한 forward path가 만나는 positive row다. 낮은 MAE와 50% MFE가 Green 허용 표본이지만, cash bridge가 없는 동종 report row와 구분해야 한다. |
| 8 | 014620 | direct_krx_business_report | false | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250320001317&docno=&method=searchInitInfo | 사업보고서 기반의 fittings/plant shipbuilding route는 존재하고 90/180D MFE도 양호하나, 30D MAE와 peak 이후 drawdown 때문에 Green보다 Yellow+local 4B-watch가 맞다. |


## 10. Price Data Source Map

| symbol | entry OHLCV row | 30D | 90D | 180D | peak/trough/drawdown | corporate-action screen |
|---|---|---|---|---|---|---|
| 082740 | 2024-02-26 O=8,200 H=8,210 L=8,080 C=8,170 V=306,373 | 25.09 / -1.71 | 107.96 / -1.71 | 110.04 / -1.71 | peak 2024-07-24 17,160; trough 2024-02-27 8,030; DD -35.9% | shares Δ max 16.6375%; clean_180D_window |
| 100090 | 2024-06-05 O=15,020 H=16,180 L=14,460 C=15,470 V=3,024,498 | 4.59 / -14.03 | 4.72 / -33.42 | 4.72 / -33.42 | peak 2024-09-24 16,200; trough 2024-08-05 10,300; DD -31.42% | shares Δ max 0.0%; clean_180D_window |
| 086670 | 2024-05-28 O=13,390 H=13,450 L=13,090 C=13,180 V=34,570 | 7.21 / -9.33 | 7.21 / -31.94 | 7.21 / -47.65 | peak 2024-06-05 14,130; trough 2024-12-09 6,900; DD -51.17% | shares Δ max 0.0%; clean_180D_window |
| 333430 | 2025-05-16 O=4,705 H=4,820 L=4,600 C=4,605 V=230,574 | 27.25 / -10.53 | 126.49 / -14.44 | 126.49 / -14.44 | peak 2025-09-11 10,430; trough 2025-07-18 3,940; DD -48.71% | shares Δ max 0.0%; clean_180D_window |
| 099410 | 2024-10-07 O=2,820 H=2,900 L=2,790 C=2,885 V=233,688 | 13.52 / -6.59 | 22.7 / -10.92 | 41.07 / -10.92 | peak 2025-05-27 4,070; trough 2024-12-09 2,570; DD -21.74% | shares Δ max 0.0%; clean_180D_window |
| 023160 | 2024-08-30 O=13,700 H=14,760 L=13,700 C=14,700 V=476,218 | 2.04 / -13.81 | 48.3 / -19.18 | 83.67 / -19.18 | peak 2025-03-04 27,000; trough 2024-10-31 11,880; DD -34.44% | shares Δ max 0.0%; clean_180D_window |
| 013030 | 2025-05-16 O=27,250 H=27,700 L=27,200 C=27,650 V=58,338 | 16.46 / -2.89 | 50.09 / -2.89 | 50.09 / -2.89 | peak 2025-09-11 41,500; trough 2025-05-23 26,850; DD -28.8% | shares Δ max 4.2886%; clean_180D_window |
| 014620 | 2025-03-21 O=25,400 H=26,600 L=25,350 C=26,300 V=377,001 | 12.17 / -14.26 | 40.3 / -14.26 | 47.53 / -14.26 | peak 2025-09-11 38,800; trough 2025-04-07 22,550; DD -34.02% | shares Δ max 4.9096%; clean_180D_window |


## 11. Case-by-Case Trigger Grid

### Case 1 — 082740 / 한화엔진 / direct_engine_contract_margin_bridge_positive

- Trigger: `Stage3-Yellow`, trigger date `2024-02-23`, entry `2024-02-26` close `8,170`.
- Actual path: MFE90 `107.96%`, MAE90 `-1.71%`, MFE180 `110.04%`, MAE180 `-1.71%`.
- Calibration meaning: 2024-02-23 한화오션향 선박용 엔진 공급계약 보도/공시 요약. 계약금액과 납기 가시성이 있는 direct issuer route이며, 이후 OHLC 경로가 낮은 MAE와 큰 90/180D MFE로 이어졌다.

### Case 2 — 100090 / SK오션플랜트 / large_order_headline_without_margin_cash_counterexample

- Trigger: `Stage2`, trigger date `2024-06-04`, entry `2024-06-05` close `15,470`.
- Actual path: MFE90 `4.72%`, MAE90 `-33.42%`, MFE180 `4.72%`, MAE180 `-33.42%`.
- Calibration meaning: 2024-06-04 해상풍력 하부구조물 대형 수주 headline은 direct order route를 제공하지만, 당시 가격경로는 90/180D MFE가 거의 없고 MAE가 깊어 margin/cash conversion 확인 전 Green 승격을 막는 반례다.

### Case 3 — 086670 / 비엠티 / source_proxy_fitting_valve_counterexample

- Trigger: `Stage2`, trigger date `2024-05-28`, entry `2024-05-28` close `13,180`.
- Actual path: MFE90 `7.21%`, MAE90 `-31.94%`, MFE180 `7.21%`, MAE180 `-47.65%`.
- Calibration meaning: 조선·반도체 피팅/밸브 노출은 보이지만 issuer-level order conversion이나 margin/cash bridge가 약한 proxy row다. 180D MAE가 매우 깊어 Stage2-required-bridge를 강화한다.

### Case 4 — 333430 / 일승 / report_result_and_shipbuilding_equipment_positive_with_phase_watch

- Trigger: `Stage3-Yellow`, trigger date `2025-05-15`, entry `2025-05-16` close `4,605`.
- Actual path: MFE90 `126.49%`, MAE90 `-14.44%`, MFE180 `126.49%`, MAE180 `-14.44%`.
- Calibration meaning: 2025년 분기보고서가 조선기자재 집중과 사업구조 개편을 확인하는 row다. 90/180D MFE가 크지만 peak 이후 drawdown이 커 Green보다는 Yellow+phase watch가 더 맞다.

### Case 5 — 099410 / 동방선기 / ship_pipe_report_actionable_but_not_green

- Trigger: `Stage2-Actionable`, trigger date `2024-10-04`, entry `2024-10-07` close `2,885`.
- Actual path: MFE90 `22.7%`, MAE90 `-10.92%`, MFE180 `41.07%`, MAE180 `-10.92%`.
- Calibration meaning: 선박용 배관 조선기자재 route는 뚜렷하지만 직접 수주·현금전환 row는 아니다. Actionable은 가능하나 Green으로 올리기 전 margin/cash freshness가 필요하다.

### Case 6 — 023160 / 태광 / backlog_revenue_recognition_delay_positive_high_mae_guard

- Trigger: `Stage3-Yellow`, trigger date `2024-08-29`, entry `2024-08-30` close `14,700`.
- Actual path: MFE90 `48.3%`, MAE90 `-19.18%`, MFE180 `83.67%`, MAE180 `-19.18%`.
- Calibration meaning: 수주잔고와 3~6개월 매출인식 lag가 동시에 언급된 fitting row다. 초기 MAE가 컸지만 90/180D MFE가 살아 있어 hard 4C가 아니라 Yellow+high-MAE watch가 적합하다.

### Case 7 — 013030 / 하이록코리아 / direct_report_quality_margin_positive

- Trigger: `Stage3-Green`, trigger date `2025-05-15`, entry `2025-05-16` close `27,650`.
- Actual path: MFE90 `50.09%`, MAE90 `-2.89%`, MFE180 `50.09%`, MAE180 `-2.89%`.
- Calibration meaning: 분기보고서 기반의 fittings/valves issuer route와 양호한 forward path가 만나는 positive row다. 낮은 MAE와 50% MFE가 Green 허용 표본이지만, cash bridge가 없는 동종 report row와 구분해야 한다.

### Case 8 — 014620 / 성광벤드 / business_report_yellow_with_4b_phase_watch

- Trigger: `Stage3-Yellow`, trigger date `2025-03-20`, entry `2025-03-21` close `26,300`.
- Actual path: MFE90 `40.3%`, MAE90 `-14.26%`, MFE180 `47.53%`, MAE180 `-14.26%`.
- Calibration meaning: 사업보고서 기반의 fittings/plant shipbuilding route는 존재하고 90/180D MFE도 양호하나, 30D MAE와 peak 이후 drawdown 때문에 Green보다 Yellow+local 4B-watch가 맞다.

## 12. Trigger-Level OHLC Backtest Tables

Every `row_type="trigger"` row in section 25 contains canonical `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct`.

## 13. Stage2 / Actionable Evidence Stress Test

C05 Stage2 should start only when the row shows a real issuer route. Generic sector weather or report text is not enough. `100090` demonstrates that even a large direct order can fail if cash/margin conversion is absent. `086670` shows the stricter proxy case: a broad fitting/valve route without issuer-level conversion produces a deep MAE path.

## 14. Stage3 Yellow / Green Stress Test

Yellow is appropriate when the direct route and conversion timing are visible but cash quality is not fully proven, as in `023160`, `333430`, and `014620`. Green is reserved for rows like `013030`, where the forward path, low MAE, and conversion profile support promotion. Green should not be inherited from order size alone.

## 15. Stage4B Timing Stress Test

High-MAE rows with surviving customer/order routes should be placed in local 4B-watch before hard 4C. `023160`, `333430`, and `014620` all have meaningful forward MFE but carry price-phase or post-peak risk. That makes them position-size / watch rows, not thesis-death rows.

## 16. Stage4C Thesis-Break Stress Test

Hard 4C requires non-price thesis death: cancellation, customer route death, repeated cash-flow damage, accounting/trust break, or irreversible funding failure. MAE alone is smoke, not the fire. `100090` and `086670` are counterexamples to promotion, but not permanent 4C examples unless later evidence proves route death.

## 17. Current Profile Error Taxonomy

| error_mode | symbols | repair |
|---|---|---|
| large_order_without_cash_false_positive | 100090 | Do not promote direct order headline without margin/cash bridge. |
| proxy_route_without_issuer_conversion | 086670 | Cap proxy-only supplier exposure at Stage2-watch. |
| missed_structural_direct_route | 082740, 333430 | Direct route plus strong OHLC path should not stay trapped in weak watch bucket. |
| high_mae_live_route_not_4c | 023160, 014620 | Use local 4B-watch unless non-price thesis death appears. |
| green_requires_cash_freshness | 014620 | Report/result rows after rerating cap below Green when cash freshness is incomplete. |


## 18. Sector-Specific Rule Candidate

`L1_INDUSTRIALS_INFRA_DEFENSE_GRID` supplier/order/result rows should split sector/order headline, issuer-level customer route, realized margin, working-capital/cash conversion, and price phase. Order is the pipe; margin and cash are the water. The model should reward water flow, not pipe diameter alone.

## 19. Canonical Archetype Rule Candidate

`C05_EPC_MEGA_CONTRACT_MARGIN_GAP` should use a supplier order-to-margin/cash conversion ladder:

1. source/exposure or sector backlog text -> Stage2-watch only;
2. direct customer/order route -> Stage2-Actionable;
3. margin or cost-rate proof -> Stage3-Yellow;
4. working-capital/cash conversion plus low phase risk -> Stage3-Green;
5. high MAE with live route -> local 4B-watch;
6. confirmed route death or repeated cash damage -> Stage4C.

## 20. Shadow Weight Delta Proposal

| axis | before | after | rationale | production_change |
|---|---|---|---|---|
| direct_order_bonus | high when contract headline exists | kept but gated by margin/cash freshness | 100090 shows order size alone failed | false |
| proxy_supplier_bonus | Stage2 possible | Stage2-watch cap unless direct issuer route | 086670 deep MAE path | false |
| margin_cash_freshness | implicit | explicit Yellow/Green gate | 013030 positive vs 014620 watch | false |
| high_MAE_to_4C | too aggressive if MAE-only | requires non-price thesis death | 023160 and 333430 survive after drawdown | false |


## 21. Validation Scope and Holdout Notes

The batch is a calibration sample, not a production deployment. It intentionally mixes direct contract rows, KRX report rows, KIRS/broker proxy rows, and phase-risk rows. It is suitable for C05 rule shaping but should not be used as a live screen.

## 22. Residual Learning Summary

The residual is not that C05 should become stricter everywhere. It should become more mechanical: direct route opens the gate; margin/cash conversion decides the room; price phase decides how wide the position door opens. The same headline can be a bridge, a trap, or a watch signal depending on whether water is actually moving through the pipe.

## 23. No-Repeat Update Candidate

Append after review:

```text
R1 loop 219 / C05_EPC_MEGA_CONTRACT_MARGIN_GAP / C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD / 8 trigger rows / 7 strict-new local C05 symbols / direct URL+MFE-MAE complete / no hard duplicate keys
```

## 24. Batch Ingest Self-Audit

```json
{
  "JSONL_rows": 28,
  "trigger_rows": 8,
  "score_rows": 8,
  "required_MFE_MAE_missing": 0,
  "entry_date_entry_price_missing": 0,
  "noncanonical_trigger_type": 0,
  "corporate_action_contaminated_trigger_rows": 0,
  "hard_duplicate_key_count_vs_local_C05_archive": 0,
  "production_scoring_changed": false
}
```

## 25. Machine-Readable JSONL

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_row_count": 15214118, "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "symbol_count": 5414, "tradable_columns": ["d", "o", "h", "l", "c", "v", "a", "mc", "s", "m"], "tradable_row_count": 14354401}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_001", "case_outcome": "positive", "case_role": "direct_engine_contract_margin_bridge_positive", "company_name": "한화엔진", "entry_date": "2024-02-26", "evidence_url": "https://securities.miraeasset.com/bbs/download/2125659.pdf?attachmentId=2125659", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": false, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "news_with_contract_disclosure_summary", "symbol": "082740", "trigger_date": "2024-02-23"}
{"MAE_180D_pct": -1.71, "MAE_30D_pct": -1.71, "MAE_90D_pct": -1.71, "MFE_180D_pct": 110.04, "MFE_30D_pct": 25.09, "MFE_90D_pct": 107.96, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_001", "company_name": "한화엔진", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_missed_structural_if_contract_route_capped_at_watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.9, "entry_date": "2024-02-26", "entry_ohlcv": {"c": 8170.0, "d": "2024-02-26", "h": 8210.0, "l": 8080.0, "mc": 584514430980.0, "o": 8200.0, "s": 71543994, "v": 306373}, "entry_price": 8170.0, "evidence_available_at_that_date": true, "evidence_source": "https://securities.miraeasset.com/bbs/download/2125659.pdf?attachmentId=2125659", "evidence_summary": "2024-02-23 한화오션향 선박용 엔진 공급계약 보도/공시 요약. 계약금액과 납기 가시성이 있는 direct issuer route이며, 이후 OHLC 경로가 낮은 MAE와 큰 90/180D MFE로 이어졌다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "price_phase_plus_bridge_quality", "four_b_full_window_peak_proximity": "late_peak_drawdown_watch", "four_b_local_peak_proximity": "requires_watch", "four_b_timing_verdict": "local_4b_watch_before_full_4b", "four_c_protection_label": "none", "green_lateness_ratio": 0.772, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2024-07-24", "peak_price": 17160.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/082/082740.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_082740_2024-02-26", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 16.6375, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": ["margin_cash_bridge_present_or_expected"], "stage4b_evidence": ["initial_high_mae_or_late_phase_requires_watch"], "stage4c_evidence": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "082740", "trigger_date": "2024-02-23", "trigger_id": "C05L219_TRIG_001", "trigger_outcome_label": "positive", "trigger_type": "Stage3-Yellow", "trough_date": "2024-02-27", "trough_price": 8030.0}
{"case_id": "C05L219_CASE_001", "delta_total": 13, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage3-Yellow", "raw_component_breakdown_after": {"directness": 18, "margin_cash_freshness": 21, "penalty": -5, "phase_sanity": 14, "stage2_bridge": 21, "total": 69}, "raw_component_breakdown_before": {"directness": 14, "margin_cash_freshness": 17, "penalty": -6, "phase_sanity": 13, "stage2_bridge": 18, "total": 56}, "row_type": "score_simulation", "shadow_only": true, "symbol": "082740", "trigger_id": "C05L219_TRIG_001"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_002", "case_outcome": "counterexample", "case_role": "large_order_headline_without_margin_cash_counterexample", "company_name": "SK오션플랜트", "entry_date": "2024-06-05", "evidence_url": "https://v.daum.net/v/HRQs7KiBUy", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": false, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "news_with_contract_amount", "symbol": "100090", "trigger_date": "2024-06-04"}
{"MAE_180D_pct": -33.42, "MAE_30D_pct": -14.03, "MAE_90D_pct": -33.42, "MFE_180D_pct": 4.72, "MFE_30D_pct": 4.59, "MFE_90D_pct": 4.72, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_002", "company_name": "SK오션플랜트", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive_if_large_contract_promoted_without_cash_bridge", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.42, "entry_date": "2024-06-05", "entry_ohlcv": {"c": 15470.0, "d": "2024-06-05", "h": 16180.0, "l": 14460.0, "mc": 915755436960.0, "o": 15020.0, "s": 59195568, "v": 3024498}, "entry_price": 15470.0, "evidence_available_at_that_date": true, "evidence_source": "https://v.daum.net/v/HRQs7KiBUy", "evidence_summary": "2024-06-04 해상풍력 하부구조물 대형 수주 headline은 direct order route를 제공하지만, 당시 가격경로는 90/180D MFE가 거의 없고 MAE가 깊어 margin/cash conversion 확인 전 Green 승격을 막는 반례다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "price_phase_plus_bridge_quality", "four_b_full_window_peak_proximity": "late_peak_drawdown_watch", "four_b_local_peak_proximity": "requires_watch", "four_b_timing_verdict": "local_4b_watch_before_full_4b", "four_c_protection_label": "route_absent_counterexample_watch_not_permanent_4c", "green_lateness_ratio": 0.028, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2024-09-24", "peak_price": 16200.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100090/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/100/100090.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_100090_2024-06-05", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 0.0, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": [], "stage4b_evidence": ["initial_high_mae_or_late_phase_requires_watch"], "stage4c_evidence": ["bridge_absent_and_forward_path_failed_but_not_permanent_thesis_death"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "100090", "trigger_date": "2024-06-04", "trigger_id": "C05L219_TRIG_002", "trigger_outcome_label": "counterexample", "trigger_type": "Stage2", "trough_date": "2024-08-05", "trough_price": 10300.0}
{"case_id": "C05L219_CASE_002", "delta_total": -13, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage2", "raw_component_breakdown_after": {"directness": 15, "margin_cash_freshness": 4, "penalty": -22, "phase_sanity": 5, "stage2_bridge": 17, "total": 19}, "raw_component_breakdown_before": {"directness": 16, "margin_cash_freshness": 6, "penalty": -16, "phase_sanity": 6, "stage2_bridge": 20, "total": 32}, "row_type": "score_simulation", "shadow_only": true, "symbol": "100090", "trigger_id": "C05L219_TRIG_002"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_003", "case_outcome": "counterexample", "case_role": "source_proxy_fitting_valve_counterexample", "company_name": "비엠티", "entry_date": "2024-05-28", "evidence_url": "https://w4.kirs.or.kr/download/research/240528_%EB%B9%84%EC%97%A0%ED%8B%B0.pdf", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": true, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "kirs_report_proxy", "symbol": "086670", "trigger_date": "2024-05-28"}
{"MAE_180D_pct": -47.65, "MAE_30D_pct": -9.33, "MAE_90D_pct": -31.94, "MFE_180D_pct": 7.21, "MFE_30D_pct": 7.21, "MFE_90D_pct": 7.21, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_003", "company_name": "비엠티", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive_proxy_route_without_order_conversion", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.17, "entry_date": "2024-05-28", "entry_ohlcv": {"c": 13180.0, "d": "2024-05-28", "h": 13450.0, "l": 13090.0, "mc": 120269793320.0, "o": 13390.0, "s": 9125174, "v": 34570}, "entry_price": 13180.0, "evidence_available_at_that_date": true, "evidence_source": "https://w4.kirs.or.kr/download/research/240528_%EB%B9%84%EC%97%A0%ED%8B%B0.pdf", "evidence_summary": "조선·반도체 피팅/밸브 노출은 보이지만 issuer-level order conversion이나 margin/cash bridge가 약한 proxy row다. 180D MAE가 매우 깊어 Stage2-required-bridge를 강화한다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "price_phase_plus_bridge_quality", "four_b_full_window_peak_proximity": "late_peak_drawdown_watch", "four_b_local_peak_proximity": "requires_watch", "four_b_timing_verdict": "local_4b_watch_before_full_4b", "four_c_protection_label": "route_absent_counterexample_watch_not_permanent_4c", "green_lateness_ratio": 0.0, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2024-06-05", "peak_price": 14130.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086670/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/086/086670.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_086670_2024-05-28", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 0.0, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": [], "stage4b_evidence": ["initial_high_mae_or_late_phase_requires_watch"], "stage4c_evidence": ["bridge_absent_and_forward_path_failed_but_not_permanent_thesis_death"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "086670", "trigger_date": "2024-05-28", "trigger_id": "C05L219_TRIG_003", "trigger_outcome_label": "counterexample", "trigger_type": "Stage2", "trough_date": "2024-12-09", "trough_price": 6900.0}
{"case_id": "C05L219_CASE_003", "delta_total": -15, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage2", "raw_component_breakdown_after": {"directness": 6, "margin_cash_freshness": 3, "penalty": -25, "phase_sanity": 4, "stage2_bridge": 11, "total": -1}, "raw_component_breakdown_before": {"directness": 8, "margin_cash_freshness": 5, "penalty": -18, "phase_sanity": 5, "stage2_bridge": 14, "total": 14}, "row_type": "score_simulation", "shadow_only": true, "symbol": "086670", "trigger_id": "C05L219_TRIG_003"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_004", "case_outcome": "positive", "case_role": "report_result_and_shipbuilding_equipment_positive_with_phase_watch", "company_name": "일승", "entry_date": "2025-05-16", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002665&docno=&method=searchInitInfo", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": false, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "direct_krx_quarterly_report", "symbol": "333430", "trigger_date": "2025-05-15"}
{"MAE_180D_pct": -14.44, "MAE_30D_pct": -10.53, "MAE_90D_pct": -14.44, "MFE_180D_pct": 126.49, "MFE_30D_pct": 27.25, "MFE_90D_pct": 126.49, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_004", "company_name": "일승", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_missed_structural_or_too_low_if_report_cash_bridge_ignored", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.71, "entry_date": "2025-05-16", "entry_ohlcv": {"c": 4605.0, "d": "2025-05-16", "h": 4820.0, "l": 4600.0, "mc": 141496669935.0, "o": 4705.0, "s": 30726747, "v": 230574}, "entry_price": 4605.0, "evidence_available_at_that_date": true, "evidence_source": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002665&docno=&method=searchInitInfo", "evidence_summary": "2025년 분기보고서가 조선기자재 집중과 사업구조 개편을 확인하는 row다. 90/180D MFE가 크지만 peak 이후 drawdown이 커 Green보다는 Yellow+phase watch가 더 맞다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "price_phase_plus_bridge_quality", "four_b_full_window_peak_proximity": "late_peak_drawdown_watch", "four_b_local_peak_proximity": "requires_watch", "four_b_timing_verdict": "local_4b_watch_before_full_4b", "four_c_protection_label": "not_hard_4c_if_direct_route_survives", "green_lateness_ratio": 0.785, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2025-09-11", "peak_price": 10430.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/333/333430/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/333/333430.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_333430_2025-05-16", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 0.0, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": ["margin_cash_bridge_present_or_expected"], "stage4b_evidence": ["initial_high_mae_or_late_phase_requires_watch"], "stage4c_evidence": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "333430", "trigger_date": "2025-05-15", "trigger_id": "C05L219_TRIG_004", "trigger_outcome_label": "positive", "trigger_type": "Stage3-Yellow", "trough_date": "2025-07-18", "trough_price": 3940.0}
{"case_id": "C05L219_CASE_004", "delta_total": 8, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage3-Yellow", "raw_component_breakdown_after": {"directness": 13, "margin_cash_freshness": 22, "penalty": -8, "phase_sanity": 10, "stage2_bridge": 20, "total": 57}, "raw_component_breakdown_before": {"directness": 12, "margin_cash_freshness": 18, "penalty": -8, "phase_sanity": 9, "stage2_bridge": 18, "total": 49}, "row_type": "score_simulation", "shadow_only": true, "symbol": "333430", "trigger_id": "C05L219_TRIG_004"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_005", "case_outcome": "counterexample", "case_role": "ship_pipe_report_actionable_but_not_green", "company_name": "동방선기", "entry_date": "2024-10-07", "evidence_url": "https://w4.kirs.or.kr/download/research/241004_%EB%8F%99%EB%B0%A9%EC%84%A0%EA%B8%B0.pdf", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": true, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "kirs_report_direct_business_profile", "symbol": "099410", "trigger_date": "2024-10-04"}
{"MAE_180D_pct": -10.92, "MAE_30D_pct": -6.59, "MAE_90D_pct": -10.92, "MFE_180D_pct": 41.07, "MFE_30D_pct": 13.52, "MFE_90D_pct": 22.7, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_005", "company_name": "동방선기", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct_stage2_actionable_if_kept_below_green", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.74, "entry_date": "2024-10-07", "entry_ohlcv": {"c": 2885.0, "d": "2024-10-07", "h": 2900.0, "l": 2790.0, "mc": 40390000000.0, "o": 2820.0, "s": 14000000, "v": 233688}, "entry_price": 2885.0, "evidence_available_at_that_date": true, "evidence_source": "https://w4.kirs.or.kr/download/research/241004_%EB%8F%99%EB%B0%A9%EC%84%A0%EA%B8%B0.pdf", "evidence_summary": "선박용 배관 조선기자재 route는 뚜렷하지만 직접 수주·현금전환 row는 아니다. Actionable은 가능하나 Green으로 올리기 전 margin/cash freshness가 필요하다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "none", "four_b_full_window_peak_proximity": "normal", "four_b_local_peak_proximity": "not_peak_only", "four_b_timing_verdict": "no_4b_required", "four_c_protection_label": "none", "green_lateness_ratio": 0.671, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2025-05-27", "peak_price": 4070.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099410/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/099/099410.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_099410_2024-10-07", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 0.0, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": [], "stage4b_evidence": [], "stage4c_evidence": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "099410", "trigger_date": "2024-10-04", "trigger_id": "C05L219_TRIG_005", "trigger_outcome_label": "counterexample", "trigger_type": "Stage2-Actionable", "trough_date": "2024-12-09", "trough_price": 2570.0}
{"case_id": "C05L219_CASE_005", "delta_total": 5, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage2-Actionable", "raw_component_breakdown_after": {"directness": 10, "margin_cash_freshness": 10, "penalty": -5, "phase_sanity": 13, "stage2_bridge": 17, "total": 45}, "raw_component_breakdown_before": {"directness": 9, "margin_cash_freshness": 9, "penalty": -6, "phase_sanity": 12, "stage2_bridge": 16, "total": 40}, "row_type": "score_simulation", "shadow_only": true, "symbol": "099410", "trigger_id": "C05L219_TRIG_005"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_006", "case_outcome": "positive", "case_role": "backlog_revenue_recognition_delay_positive_high_mae_guard", "company_name": "태광", "entry_date": "2024-08-30", "evidence_url": "https://stock.pstatic.net/stock-research/company/53/20240829_company_188003000.pdf", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": true, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "broker_report_with_backlog_recognition_timing", "symbol": "023160", "trigger_date": "2024-08-29"}
{"MAE_180D_pct": -19.18, "MAE_30D_pct": -13.81, "MAE_90D_pct": -19.18, "MFE_180D_pct": 83.67, "MFE_30D_pct": 2.04, "MFE_90D_pct": 48.3, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_006", "company_name": "태광", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_4C_too_early_if_initial_mae_overweighted", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.44, "entry_date": "2024-08-30", "entry_ohlcv": {"c": 14700.0, "d": "2024-08-30", "h": 14760.0, "l": 13700.0, "mc": 389550000000.0, "o": 13700.0, "s": 26500000, "v": 476218}, "entry_price": 14700.0, "evidence_available_at_that_date": true, "evidence_source": "https://stock.pstatic.net/stock-research/company/53/20240829_company_188003000.pdf", "evidence_summary": "수주잔고와 3~6개월 매출인식 lag가 동시에 언급된 fitting row다. 초기 MAE가 컸지만 90/180D MFE가 살아 있어 hard 4C가 아니라 Yellow+high-MAE watch가 적합하다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "price_phase_plus_bridge_quality", "four_b_full_window_peak_proximity": "late_peak_drawdown_watch", "four_b_local_peak_proximity": "requires_watch", "four_b_timing_verdict": "local_4b_watch_before_full_4b", "four_c_protection_label": "not_hard_4c_if_direct_route_survives", "green_lateness_ratio": 0.976, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2025-03-04", "peak_price": 27000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023160/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/023/023160.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_023160_2024-08-30", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 0.0, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": ["margin_cash_bridge_present_or_expected"], "stage4b_evidence": ["initial_high_mae_or_late_phase_requires_watch"], "stage4c_evidence": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "023160", "trigger_date": "2024-08-29", "trigger_id": "C05L219_TRIG_006", "trigger_outcome_label": "positive", "trigger_type": "Stage3-Yellow", "trough_date": "2024-10-31", "trough_price": 11880.0}
{"case_id": "C05L219_CASE_006", "delta_total": 6, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage3-Yellow", "raw_component_breakdown_after": {"directness": 10, "margin_cash_freshness": 18, "penalty": -9, "phase_sanity": 9, "stage2_bridge": 18, "total": 46}, "raw_component_breakdown_before": {"directness": 10, "margin_cash_freshness": 15, "penalty": -10, "phase_sanity": 8, "stage2_bridge": 17, "total": 40}, "row_type": "score_simulation", "shadow_only": true, "symbol": "023160", "trigger_id": "C05L219_TRIG_006"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_007", "case_outcome": "positive", "case_role": "direct_report_quality_margin_positive", "company_name": "하이록코리아", "entry_date": "2025-05-16", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515001059&docno=&method=searchInitInfo", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": false, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "direct_krx_quarterly_report", "symbol": "013030", "trigger_date": "2025-05-15"}
{"MAE_180D_pct": -2.89, "MAE_30D_pct": -2.89, "MAE_90D_pct": -2.89, "MFE_180D_pct": 50.09, "MFE_30D_pct": 16.46, "MFE_90D_pct": 50.09, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_007", "company_name": "하이록코리아", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct_or_missed_green_when_cash_bridge_visible", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.8, "entry_date": "2025-05-16", "entry_ohlcv": {"c": 27650.0, "d": "2025-05-16", "h": 27700.0, "l": 27200.0, "mc": 339968971300.0, "o": 27250.0, "s": 12295442, "v": 58338}, "entry_price": 27650.0, "evidence_available_at_that_date": true, "evidence_source": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515001059&docno=&method=searchInitInfo", "evidence_summary": "분기보고서 기반의 fittings/valves issuer route와 양호한 forward path가 만나는 positive row다. 낮은 MAE와 50% MFE가 Green 허용 표본이지만, cash bridge가 없는 동종 report row와 구분해야 한다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "none", "four_b_full_window_peak_proximity": "normal", "four_b_local_peak_proximity": "not_peak_only", "four_b_timing_verdict": "no_4b_required", "four_c_protection_label": "none", "green_lateness_ratio": 0.671, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2025-09-11", "peak_price": 41500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013030/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/013/013030.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_013030_2025-05-16", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 4.2886, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": ["margin_cash_bridge_present_or_expected"], "stage4b_evidence": [], "stage4c_evidence": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "013030", "trigger_date": "2025-05-15", "trigger_id": "C05L219_TRIG_007", "trigger_outcome_label": "positive", "trigger_type": "Stage3-Green", "trough_date": "2025-05-23", "trough_price": 26850.0}
{"case_id": "C05L219_CASE_007", "delta_total": 6, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage3-Green", "raw_component_breakdown_after": {"directness": 14, "margin_cash_freshness": 26, "penalty": -2, "phase_sanity": 16, "stage2_bridge": 20, "total": 74}, "raw_component_breakdown_before": {"directness": 13, "margin_cash_freshness": 23, "penalty": -3, "phase_sanity": 16, "stage2_bridge": 19, "total": 68}, "row_type": "score_simulation", "shadow_only": true, "symbol": "013030", "trigger_id": "C05L219_TRIG_007"}
{"calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_008", "case_outcome": "counterexample", "case_role": "business_report_yellow_with_4b_phase_watch", "company_name": "성광벤드", "entry_date": "2025-03-21", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250320001317&docno=&method=searchInitInfo", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "proxy_only": false, "reuse_reason": "none", "round": "R1", "row_type": "case", "source_quality": "direct_krx_business_report", "symbol": "014620", "trigger_date": "2025-03-20"}
{"MAE_180D_pct": -14.26, "MAE_30D_pct": -14.26, "MAE_90D_pct": -14.26, "MFE_180D_pct": 47.53, "MFE_30D_pct": 12.17, "MFE_90D_pct": 40.3, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05L219_CASE_008", "company_name": "성광벤드", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_green_if_report_result_lifted_without_phase_cap", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.02, "entry_date": "2025-03-21", "entry_ohlcv": {"c": 26300.0, "d": "2025-03-21", "h": 26600.0, "l": 25350.0, "mc": 734520786100.0, "o": 25400.0, "s": 27928547, "v": 377001}, "entry_price": 26300.0, "evidence_available_at_that_date": true, "evidence_source": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250320001317&docno=&method=searchInitInfo", "evidence_summary": "사업보고서 기반의 fittings/plant shipbuilding route는 존재하고 90/180D MFE도 양호하나, 30D MAE와 peak 이후 drawdown 때문에 Green보다 Yellow+local 4B-watch가 맞다.", "fine_archetype_id": "C05_SUPPLIER_ORDER_TO_MARGIN_CASH_CONVERSION_AND_PHASE_GUARD", "forward_window_trading_days": 180, "four_b_evidence_type": "price_phase_plus_bridge_quality", "four_b_full_window_peak_proximity": "late_peak_drawdown_watch", "four_b_local_peak_proximity": "requires_watch", "four_b_timing_verdict": "local_4b_watch_before_full_4b", "four_c_protection_label": "not_hard_4c_if_direct_route_survives", "green_lateness_ratio": 0.744, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 219, "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "peak_date": "2025-09-11", "peak_price": 38800.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014620/<year>.csv", "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "profile_path": "atlas/symbol_profiles/014/014620.json", "reuse_reason": "none_under_selected_C05_hard_key", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C05_L219_014620_2025-03-21", "sector": "L1 shipbuilding/EPC supplier/order-margin-cash conversion", "share_change_pct_max_180D": 4.9096, "stage2_evidence": ["issuer_or_supplier_route_exists", "order_backlog_or_report_evidence_available"], "stage3_evidence": ["margin_cash_bridge_present_or_expected"], "stage4b_evidence": ["initial_high_mae_or_late_phase_requires_watch"], "stage4c_evidence": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "014620", "trigger_date": "2025-03-20", "trigger_id": "C05L219_TRIG_008", "trigger_outcome_label": "counterexample", "trigger_type": "Stage3-Yellow", "trough_date": "2025-04-07", "trough_price": 22550.0}
{"case_id": "C05L219_CASE_008", "delta_total": 5, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "proposed_stage_after": "Stage3-Yellow", "raw_component_breakdown_after": {"directness": 13, "margin_cash_freshness": 19, "penalty": -8, "phase_sanity": 10, "stage2_bridge": 19, "total": 53}, "raw_component_breakdown_before": {"directness": 13, "margin_cash_freshness": 17, "penalty": -9, "phase_sanity": 9, "stage2_bridge": 18, "total": 48}, "row_type": "score_simulation", "shadow_only": true, "symbol": "014620", "trigger_id": "C05L219_TRIG_008"}
{"calibration_usable_case_count": 8, "counterexample_count": 4, "current_profile_error_count": 6, "main_error_modes": ["large_order_without_margin_cash_false_positive", "proxy_route_without_issuer_conversion", "high_mae_live_route_should_be_watch_not_4c", "report_only_green_trap"], "positive_case_count": 4, "production_scoring_changed": false, "profile_after": "c05_shadow_margin_cash_conversion_ladder", "profile_before": "e2r_2_2_rolling_calibrated_proxy", "row_type": "profile_aggregate_comparison"}
{"after_weight": "stage2_required_bridge_plus_margin_cash_freshness_gate", "before_weight": "implicit_order_backlog_stage2_bonus", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "implementation_target": "coding_agent_future_patch_only_after_review", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "production_scoring_changed": false, "row_type": "shadow_weight_proposal", "rule_axis": "c05_supplier_order_to_margin_cash_conversion_ladder"}
{"canonical_archetype_rule_candidate": "C05 should use a supplier order-to-margin/cash ladder: direct route -> margin/cost proof -> working-capital/cash conversion -> persistence/phase sanity. High MAE with a live route is 4B-watch, not hard 4C.", "loop": 219, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "c05_supplier_order_to_margin_cash_conversion_and_phase_guard", "production_scoring_changed": false, "row_type": "residual_contribution", "sector_specific_rule_candidate": "L1 supplier/order/result rows should split sector/order headline, issuer-level customer route, realized margin, working-capital/cash conversion, and price phase."}
```

## 26. Human Reviewer Checklist

- Verify that each evidence URL is not merely thematic when the row is promoted above Stage2.
- Confirm that margin/cash freshness is explicitly available for Yellow/Green rows.
- Keep proxy-only rows below Green unless a later direct conversion source is added.
- Treat high MAE with live customer route as local 4B-watch, not hard 4C.

## 27. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring automatically. Review this MD as a C05 shadow calibration sample. If accepted, add a C05 supplier_order_to_margin_cash_conversion_ladder that: (1) caps proxy-only supplier exposure at Stage2-watch; (2) requires margin/cash freshness for Yellow/Green; (3) routes high-MAE live-route rows to local 4B-watch rather than hard 4C; and (4) treats direct order headlines without cash conversion as false-positive risk. Preserve existing hard gates for MFE/MAE completeness and actual Stock-Web OHLC rows.
```

## 28. Final Artifact Summary

```text
new_independent_case_count = 8
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 8
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
positive_case_count = 4
counterexample_count = 4
current_profile_error_count = 6
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c05_supplier_order_to_margin_cash_conversion_and_phase_guard
existing_axis_strengthened = stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_qualified_for_high_mae_live_contract_route_only
next_recommended_archetypes = C01 direct backlog-to-FCF rows; C13 strict-new utilization/ex-credit rows; C10 strict-new order-conversion rows; C15 spread freshness rows; C31 non-semi/battery awarded-cashflow rows; R13 only for genuinely new taxonomy compression
```
