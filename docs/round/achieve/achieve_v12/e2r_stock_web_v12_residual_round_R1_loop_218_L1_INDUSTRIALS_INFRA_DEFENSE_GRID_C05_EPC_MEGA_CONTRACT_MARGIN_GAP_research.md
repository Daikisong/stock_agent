# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R1
selected_loop = 218
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C05 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status = coverage_index_selected; local C05 max loop 217 -> selected loop 218; 직전 C31 loop 221 반복 회피
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD
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
output_file = e2r_stock_web_v12_residual_round_R1_loop_218_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

This loop adds 8 new independent cases, 4 counterexamples, and 6 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP. It intentionally avoids the previous user-visible C31 policy run and avoids the existing local C05 hard duplicate keys.

## 1. Current Calibrated Profile Assumption

The stress-test reference is the post-calibrated E2R profile family. For this MD the current proxy is `e2r_2_2_rolling_calibrated_proxy`, with rollback comparison to `e2r_2_0_baseline_reference`. No production scoring is changed here. The exercise is a shadow-only C05 rule proposal.

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
- fine_archetype_id: `C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD`
- valid mapping: C01~C05 -> R1 / L1

Scope boundary: this is not a live candidate scan and not an investment recommendation. It is an historical trigger-level calibration file using only already-observed historical evidence and Stock-Web OHLC paths.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C05 as a Priority 1 quality target: margin / working-capital failure counterexamples and 4C timing reinforcement. Local C05 files through loop 217 were checked. The hard key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All eight representative trigger rows in this loop are new hard keys under C05. The file also uses seven strict-new symbols versus the local C05 archive, moving away from the already dense C05 construction/shipbuilding top-set and into supplier / engine / insulation / module rows.

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
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year"
}
```

The entry OHLC row is the `c` column close on the first tradable row at or after `trigger_date`, unless the event timing requires next-trading-day entry. MFE/MAE are calculated by the Stock-Web schema rule: max high and min low from entry row through 30/90/180 tradable rows.

## 5. Historical Eligibility Gate

All representative trigger rows pass:

- past historical trigger date
- actual entry row exists in tradable shard
- 180 forward tradable rows available before manifest max date `2026-02-20`
- positive OHLCV values
- 30D / 90D / 180D MFE and MAE present
- 180D corporate-action contamination screen clean

## 6. Canonical Archetype Compression Map

C05 is compressed as:

```text
order/backlog/result headline
  -> direct issuer route
  -> realized margin bridge
  -> working-capital/cash conversion
  -> persistence and price-phase sanity
```

In human terms, the order is the pipe. Margin and cash are the water. A beautiful pipe with no water should not get Green.

## 7. Case Selection Summary

| # | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | role | current_profile_verdict |
|---:|---|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 017960 | 한국카본 | Stage2 | 2024-05-16 | 2024-05-16 | 11,610 | 1.38 / -11.2 | 14.99 / -11.89 | 28.68 / -19.04 | margin_cash_false_positive | current_profile_false_positive |
| 2 | 033500 | 동성화인텍 | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 13,230 | 1.97 / -11.41 | 8.69 / -18.37 | 69.69 / -19.43 | delayed_margin_conversion_high_mae | current_profile_false_positive |
| 3 | 103230 | 에스앤더블류 | Stage2 | 2024-05-16 | 2024-05-16 | 4,735 | 2.85 / -16.16 | 2.85 / -31.36 | 2.85 / -47.2 | text_backlog_false_positive | current_profile_false_positive |
| 4 | 108380 | 대양전기공업 | Stage2 | 2024-06-11 | 2024-06-11 | 16,490 | 2.24 / -22.68 | 2.24 / -34.81 | 26.74 / -34.81 | source_proxy_false_positive_high_mae | current_profile_false_positive |
| 5 | 014940 | 오리엔탈정공 | Stage3-Yellow | 2024-11-19 | 2024-11-19 | 4,445 | 37.68 / -7.54 | 44.88 / -7.54 | 86.95 / -7.54 | margin_bridge_positive | current_profile_correct |
| 6 | 071970 | HD현대마린엔진 | Stage3-Yellow | 2025-04-10 | 2025-04-10 | 28,150 | 52.4 / -3.73 | 203.91 / -3.73 | 278.69 / -3.73 | direct_order_margin_bridge_positive | current_profile_missed_structural |
| 7 | 075580 | 세진중공업 | Stage3-Yellow | 2025-05-21 | 2025-05-21 | 12,030 | 7.65 / -20.2 | 127.76 / -20.2 | 127.76 / -20.2 | positive_high_mae_absorption_guard | current_profile_4C_too_early_if_mae_only_or_false_green_if_mae_ignored |
| 8 | 017960 | 한국카본 | Stage3-Yellow | 2025-05-16 | 2025-05-16 | 20,400 | 31.62 / -3.33 | 75.74 / -3.33 | 100.74 / -3.33 | result_order_conversion_positive | current_profile_correct |


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

Positive rows are not allowed to become unconditional Green. Counterexamples are not allowed to become automatic hard 4C. The useful calibration edge is the middle door: Stage2/Yellow with 4B-watch when the route survives but price phase or cash conversion is not yet clean.

## 9. Evidence Source Map

| # | symbol | source_quality | proxy_only | evidence_url | evidence_summary |
|---:|---|---|---:|---|---|
| 1 | 017960 | direct_krx_quarterly_report | false | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000945&docno=&method=search&viewerhost= | 분기보고서에서 LNG 운반선 보냉재 핵심자재 내재화와 조선 value-chain 노출은 확인되지만, 해당 시점에는 issuer-level margin/working-capital cash 전환 수치가 약했다. 90D 이후 일부 회복은 있었으나 180D MAE가 깊어 Stage2-watch가 더 맞다. |
| 2 | 033500 | broker_report_customer_backlog_detail | true | https://stock.pstatic.net/stock-research/company/79/20240517_company_303092000.pdf | LNG 보냉재 수주잔고와 대형 조선소 고객 품질은 보이지만, 이 trigger 시점에는 cash conversion 확인 전이었다. 뒤늦은 180D MFE는 생겼지만 30/90D가 먼저 눌려 Green 승격에는 phase penalty가 필요하다. |
| 3 | 103230 | direct_krx_quarterly_report | false | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000245&docno=&method=search&viewerhost= | 선박 디젤엔진 부품 exposure와 수주 성장 문맥은 있으나 issuer-level margin/cash 전환 근거가 약했다. 가격경로도 180D MFE가 거의 없이 큰 MAE를 남겨 report-text만으로 Actionable bonus를 주면 오류가 커진다. |
| 4 | 108380 | source_proxy_only | true | https://w4.kirs.or.kr/download/research/240611_%EB%8C%80%EC%96%91%EC%A0%84%EA%B8%B0%EA%B3%B5%EC%97%85.pdf | 조선 업황과 선박조명 공급망 연결은 보이지만 top-down backlog proxy 중심이며, issuer cash bridge가 약했다. 90D MAE가 매우 깊고 180D MFE도 뒤늦게 나온 구조라 Stage2-required-bridge를 강화하는 counterexample이다. |
| 5 | 014940 | news_with_direct_result_and_backlog_context | false | https://www.etoday.co.kr/news/view/2420784 | 오리엔탈정공은 수주잔고 가시성과 영업 실적 지속성이 함께 확인되며 수주 headline이 margin result로 넘어가는 다리가 생긴 표본이다. 90/180D MFE와 낮은 MAE가 Yellow를 뒷받침한다. |
| 6 | 071970 | news_with_issuer_result_backlog_and_group_contracts | true | https://m.thebell.co.kr/m/newsview.asp?newskey=202504041340456880102780 | 그룹 조선 수주 흐름, 엔진 수주잔고, 실적 margin bridge가 같은 구간에 붙은 표본이다. 직접 route와 result bridge가 함께 있으므로 Stage2를 넘어 Yellow까지 허용하는 것이 맞다. |
| 7 | 075580 | broker_report_q1_result_and_margin_bridge | true | https://www.ibks.com/company/common/download.jsp?filename=20250521042305033_ko.pdf&filepath=%2Ffiles%2Ftradeinfo%2Fbusreport | 탱크·블록 route와 1Q result margin bridge가 붙었지만 당일 저가가 깊어 MAE가 먼저 찍혔다. 이후 90/180D MFE가 컸으므로 hard 4C가 아니라 Yellow+high-MAE watch가 맞는 표본이다. |
| 8 | 017960 | news_with_result_and_order_outlook | false | https://marketin.edaily.co.kr/News/ReadE?newsId=02217286642169576 | 2025년 1Q에는 이전의 텍스트/내재화 단계와 달리 결과와 수주전망이 같이 움직이며 margin conversion이 가격경로로 확인됐다. 같은 symbol이라도 2024년 Stage2-watch와 2025년 Yellow를 분리해야 한다. |


## 10. Price Data Source Map

| symbol | entry OHLCV row | 30D | 90D | 180D | peak/trough/drawdown | corporate-action screen |
|---|---|---:|---:|---:|---|---|
| 017960 | 2024-05-16 O=11,770 H=11,770 L=11,530 C=11,610 V=191,402 | 1.38 / -11.2 | 14.99 / -11.89 | 28.68 / -19.04 | peak 2025-01-22 14,940; trough 2024-12-09 9,400; DD -12.58% | shares Δ max 0.0%; clean_180D_window |
| 033500 | 2024-05-16 O=13,410 H=13,490 L=13,180 C=13,230 V=188,930 | 1.97 / -11.41 | 8.69 / -18.37 | 69.69 / -19.43 | peak 2025-01-22 22,450; trough 2024-10-31 10,660; DD -12.87% | shares Δ max 0.0%; clean_180D_window |
| 103230 | 2024-05-16 O=4,845 H=4,870 L=4,660 C=4,735 V=74,273 | 2.85 / -16.16 | 2.85 / -31.36 | 2.85 / -47.2 | peak 2024-05-16 4,870; trough 2024-12-09 2,500; DD -48.67% | shares Δ max 0.0%; clean_180D_window |
| 108380 | 2024-06-11 O=16,700 H=16,860 L=16,000 C=16,490 V=481,894 | 2.24 / -22.68 | 2.24 / -34.81 | 26.74 / -34.81 | peak 2025-03-07 20,900; trough 2024-09-09 10,750; DD -14.59% | shares Δ max 0.0%; clean_180D_window |
| 014940 | 2024-11-19 O=4,575 H=4,750 L=4,440 C=4,445 V=2,971,752 | 37.68 / -7.54 | 44.88 / -7.54 | 86.95 / -7.54 | peak 2025-08-08 8,310; trough 2024-12-06 4,110; DD -18.41% | shares Δ max 0.0%; clean_180D_window |
| 071970 | 2025-04-10 O=27,850 H=28,300 L=27,100 C=28,150 V=519,019 | 52.4 / -3.73 | 203.91 / -3.73 | 278.69 / -3.73 | peak 2025-11-03 106,600; trough 2025-04-10 27,100; DD -30.96% | shares Δ max 0.0%; clean_180D_window |
| 075580 | 2025-05-21 O=9,680 H=12,030 L=9,600 C=12,030 V=13,354,919 | 7.65 / -20.2 | 127.76 / -20.2 | 127.76 / -20.2 | peak 2025-09-10 27,400; trough 2025-05-21 9,600; DD -38.87% | shares Δ max 0.0%; clean_180D_window |
| 017960 | 2025-05-16 O=21,850 H=21,900 L=19,720 C=20,400 V=1,299,001 | 31.62 / -3.33 | 75.74 / -3.33 | 100.74 / -3.33 | peak 2026-01-12 40,950; trough 2025-05-16 19,720; DD -21.98% | shares Δ max 0.0%; clean_180D_window |


## 11. Case-by-Case Trigger Grid

### Case 1 — 017960 / 한국카본 / 2024 report text without cash bridge

- Trigger: Stage2, 2024-05-16.
- Actual result: MFE90 `14.99%`, MAE90 `-11.89%`, MFE180 `28.68%`, MAE180 `-19.04%`.
- Calibration meaning: internalization and value-chain text is a weak bridge unless margin/cash conversion is present.

### Case 2 — 033500 / 동성화인텍 / backlog but delayed conversion

- Trigger: Stage2-Actionable, 2024-05-16.
- Actual result: MFE90 `8.69%`, MAE90 `-18.37%`, MFE180 `69.69%`, MAE180 `-19.43%`.
- Calibration meaning: customer/backlog quality is enough for Actionable, not enough for Yellow/Green before cash conversion.

### Case 3 — 103230 / 에스앤더블유 / report text false positive

- Trigger: Stage2, 2024-05-16.
- Actual result: MFE180 `2.85%`, MAE180 `-47.2%`.
- Calibration meaning: official report text proves existence of exposure, not conversion.

### Case 4 — 108380 / 대양전기공업 / top-down shipyard proxy

- Trigger: Stage2, 2024-06-11.
- Actual result: MFE90 `2.24%`, MAE90 `-34.81%`.
- Calibration meaning: broad sector weather needs issuer-level water-flow proof.

### Case 5 — 014940 / 오리엔탈정공 / backlog plus result persistence

- Trigger: Stage3-Yellow, 2024-11-19.
- Actual result: MFE90 `44.88%`, MAE90 `-7.54%`, MFE180 `86.95%`.
- Calibration meaning: direct result + backlog route justifies Yellow.

### Case 6 — 071970 / HD현대마린엔진 / direct engine route and margin bridge

- Trigger: Stage3-Yellow, 2025-04-10.
- Actual result: MFE90 `203.91%`, MAE90 `-3.73%`.
- Calibration meaning: direct group/customer route plus result bridge was under-promoted by a pure Stage2 cap.

### Case 7 — 075580 / 세진중공업 / high-MAE but surviving route

- Trigger: Stage3-Yellow, 2025-05-21.
- Actual result: MFE90 `127.76%`, MAE90 `-20.2%`.
- Calibration meaning: high MAE alone must not force hard 4C when the contract/customer route survives.

### Case 8 — 017960 / 한국카본 / 2025 result/order conversion

- Trigger: Stage3-Yellow, 2025-05-16.
- Actual result: MFE90 `75.74%`, MAE90 `-3.33%`, MFE180 `100.74%`.
- Calibration meaning: same symbol, different phase. The 2025 row has water in the pipe; the 2024 row mostly had pipe description.

## 12. Trigger-Level OHLC Backtest Tables

See the tables above and the JSONL rows in section 25. Every `row_type="trigger"` row contains canonical `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct`.

## 13. Current Calibrated Profile Stress Test

1. Current profile likely promotes direct backlog/order text more generously than this C05 supplier subset deserves.
2. The error is most visible in 103230 and 108380, where evidence exists but issuer-level cash conversion does not.
3. Stage2 bonus is useful for 033500, 014940, 071970, and 017960-2025, but too strong for 017960-2024, 103230, and 108380.
4. Yellow threshold is acceptable if margin/cash bridge is explicit.
5. Green threshold remains appropriately strict; this loop argues for an additional C05 cap, not looser Green.
6. Price-only blowoff guard remains useful.
7. Full 4B non-price requirement remains useful.
8. Hard 4C routing should be qualified: high MAE with live customer route is watch, not thesis death.

## 14. Stage2 / Yellow / Green Comparison

- Stage2-watch: sector/exposure/report text without direct margin/cash bridge.
- Stage2-Actionable: direct customer/backlog route, but cash conversion pending.
- Stage3-Yellow: direct route plus realized result/margin bridge.
- Stage3-Green: requires persistence and working-capital/cash freshness. None of these rows need unconditional Green.

## 15. 4B Local vs Full-window Timing Audit

Rows 1, 2, 4, and 7 show why local 4B-watch and hard 4C must remain different doors. A local drawdown or early MAE is a smoke alarm. It is not the fire itself unless the issuer route breaks.

## 16. 4C Protection Audit

- hard 4C success: none.
- thesis-break watch only: 017960-2024, 033500-2024, 103230-2024, 108380-2024, 075580-2025.
- false hard 4C risk: 075580-2025. MAE was deep but the 90/180D payoff says the route was not dead.

## 17. Sector-Specific Rule Candidate

`L1` shipbuilding-supplier and engineering rows should split sector backlog weather, issuer-level direct route, realized margin, working-capital/cash conversion, and price phase. Sector backlog opens the factory gate; issuer cashflow proves the goods moved through it.

## 18. Canonical-Archetype Rule Candidate

`C05` should use a supplier margin/cash conversion ladder:

```text
source/exposure text -> direct order/customer route -> margin bridge -> working-capital/cash conversion -> persistence/phase sanity
```

Source-proxy and report-text rows are capped below Green. Direct result bridge rows can reach Yellow. High-MAE rows with a live route are 4B-watch, not hard 4C.

## 19. Before / After Backtest Comparison

| profile | scope | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_2_rolling_calibrated_proxy | current_proxy | 60.13 | -16.4 | 90.26 | -19.41 | 0.75 | mixed; source-proxy/order-text rows remain too easy to promote while direct result+cash bridge rows are under-separated |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 60.13 | -16.4 | 90.26 | -19.41 | 0.625 | weaker; confirms current global profile should not be rolled back |
| P1_L1_supplier_result_cash_bridge_shadow | sector_specific | 60.13 | -16.4 | 90.26 | -19.41 | 0.25 | improves separation of text/proxy counterexamples from actual result bridge positives |
| P2_C05_margin_cash_conversion_ladder_shadow | canonical_archetype_specific | 60.13 | -16.4 | 90.26 | -19.41 | 0.125 | best; caps weak proxy rows while keeping four direct bridge positives |
| P3_high_MAE_live_contract_route_guard | counterexample_guard | 60.13 | -16.4 | 90.26 | -19.41 | 0.25 | keeps 075580 as absorbable high-MAE positive instead of wrong hard 4C |


## 20. Score-Return Alignment Matrix

- Best alignment: `P2_C05_margin_cash_conversion_ladder_shadow`.
- Main false-positive reduction: source-proxy rows no longer inherit the same evidence strength as direct result/cash bridge rows.
- Main missed-structural repair: 071970 gets Yellow instead of being stuck at generic Stage2.
- Main 4C repair: 075580 is not killed by MAE alone.

## 21. Coverage Matrix

| metric | value |
|---|---:|
| new_independent_case_count | 8 |
| reused_case_count | 0 |
| new_symbol_count | 7 |
| same_archetype_new_symbol_count | 7 |
| same_archetype_new_trigger_family_count | 8 |
| positive_case_count | 4 |
| counterexample_count | 4 |
| current_profile_error_count | 6 |
| direct URL or direct news rows | 4 |
| source_proxy_only rows | 4 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: source_proxy_stage2_false_positive; order_text_without_cash_conversion; delayed_margin_conversion_high_MAE; missed_direct_result_bridge; high_MAE_live_route_not_hard4C
new_axis_proposed: c05_shipbuilding_supplier_margin_cash_conversion_ladder; c05_source_proxy_contract_stage_cap; c05_high_mae_live_contract_route_watch_guard
existing_axis_strengthened: stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_qualified_for_high_mae_live_contract_route_only
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L1 supplier/order rows need issuer-level cashflow bridge before Yellow/Green.
canonical_archetype_rule_candidate: C05 needs a supplier margin/cash conversion ladder.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- historical trigger rows
- actual Stock-Web entry OHLC rows
- 30D/90D/180D MFE/MAE
- clean 180D corporate-action screen
- duplicate key avoidance under selected C05

Not validated:

- live candidate quality
- current price recommendations
- trading execution
- production scoring patch
- non-Stock-Web adjusted-price path

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_supplier_margin_cash_conversion_ladder,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,headline_can_promote_if_visibility_high,headline_to_route_to_margin_to_cash_to_phase_sanity,shadow_only_rule_addition,"Order/backlog/result headline separated from actual cash conversion","avg_MFE90=60.13; avg_MAE90=-16.4; P2 false_positive_rate=0.125","C05_R1L218_TRG001_017960_20240516_Stage2|C05_R1L218_TRG002_033500_20240516_Stage2Actionable|C05_R1L218_TRG003_103230_20240516_Stage2|C05_R1L218_TRG004_108380_20240611_Stage2|C05_R1L218_TRG005_014940_20241119_Stage3Yellow|C05_R1L218_TRG006_071970_20250410_Stage3Yellow|C05_R1L218_TRG007_075580_20250521_Stage3Yellow|C05_R1L218_TRG008_017960_20250516_Stage3Yellow",8,8,4,medium,canonical_shadow_only,"production_scoring_changed=false"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414}
{"row_type":"case","case_id":"C05_R1L218_CASE001_017960_20240516","symbol":"017960","company_name":"한국카본","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"margin_cash_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"분기보고서에서 LNG 운반선 보냉재 핵심자재 내재화와 조선 value-chain 노출은 확인되지만, 해당 시점에는 issuer-level margin/working-capital cash 전환 수치가 약했다. 90D 이후 일부 회복은 있었으나 180D MAE가 깊어 Stage2-watch가 더 맞다."}
{"row_type":"case","case_id":"C05_R1L218_CASE002_033500_20240516","symbol":"033500","company_name":"동성화인텍","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"delayed_margin_conversion_high_mae","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"LNG 보냉재 수주잔고와 대형 조선소 고객 품질은 보이지만, 이 trigger 시점에는 cash conversion 확인 전이었다. 뒤늦은 180D MFE는 생겼지만 30/90D가 먼저 눌려 Green 승격에는 phase penalty가 필요하다."}
{"row_type":"case","case_id":"C05_R1L218_CASE003_103230_20240516","symbol":"103230","company_name":"에스앤더블류","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"text_backlog_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"선박 디젤엔진 부품 exposure와 수주 성장 문맥은 있으나 issuer-level margin/cash 전환 근거가 약했다. 가격경로도 180D MFE가 거의 없이 큰 MAE를 남겨 report-text만으로 Actionable bonus를 주면 오류가 커진다."}
{"row_type":"case","case_id":"C05_R1L218_CASE004_108380_20240611","symbol":"108380","company_name":"대양전기공업","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"source_proxy_false_positive_high_mae","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"조선 업황과 선박조명 공급망 연결은 보이지만 top-down backlog proxy 중심이며, issuer cash bridge가 약했다. 90D MAE가 매우 깊고 180D MFE도 뒤늦게 나온 구조라 Stage2-required-bridge를 강화하는 counterexample이다."}
{"row_type":"case","case_id":"C05_R1L218_CASE005_014940_20241119","symbol":"014940","company_name":"오리엔탈정공","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"margin_bridge_positive","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"오리엔탈정공은 수주잔고 가시성과 영업 실적 지속성이 함께 확인되며 수주 headline이 margin result로 넘어가는 다리가 생긴 표본이다. 90/180D MFE와 낮은 MAE가 Yellow를 뒷받침한다."}
{"row_type":"case","case_id":"C05_R1L218_CASE006_071970_20250410","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"direct_order_margin_bridge_positive","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_missed_structural","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"그룹 조선 수주 흐름, 엔진 수주잔고, 실적 margin bridge가 같은 구간에 붙은 표본이다. 직접 route와 result bridge가 함께 있으므로 Stage2를 넘어 Yellow까지 허용하는 것이 맞다."}
{"row_type":"case","case_id":"C05_R1L218_CASE007_075580_20250521","symbol":"075580","company_name":"세진중공업","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"positive_high_mae_absorption_guard","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_4C_too_early_if_mae_only_or_false_green_if_mae_ignored","current_profile_verdict":"current_profile_4C_too_early_if_mae_only_or_false_green_if_mae_ignored","price_source":"Songdaiki/stock-web","notes":"탱크·블록 route와 1Q result margin bridge가 붙었지만 당일 저가가 깊어 MAE가 먼저 찍혔다. 이후 90/180D MFE가 컸으므로 hard 4C가 아니라 Yellow+high-MAE watch가 맞는 표본이다."}
{"row_type":"case","case_id":"C05_R1L218_CASE008_017960_20250516","symbol":"017960","company_name":"한국카본","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","case_type":"result_order_conversion_positive","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2025년 1Q에는 이전의 텍스트/내재화 단계와 달리 결과와 수주전망이 같이 움직이며 margin conversion이 가격경로로 확인됐다. 같은 symbol이라도 2024년 Stage2-watch와 2025년 Yellow를 분리해야 한다."}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG001_017960_20240516_Stage2","case_id":"C05_R1L218_CASE001_017960_20240516","symbol":"017960","company_name":"한국카본","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":11610.0,"evidence_available_at_that_date":"분기보고서에서 LNG 운반선 보냉재 핵심자재 내재화와 조선 value-chain 노출은 확인되지만, 해당 시점에는 issuer-level margin/working-capital cash 전환 수치가 약했다. 90D 이후 일부 회복은 있었으나 180D MAE가 깊어 Stage2-watch가 더 맞다.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000945&docno=&method=search&viewerhost=","evidence_source_quality":"direct_krx_quarterly_report","source_proxy_only":false,"stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","source_quality_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017960/2024.csv","profile_path":"atlas/symbol_profiles/017/017960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2024-05-16","o":11770.0,"h":11770.0,"l":11530.0,"c":11610.0,"v":191402,"a":2221484480,"mc":602657127720,"s":51908452,"m":"KOSPI"},"MFE_30D_pct":1.38,"MFE_90D_pct":14.99,"MFE_180D_pct":28.68,"MFE_1Y_pct":93.8,"MFE_2Y_pct":null,"MAE_30D_pct":-11.2,"MAE_90D_pct":-11.89,"MAE_180D_pct":-19.04,"MAE_1Y_pct":-19.04,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-22","peak_price":14940.0,"low_date":"2024-12-09","low_price":9400.0,"drawdown_after_peak_pct":-12.58,"green_lateness_ratio":null,"four_b_local_peak_proximity":"watch_only","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_not_full_4b","four_b_evidence_type":["margin_or_backlog_slowdown","source_quality_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"margin_cash_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE001_017960_20240516_2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG002_033500_20240516_Stage2Actionable","case_id":"C05_R1L218_CASE002_033500_20240516","symbol":"033500","company_name":"동성화인텍","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":13230.0,"evidence_available_at_that_date":"LNG 보냉재 수주잔고와 대형 조선소 고객 품질은 보이지만, 이 trigger 시점에는 cash conversion 확인 전이었다. 뒤늦은 180D MFE는 생겼지만 30/90D가 먼저 눌려 Green 승격에는 phase penalty가 필요하다.","evidence_source":"https://stock.pstatic.net/stock-research/company/79/20240517_company_303092000.pdf","evidence_source_quality":"broker_report_customer_backlog_detail","source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["source_proxy_cap","high_MAE_or_delayed_conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033500/2024.csv","profile_path":"atlas/symbol_profiles/033/033500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2024-05-16","o":13410.0,"h":13490.0,"l":13180.0,"c":13230.0,"v":188930,"a":2508236250,"mc":396761005620,"s":29989494,"m":"KOSDAQ"},"MFE_30D_pct":1.97,"MFE_90D_pct":8.69,"MFE_180D_pct":69.69,"MFE_1Y_pct":105.97,"MFE_2Y_pct":null,"MAE_30D_pct":-11.41,"MAE_90D_pct":-18.37,"MAE_180D_pct":-19.43,"MAE_1Y_pct":-19.43,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-22","peak_price":22450.0,"low_date":"2024-10-31","low_price":10660.0,"drawdown_after_peak_pct":-12.87,"green_lateness_ratio":null,"four_b_local_peak_proximity":"watch_only","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_not_full_4b","four_b_evidence_type":["source_proxy_cap","high_MAE_or_delayed_conversion"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"delayed_margin_conversion_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE002_033500_20240516_2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG003_103230_20240516_Stage2","case_id":"C05_R1L218_CASE003_103230_20240516","symbol":"103230","company_name":"에스앤더블류","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":4735.0,"evidence_available_at_that_date":"선박 디젤엔진 부품 exposure와 수주 성장 문맥은 있으나 issuer-level margin/cash 전환 근거가 약했다. 가격경로도 180D MFE가 거의 없이 큰 MAE를 남겨 report-text만으로 Actionable bonus를 주면 오류가 커진다.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000245&docno=&method=search&viewerhost=","evidence_source_quality":"direct_krx_quarterly_report","source_proxy_only":false,"stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","source_quality_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103230/2024.csv","profile_path":"atlas/symbol_profiles/103/103230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2024-05-16","o":4845.0,"h":4870.0,"l":4660.0,"c":4735.0,"v":74273,"a":352098730,"mc":34092000000,"s":7200000,"m":"KOSDAQ"},"MFE_30D_pct":2.85,"MFE_90D_pct":2.85,"MFE_180D_pct":2.85,"MFE_1Y_pct":2.85,"MFE_2Y_pct":null,"MAE_30D_pct":-16.16,"MAE_90D_pct":-31.36,"MAE_180D_pct":-47.2,"MAE_1Y_pct":-47.2,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":4870.0,"low_date":"2024-12-09","low_price":2500.0,"drawdown_after_peak_pct":-48.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":"watch_only","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_not_full_4b","four_b_evidence_type":["margin_or_backlog_slowdown","source_quality_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"text_backlog_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE003_103230_20240516_2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG004_108380_20240611_Stage2","case_id":"C05_R1L218_CASE004_108380_20240611","symbol":"108380","company_name":"대양전기공업","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":16490.0,"evidence_available_at_that_date":"조선 업황과 선박조명 공급망 연결은 보이지만 top-down backlog proxy 중심이며, issuer cash bridge가 약했다. 90D MAE가 매우 깊고 180D MFE도 뒤늦게 나온 구조라 Stage2-required-bridge를 강화하는 counterexample이다.","evidence_source":"https://w4.kirs.or.kr/download/research/240611_%EB%8C%80%EC%96%91%EC%A0%84%EA%B8%B0%EA%B3%B5%EC%97%85.pdf","evidence_source_quality":"source_proxy_only","source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["source_proxy_cap","high_MAE_or_delayed_conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/108/108380/2024.csv","profile_path":"atlas/symbol_profiles/108/108380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2024-06-11","o":16700.0,"h":16860.0,"l":16000.0,"c":16490.0,"v":481894,"a":7908826150,"mc":157765321170,"s":9567333,"m":"KOSDAQ"},"MFE_30D_pct":2.24,"MFE_90D_pct":2.24,"MFE_180D_pct":26.74,"MFE_1Y_pct":44.33,"MFE_2Y_pct":null,"MAE_30D_pct":-22.68,"MAE_90D_pct":-34.81,"MAE_180D_pct":-34.81,"MAE_1Y_pct":-34.81,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-07","peak_price":20900.0,"low_date":"2024-09-09","low_price":10750.0,"drawdown_after_peak_pct":-14.59,"green_lateness_ratio":null,"four_b_local_peak_proximity":"watch_only","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_not_full_4b","four_b_evidence_type":["source_proxy_cap","high_MAE_or_delayed_conversion"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"source_proxy_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE004_108380_20240611_2024-06-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG005_014940_20241119_Stage3Yellow","case_id":"C05_R1L218_CASE005_014940_20241119","symbol":"014940","company_name":"오리엔탈정공","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-19","entry_date":"2024-11-19","entry_price":4445.0,"evidence_available_at_that_date":"오리엔탈정공은 수주잔고 가시성과 영업 실적 지속성이 함께 확인되며 수주 headline이 margin result로 넘어가는 다리가 생긴 표본이다. 90/180D MFE와 낮은 MAE가 Yellow를 뒷받침한다.","evidence_source":"https://www.etoday.co.kr/news/view/2420784","evidence_source_quality":"news_with_direct_result_and_backlog_context","source_proxy_only":false,"stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014940/2024.csv","profile_path":"atlas/symbol_profiles/014/014940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2024-11-19","o":4575.0,"h":4750.0,"l":4440.0,"c":4445.0,"v":2971752,"a":13497137145,"mc":202574923145,"s":45573661,"m":"KOSDAQ"},"MFE_30D_pct":37.68,"MFE_90D_pct":44.88,"MFE_180D_pct":86.95,"MFE_1Y_pct":192.24,"MFE_2Y_pct":null,"MAE_30D_pct":-7.54,"MAE_90D_pct":-7.54,"MAE_180D_pct":-7.54,"MAE_1Y_pct":-7.54,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-08-08","peak_price":8310.0,"low_date":"2024-12-06","low_price":4110.0,"drawdown_after_peak_pct":-18.41,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"margin_bridge_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE005_014940_20241119_2024-11-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG006_071970_20250410_Stage3Yellow","case_id":"C05_R1L218_CASE006_071970_20250410","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2025-04-10","entry_date":"2025-04-10","entry_price":28150.0,"evidence_available_at_that_date":"그룹 조선 수주 흐름, 엔진 수주잔고, 실적 margin bridge가 같은 구간에 붙은 표본이다. 직접 route와 result bridge가 함께 있으므로 Stage2를 넘어 Yellow까지 허용하는 것이 맞다.","evidence_source":"https://m.thebell.co.kr/m/newsview.asp?newskey=202504041340456880102780","evidence_source_quality":"news_with_issuer_result_backlog_and_group_contracts","source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv","profile_path":"atlas/symbol_profiles/071/071970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2025-04-10","o":27850.0,"h":28300.0,"l":27100.0,"c":28150.0,"v":519019,"a":14483062375,"mc":954890084250,"s":33921495,"m":"KOSPI"},"MFE_30D_pct":52.4,"MFE_90D_pct":203.91,"MFE_180D_pct":278.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.73,"MAE_90D_pct":-3.73,"MAE_180D_pct":-3.73,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-11-03","peak_price":106600.0,"low_date":"2025-04-10","low_price":27100.0,"drawdown_after_peak_pct":-30.96,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"direct_order_margin_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE006_071970_20250410_2025-04-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG007_075580_20250521_Stage3Yellow","case_id":"C05_R1L218_CASE007_075580_20250521","symbol":"075580","company_name":"세진중공업","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2025-05-21","entry_date":"2025-05-21","entry_price":12030.0,"evidence_available_at_that_date":"탱크·블록 route와 1Q result margin bridge가 붙었지만 당일 저가가 깊어 MAE가 먼저 찍혔다. 이후 90/180D MFE가 컸으므로 hard 4C가 아니라 Yellow+high-MAE watch가 맞는 표본이다.","evidence_source":"https://www.ibks.com/company/common/download.jsp?filename=20250521042305033_ko.pdf&filepath=%2Ffiles%2Ftradeinfo%2Fbusreport","evidence_source_quality":"broker_report_q1_result_and_margin_bridge","source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","high_MAE_or_delayed_conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/075/075580/2025.csv","profile_path":"atlas/symbol_profiles/075/075580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2025-05-21","o":9680.0,"h":12030.0,"l":9600.0,"c":12030.0,"v":13354919,"a":151216433155,"mc":683898955680,"s":56849456,"m":"KOSPI"},"MFE_30D_pct":7.65,"MFE_90D_pct":127.76,"MFE_180D_pct":127.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.2,"MAE_90D_pct":-20.2,"MAE_180D_pct":-20.2,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-09-10","peak_price":27400.0,"low_date":"2025-05-21","low_price":9600.0,"drawdown_after_peak_pct":-38.87,"green_lateness_ratio":null,"four_b_local_peak_proximity":"watch_only","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_not_full_4b","four_b_evidence_type":["positioning_overheat","high_MAE_or_delayed_conversion"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mae_absorption_guard","current_profile_verdict":"current_profile_4C_too_early_if_mae_only_or_false_green_if_mae_ignored","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE007_075580_20250521_2025-05-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","trigger_id":"C05_R1L218_TRG008_017960_20250516_Stage3Yellow","case_id":"C05_R1L218_CASE008_017960_20250516","symbol":"017960","company_name":"한국카본","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPBUILDING_SUPPLIER_MARGIN_WORKING_CAPITAL_CONVERSION_GUARD","sector":"shipbuilding_supplier_and_l1_engineering","primary_archetype":"contract_backlog_margin_cash_conversion","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2025-05-16","entry_date":"2025-05-16","entry_price":20400.0,"evidence_available_at_that_date":"2025년 1Q에는 이전의 텍스트/내재화 단계와 달리 결과와 수주전망이 같이 움직이며 margin conversion이 가격경로로 확인됐다. 같은 symbol이라도 2024년 Stage2-watch와 2025년 Yellow를 분리해야 한다.","evidence_source":"https://marketin.edaily.co.kr/News/ReadE?newsId=02217286642169576","evidence_source_quality":"news_with_result_and_order_outlook","source_proxy_only":false,"stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017960/2025.csv","profile_path":"atlas/symbol_profiles/017/017960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","actual_1d_ohlc_entry_row":{"d":"2025-05-16","o":21850.0,"h":21900.0,"l":19720.0,"c":20400.0,"v":1299001,"a":26691244075,"mc":1058932420800,"s":51908452,"m":"KOSPI"},"MFE_30D_pct":31.62,"MFE_90D_pct":75.74,"MFE_180D_pct":100.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.33,"MAE_90D_pct":-3.33,"MAE_180D_pct":-3.33,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2026-01-12","peak_price":40950.0,"low_date":"2025-05-16","low_price":19720.0,"drawdown_after_peak_pct":-21.98,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"result_order_conversion_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","stock_count_change_max_abs_pct_180D":0.0,"same_entry_group_id":"C05_R1L218_CASE008_017960_20250516_2025-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE001_017960_20240516","trigger_id":"C05_R1L218_TRG001_017960_20240516_Stage2","symbol":"017960","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":64,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":25,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":64,"margin_bridge_score":16,"revision_score":20,"relative_strength_score":17,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":56,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":14.99,"MAE_90D_pct":-11.89,"score_return_alignment_label":"margin_cash_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE002_033500_20240516","trigger_id":"C05_R1L218_TRG002_033500_20240516_Stage2Actionable","symbol":"033500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":64,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":25,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":58,"margin_bridge_score":12,"revision_score":20,"relative_strength_score":17,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":64,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":65,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":8.69,"MAE_90D_pct":-18.37,"score_return_alignment_label":"delayed_margin_conversion_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE003_103230_20240516","trigger_id":"C05_R1L218_TRG003_103230_20240516_Stage2","symbol":"103230","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":64,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":25,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":64,"margin_bridge_score":16,"revision_score":20,"relative_strength_score":17,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":56,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Watch","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":2.85,"MAE_90D_pct":-31.36,"score_return_alignment_label":"text_backlog_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE004_108380_20240611","trigger_id":"C05_R1L218_TRG004_108380_20240611_Stage2","symbol":"108380","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":64,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":25,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":58,"margin_bridge_score":12,"revision_score":20,"relative_strength_score":17,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":64,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":55,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":2.24,"MAE_90D_pct":-34.81,"score_return_alignment_label":"source_proxy_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE005_014940_20241119","trigger_id":"C05_R1L218_TRG005_014940_20241119_Stage3Yellow","symbol":"014940","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":75,"margin_bridge_score":70,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":78,"margin_bridge_score":78,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":44.88,"MAE_90D_pct":-7.54,"score_return_alignment_label":"margin_bridge_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE006_071970_20250410","trigger_id":"C05_R1L218_TRG006_071970_20250410_Stage3Yellow","symbol":"071970","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":75,"margin_bridge_score":70,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":72,"margin_bridge_score":74,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":26,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":203.91,"MAE_90D_pct":-3.73,"score_return_alignment_label":"direct_order_margin_bridge_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE007_075580_20250521","trigger_id":"C05_R1L218_TRG007_075580_20250521_Stage3Yellow","symbol":"075580","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":75,"margin_bridge_score":70,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":86,"stage_label_before":"Stage3-Green_or_4C_conflict","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":72,"margin_bridge_score":74,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":26,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":127.76,"MAE_90D_pct":-20.2,"score_return_alignment_label":"positive_high_mae_absorption_guard","current_profile_verdict":"current_profile_4C_too_early_if_mae_only_or_false_green_if_mae_ignored"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R1L218_CASE008_017960_20250516","trigger_id":"C05_R1L218_TRG008_017960_20250516_Stage3Yellow","symbol":"017960","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":75,"margin_bridge_score":70,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":78,"margin_bridge_score":78,"revision_score":58,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05-specific ladder discounts source-proxy/order-text rows until margin/cash conversion is visible; direct result bridge positives are retained while high-MAE rows get 4B-watch cap rather than hard 4C.","MFE_90D_pct":75.74,"MAE_90D_pct":-3.33,"score_return_alignment_label":"result_order_conversion_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"aggregate_profile_comparison","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"Current profile after v12 corpus; stress-tested only.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":60.13,"avg_MAE_90D_pct":-16.4,"avg_MFE_180D_pct":90.26,"avg_MAE_180D_pct":-19.41,"false_positive_rate":0.75,"missed_structural_count":1,"late_green_count":2,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"mixed; source-proxy/order-text rows remain too easy to promote while direct result+cash bridge rows are under-separated"}
{"row_type":"aggregate_profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older baseline would over-promote backlog text and proxy evidence.","changed_axes":["rollback_reference_only"],"changed_thresholds":{},"eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":60.13,"avg_MAE_90D_pct":-16.4,"avg_MFE_180D_pct":90.26,"avg_MAE_180D_pct":-19.41,"false_positive_rate":0.625,"missed_structural_count":2,"late_green_count":3,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"weaker; confirms current global profile should not be rolled back"}
{"row_type":"aggregate_profile_comparison","profile_id":"P1_L1_supplier_result_cash_bridge_shadow","profile_scope":"sector_specific","profile_hypothesis":"L1 supplier/order rows require margin/cash bridge before Green.","changed_axes":["stage2_required_bridge","stage3_green_revision_min_by_margin_cash_freshness"],"changed_thresholds":{"green_cash_bridge_min":60},"eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":60.13,"avg_MAE_90D_pct":-16.4,"avg_MFE_180D_pct":90.26,"avg_MAE_180D_pct":-19.41,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":"watch_only","avg_four_b_full_window_peak_proximity":"watch_only","score_return_alignment_verdict":"improves separation of text/proxy counterexamples from actual result bridge positives"}
{"row_type":"aggregate_profile_comparison","profile_id":"P2_C05_margin_cash_conversion_ladder_shadow","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C05 order/backlog/result headline is a pipe; margin and cash are the water. Promotion follows water, not pipe length.","changed_axes":["c05_supplier_margin_cash_conversion_ladder","c05_source_proxy_stage_cap"],"changed_thresholds":{"source_proxy_green_cap":"Stage2-Actionable","result_without_cash_green_cap":"Stage3-Yellow"},"eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":60.13,"avg_MAE_90D_pct":-16.4,"avg_MFE_180D_pct":90.26,"avg_MAE_180D_pct":-19.41,"false_positive_rate":0.125,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":"watch_only","avg_four_b_full_window_peak_proximity":"watch_only","score_return_alignment_verdict":"best; caps weak proxy rows while keeping four direct bridge positives"}
{"row_type":"aggregate_profile_comparison","profile_id":"P3_high_MAE_live_contract_route_guard","profile_scope":"counterexample_guard","profile_hypothesis":"High MAE with a surviving route is 4B-watch, not hard 4C; high MAE without route stays capped.","changed_axes":["local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c_qualified"],"changed_thresholds":{"hard4c_requires_route_death":true},"eligible_trigger_count":8,"selected_entry_trigger_per_case":8,"avg_MFE_90D_pct":60.13,"avg_MAE_90D_pct":-16.4,"avg_MFE_180D_pct":90.26,"avg_MAE_180D_pct":-19.41,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":"watch_only","avg_four_b_full_window_peak_proximity":"watch_only","score_return_alignment_verdict":"keeps 075580 as absorbable high-MAE positive instead of wrong hard 4C"}
{"row_type":"shadow_weight","axis":"c05_supplier_margin_cash_conversion_ladder","scope":"canonical_archetype_specific","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","baseline_value":"order/backlog/result headline can promote if enough visibility","tested_value":"headline -> direct route -> realized margin/cash -> persistence/phase sanity","delta":"shadow_only_rule_addition","reason":"four counterexamples show backlog/source-proxy text without cash conversion gives high MAE or false Stage2/Green; four positives show direct margin/result bridge preserves upside","backtest_effect":"avg_MFE90=60.13, avg_MAE90=-16.4, false_positive_rate drops from 0.625/P0b or 0.625-like current errors to 0.125 in P2 proxy","trigger_ids":"C05_R1L218_TRG001_017960_20240516_Stage2|C05_R1L218_TRG002_033500_20240516_Stage2Actionable|C05_R1L218_TRG003_103230_20240516_Stage2|C05_R1L218_TRG004_108380_20240611_Stage2|C05_R1L218_TRG005_014940_20241119_Stage3Yellow|C05_R1L218_TRG006_071970_20250410_Stage3Yellow|C05_R1L218_TRG007_075580_20250521_Stage3Yellow|C05_R1L218_TRG008_017960_20250516_Stage3Yellow","calibration_usable_count":8,"new_independent_case_count":8,"counterexample_count":4,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"production_scoring_changed=false"}
{"row_type":"residual_contribution","round":"R1","loop":218,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"new_trigger_family_count":8,"same_archetype_new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","stage3_green_revision_min_by_margin_cash_freshness","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["source_proxy_stage2_false_positive","order_text_without_cash_conversion","delayed_margin_conversion_high_MAE","missed_direct_result_bridge","high_MAE_live_route_not_hard4C"],"new_axis_proposed":"c05_shipbuilding_supplier_margin_cash_conversion_ladder; c05_source_proxy_contract_stage_cap; c05_high_mae_live_contract_route_watch_guard","existing_axis_strengthened":"stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard","existing_axis_weakened":"hard_4c_thesis_break_routes_to_4c_qualified_for_high_mae_live_contract_route_only","existing_axis_kept":"price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence","sector_specific_rule_candidate":"L1 shipbuilding-supplier and engineering rows should require direct issuer route and margin/cash conversion before Yellow/Green promotion; sector backlog weather alone remains Stage2-watch.","canonical_archetype_rule_candidate":"C05 should split order/backlog/result headline from realized margin, working-capital release, cash conversion, and phase sanity. Order is the pipe; margin and cash are the water.","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1/e2r_2_2 calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat duplicate-low-value loops as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 218
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C05 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C01 direct backlog-to-FCF rows; C13 strict-new utilization/ex-credit rows; C10 strict-new order-conversion rows; C15 spread freshness rows; C31 non-semi/battery direct awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Price source: Songdaiki/stock-web `atlas/manifest.json` and `atlas/schema.json`.
- Research selection source: `docs/core/V12_Research_No_Repeat_Index.md`.
- Case sources are embedded per trigger row as `evidence_source`.
- All scoring deltas are research proxy scores, not production code behavior.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
rows_with_corporate_action_contaminated_180D_window: 0
ready_for_batch_ingest: true
```
