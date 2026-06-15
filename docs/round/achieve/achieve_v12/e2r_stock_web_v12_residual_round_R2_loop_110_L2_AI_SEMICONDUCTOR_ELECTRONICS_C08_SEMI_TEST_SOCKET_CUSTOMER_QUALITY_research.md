# E2R Stock-Web V12 Residual Research — R2 / C08 Test Socket Customer Quality Holdout

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 110
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: mixed_C08_test_socket_probe_card_customer_quality_holdout_pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout after session-adjusted Priority 0 and Priority 1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

The main prompt requires `coverage_index_first` selection rather than mechanical R1→R13 cycling. The static No-Repeat ledger shows C08 at 50 representative rows, so C08 is not a raw under-30 shortage. However, in this current session the under-30 and under-50 backlog has already been reinforced across C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23/C27 and R13 guardrail scopes. This run therefore uses C08 as a **quality holdout** rather than as a quantity-fill run.

C08 is the correct canonical because all selected rows sit in the semiconductor test-socket / probe-card / tester-contact chain. The research question is not whether the product category is structurally important; it is whether the evidence is strong enough to route the case from Stage2 into Stage3 without confusing a socket/probe-card/tester theme rally for durable customer-quality rerating.

## 2. Stock-Web manifest and schema check

- `source_name`: FinanceData/marcap
- `price_adjustment_status`: raw_unadjusted_marcap
- `calibration_shard_root`: atlas/ohlcv_tradable_by_symbol_year
- `max_date`: 2026-02-20
- `MFE_N_pct`: max high from entry_date through N tradable rows / entry_price - 1
- `MAE_N_pct`: min low from entry_date through N tradable rows / entry_price - 1
- All six rows below have at least 180 forward tradable rows in the downloaded Stock-Web shards.
- All corporate-action candidate dates in the symbol profiles are outside each row's 180D forward window.

## 3. Case table

| symbol | name | trigger_type | role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak-DD |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 098120 | 마이크로컨텍솔 | Stage3-Yellow | positive | 2024-12-04 | 4,570 | 33.2604 | -7.1116 | 140.919 | -7.1116 | 435.0109 | -7.1116 | -36.6053 |
| 131290 | 티에스이 | Stage4B | counterexample | 2024-09-03 | 46,450 | 17.3305 | -13.1324 | 20.5597 | -24.6502 | 20.5597 | -24.6502 | -37.5 |
| 425420 | 티에프이 | Stage4B | counterexample | 2024-01-02 | 37,100 | 1.0782 | -23.5849 | 18.4636 | -23.5849 | 18.4636 | -60.9434 | -67.0307 |
| 252990 | 샘씨엔에스 | Stage4B | counterexample | 2024-08-07 | 6,970 | 5.3085 | -31.8508 | 5.3085 | -49.7131 | 5.3085 | -49.7131 | -52.248 |
| 080580 | 오킨스전자 | Stage3-Yellow | positive | 2024-12-13 | 4,360 | 65.1376 | -2.6376 | 67.4312 | -3.4404 | 75.0 | -3.4404 | -23.9843 |
| 253590 | 네오셈 | Stage3-Yellow | positive | 2024-12-23 | 9,310 | 20.8378 | -8.3781 | 43.609 | -11.2782 | 43.609 | -18.2599 | -43.0815 |

## 4. Case notes

### 098120 마이크로컨텍솔 — positive with local 4B watch

The 2024-12-03 report framed the company as a semiconductor inspection socket specialist. The Stock-Web path confirms that this was not just a generic small-cap semiconductor rally: entry at 4,570 produced 180D MFE of 435.0109%. However, the 180D peak drawdown of -36.6053% means the rule should not unlock unguarded Green. C08 needs a **customer-quality plus reorder/margin bridge gate**, not just a test-socket label.

### 131290 티에스이 — Stage2/4B boundary counterexample

The 2024-09-02 IR material showed probe card, interface board, and test-socket positioning for high-speed memory testing. That was real Stage2 evidence. The price path, however, only reached 20.5597% MFE while suffering -24.6502% MAE and -37.5000% post-peak drawdown. The row argues that C08 should cap pre-qualification integrated-solution narratives at Stage2-Watch or local 4B until explicit customer qualification/revenue conversion is visible.

### 425420 티에프이 — package test socket narrative false-positive

The 2023-12-22 report described package test board/socket/COK capability and memory recovery/HBM-DDR5 demand. Entry at the first 2024 tradable row produced only 18.4636% 180D MFE and -60.9434% 180D MAE. This is a clean warning that a package-test-solution narrative with weak shipment/margin confirmation should not be promoted to Stage3.

### 252990 샘씨엔에스 — probe-card supply-chain growth without timing bridge

The 2024-08-06 report identified ceramic STF as an essential probe-card component and emphasized the structural probe-card market. The Stock-Web path was poor: 180D MFE stayed at 5.3085% while 180D MAE reached -49.7131%. The right C08 action is to require IDM/customer mix, DRAM/NAND allocation visibility, and margin/revenue timing before Stage3.

### 080580 오킨스전자 — cleaner C08 positive

The 2024-12-12 KIRS report identified test sockets and semiconductor test services directly. This row produced 75.0000% 180D MFE with only -3.4404% 90D/180D MAE. This is the cleanest positive row in the batch. It supports Stage3-Yellow when direct socket/test-service business evidence is paired with low MAE. Still, Green should wait for clearer recurring customer qualification or order bridge.

### 253590 네오셈 — tester-quality positive, but not pure socket Green

The 2024-12-20 report placed Neosem in SSD/CXL tester and automation equipment. Entry after the report produced 43.6090% 90D/180D MFE, but the peak-to-window drawdown reached -43.0815%. It is a useful C08 boundary positive: tester customer quality can be Stage3-Yellow, but not unguarded Stage3-Green without order backlog/revenue recognition quality.

## 5. Residual error and shadow rule

The recurring residual error is that **test socket / probe card / tester exposure gets over-compressed into a single positive C08 bucket**. The price path shows three distinct states:

1. **Clean customer-quality positive**: direct socket/test-service evidence + low MAE + strong MFE.
2. **Positive but local 4B**: very high MFE but deep peak drawdown; thesis survives, entry quality does not.
3. **Theme or timing false-positive**: product/category evidence exists, but shipment, customer qualification, margin, or revenue bridge is missing.

```text
rule_candidate =
C08_TEST_SOCKET_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REORDER_AND_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP
```

Proposed gate:

```text
Stage3-Yellow allowed only if at least two are present:
- explicit customer qualification / approved vendor / named customer route
- repeat reorder, shipment, or delivery conversion
- revenue recognition visibility
- margin bridge or high-value mix confirmation
- low MAE90/MAE180 path after entry

Stage3-Green blocked if:
- product narrative is only HBM/DDR5/CXL/probe-card adjacency
- no explicit qualification or reorder evidence
- MAE90 <= -20% or MAE180 <= -30% without later non-price confirmation
- post-peak drawdown exceeds -35% before revenue/margin bridge is confirmed
```

## 6. Machine-readable rows

```jsonl
{"MAE_180D_pct": -7.1116, "MAE_30D_pct": -7.1116, "MAE_90D_pct": -7.1116, "MFE_180D_pct": 435.0109, "MFE_30D_pct": 33.2604, "MFE_90D_pct": 140.919, "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_role": "positive", "corporate_action_candidate_dates": ["2011-04-19", "2011-05-17"], "current_profile_error": true, "drawdown_after_peak_pct": -36.6053, "entry_date": "2024-12-04", "entry_price": 4570.0, "evidence_url_pending": false, "fine_archetype_id": "IC_SOCKET_BURNIN_SOCKET_MEMORY_RECOVERY", "forward_rows_180D": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "마이크로컨텍솔", "notes": "IC socket / burn-in socket recovery evidence was strong enough to avoid generic semi-consumable treatment; the explosive 180D path supports a missed structural positive, but peak drawdown still requires local 4B overlay.", "peak_date": "2025-07-31", "peak_price": 24450.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 66, "capital_allocation": 30, "earnings_visibility": 58, "eps_fcf_explosion": 46, "information_confidence": 69, "market_mispricing": 74, "valuation_rerating": 61}, "representative_for_aggregate": true, "row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_loop": 110, "selected_round": "R2", "simulated_total_score": 57.71, "source_proxy_only": false, "source_title": "마이크로컨텍솔(098120) — 반도체 검사 소켓 제조 전문기업", "source_url": "https://stock.pstatic.net/stock-research/company/74/20241203_company_897946000.pdf", "stance": "positive_with_4b_watch", "symbol": "098120", "trigger_date": "2024-12-03", "trigger_type": "Stage3-Yellow", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -24.6502, "MAE_30D_pct": -13.1324, "MAE_90D_pct": -24.6502, "MFE_180D_pct": 20.5597, "MFE_30D_pct": 17.3305, "MFE_90D_pct": 20.5597, "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_role": "counterexample", "corporate_action_candidate_dates": ["2011-04-05", "2011-04-28"], "current_profile_error": true, "drawdown_after_peak_pct": -37.5, "entry_date": "2024-09-03", "entry_price": 46450.0, "evidence_url_pending": false, "fine_archetype_id": "PROBE_CARD_TEST_SOCKET_INTERFACE_BOARD_BOUNDARY", "forward_rows_180D": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "티에스이", "notes": "Integrated test-interface story had enough Stage2 evidence, but 2024 evidence still lacked explicit HBM customer quality/revenue conversion; MAE and post-peak drawdown argue for Stage2-Watch/4B rather than Stage3.", "peak_date": "2024-10-25", "peak_price": 56000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 48, "capital_allocation": 30, "earnings_visibility": 42, "eps_fcf_explosion": 32, "information_confidence": 58, "market_mispricing": 54, "valuation_rerating": 35}, "representative_for_aggregate": true, "row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_loop": 110, "selected_round": "R2", "simulated_total_score": 42.71, "source_proxy_only": false, "source_title": "티에스이 2024년 8월 IR 자료 — high-speed memory test interface, probe card, TIB, test socket", "source_url": "https://files-scs.pstatic.net/2024/09/02/nqmg6IpTkv/%ED%8B%B0%EC%97%90%EC%8A%A4%EC%9D%B4%2024%EB%85%848%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf", "stance": "counterexample_with_4b_watch", "symbol": "131290", "trigger_date": "2024-09-02", "trigger_type": "Stage4B", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -60.9434, "MAE_30D_pct": -23.5849, "MAE_90D_pct": -23.5849, "MFE_180D_pct": 18.4636, "MFE_30D_pct": 1.0782, "MFE_90D_pct": 18.4636, "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_role": "counterexample", "corporate_action_candidate_dates": [], "current_profile_error": true, "drawdown_after_peak_pct": -67.0307, "entry_date": "2024-01-02", "entry_price": 37100.0, "evidence_url_pending": false, "fine_archetype_id": "PACKAGE_TEST_SOCKET_RUBBER_SOCKET_HBM_DDR5_EXPECTATION", "forward_rows_180D": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "티에프이", "notes": "Memory/HBM/DDR5 recovery thesis was directionally plausible, but early 2024 entry suffered deep 30D and 180D MAE without shipment/margin confirmation.", "peak_date": "2024-03-21", "peak_price": 43950.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 48, "capital_allocation": 30, "earnings_visibility": 42, "eps_fcf_explosion": 32, "information_confidence": 58, "market_mispricing": 54, "valuation_rerating": 35}, "representative_for_aggregate": true, "row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_loop": 110, "selected_round": "R2", "simulated_total_score": 42.71, "source_proxy_only": false, "source_title": "티에프이(425420) — 패키지 테스트 부품 토탈 솔루션 업체", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1703204954624.pdf", "stance": "counterexample", "symbol": "425420", "trigger_date": "2023-12-22", "trigger_type": "Stage4B", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -49.7131, "MAE_30D_pct": -31.8508, "MAE_90D_pct": -49.7131, "MFE_180D_pct": 5.3085, "MFE_30D_pct": 5.3085, "MFE_90D_pct": 5.3085, "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_role": "counterexample", "corporate_action_candidate_dates": [], "current_profile_error": true, "drawdown_after_peak_pct": -52.248, "entry_date": "2024-08-07", "entry_price": 6970.0, "evidence_url_pending": false, "fine_archetype_id": "CERAMIC_STF_PROBE_CARD_MARKET_GROWTH", "forward_rows_180D": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "샘씨엔에스", "notes": "Probe-card supply-chain quality was real, but the row shows market-growth narrative without near-term customer mix/revenue/margin bridge; 90D/180D MAE makes Stage3 inappropriate.", "peak_date": "2024-08-07", "peak_price": 7340.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 48, "capital_allocation": 30, "earnings_visibility": 42, "eps_fcf_explosion": 32, "information_confidence": 58, "market_mispricing": 54, "valuation_rerating": 35}, "representative_for_aggregate": true, "row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_loop": 110, "selected_round": "R2", "simulated_total_score": 42.71, "source_proxy_only": false, "source_title": "샘씨엔에스(252990) — 프로브카드 필수 부품 세라믹 STF", "source_url": "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/08/06/240807_semcns.pdf", "stance": "counterexample", "symbol": "252990", "trigger_date": "2024-08-06", "trigger_type": "Stage4B", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -3.4404, "MAE_30D_pct": -2.6376, "MAE_90D_pct": -3.4404, "MFE_180D_pct": 75.0, "MFE_30D_pct": 65.1376, "MFE_90D_pct": 67.4312, "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_role": "positive", "corporate_action_candidate_dates": ["2021-01-07", "2021-01-29"], "current_profile_error": false, "drawdown_after_peak_pct": -23.9843, "entry_date": "2024-12-13", "entry_price": 4360.0, "evidence_url_pending": false, "fine_archetype_id": "BURNIN_SOCKET_TEST_SERVICE_TURNAROUND", "forward_rows_180D": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "오킨스전자", "notes": "Direct test-socket/test-service coverage paired with very shallow MAE and strong MFE; this is a clean C08 positive, though not Green without recurring customer qualification evidence.", "peak_date": "2025-08-18", "peak_price": 7630.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 66, "capital_allocation": 30, "earnings_visibility": 58, "eps_fcf_explosion": 46, "information_confidence": 69, "market_mispricing": 74, "valuation_rerating": 61}, "representative_for_aggregate": true, "row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_loop": 110, "selected_round": "R2", "simulated_total_score": 57.71, "source_proxy_only": false, "source_title": "오킨스전자(080580) — 반도체 검사용 소켓 및 테스트 전문기업", "source_url": "https://w4.kirs.or.kr/download/research/241212_%EB%B0%98%EB%8F%84%EC%B2%B4_%EC%98%A4%ED%82%A8%EC%8A%A4%EC%A0%84%EC%9E%90%28080580%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EA%B2%80%EC%82%AC%EC%9A%A9%20%EC%86%8C%EC%BC%93%20%EB%B0%8F%20%EB%B0%98%EB%8F%84%EC%B2%B4%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf", "stance": "positive", "symbol": "080580", "trigger_date": "2024-12-12", "trigger_type": "Stage3-Yellow", "window_180D_corporate_action_contaminated": false}
{"MAE_180D_pct": -18.2599, "MAE_30D_pct": -8.3781, "MAE_90D_pct": -11.2782, "MFE_180D_pct": 43.609, "MFE_30D_pct": 20.8378, "MFE_90D_pct": 43.609, "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_role": "positive", "corporate_action_candidate_dates": ["2019-01-31"], "current_profile_error": true, "drawdown_after_peak_pct": -43.0815, "entry_date": "2024-12-23", "entry_price": 9310.0, "evidence_url_pending": false, "fine_archetype_id": "SSD_CXL_TESTER_CUSTOMER_QUALITY_BOUNDARY", "forward_rows_180D": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "네오셈", "notes": "SSD/CXL tester quality path produced strong 30D/90D MFE, but full-window drawdown means C08 should separate tester order quality from price-chase Green.", "peak_date": "2025-02-19", "peak_price": 13370.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 66, "capital_allocation": 30, "earnings_visibility": 58, "eps_fcf_explosion": 46, "information_confidence": 69, "market_mispricing": 74, "valuation_rerating": 61}, "representative_for_aggregate": true, "row_type": "trigger", "schema_version": "v12_stock_web_residual", "selected_loop": 110, "selected_round": "R2", "simulated_total_score": 57.71, "source_proxy_only": false, "source_title": "네오셈(253590) — SSD/CXL tester automation and 2024 report", "source_url": "https://stock.pstatic.net/stock-research/company/74/20241220_company_638503000.pdf", "stance": "positive_with_4b_watch", "symbol": "253590", "trigger_date": "2024-12-20", "trigger_type": "Stage3-Yellow", "window_180D_corporate_action_contaminated": false}
{"avg_MAE_180D_pct": -27.3531, "avg_MFE_180D_pct": 99.6586, "calibration_usable_rows": 6, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "counterexample_count": 3, "current_profile_error_count": 5, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "positive_case_count": 3, "row_type": "aggregate", "rows_with_MAE180_below_minus_30pct": 2, "rows_with_MFE180_above_40pct": 3, "selected_loop": 110, "selected_round": "R2", "stage4b_or_watch_count": 5, "stage4c_count": 0, "trigger_row_count": 6}
{"canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "production_scoring_changed": false, "row_type": "shadow_rule_candidate", "rule_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REORDER_AND_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP", "rule_summary": "Test-socket/probe-card/tester narratives should not become Stage3-Green unless customer qualification, repeat reorder or shipment conversion, revenue recognition, and margin bridge are visible. High-MFE rows with deep post-peak drawdown remain positive but require local 4B/watch overlay.", "selected_loop": 110, "selected_round": "R2", "shadow_weight_only": true}
```

## 7. Source references

- 098120 마이크로컨텍솔: 마이크로컨텍솔(098120) — 반도체 검사 소켓 제조 전문기업 — https://stock.pstatic.net/stock-research/company/74/20241203_company_897946000.pdf
- 131290 티에스이: 티에스이 2024년 8월 IR 자료 — high-speed memory test interface, probe card, TIB, test socket — https://files-scs.pstatic.net/2024/09/02/nqmg6IpTkv/%ED%8B%B0%EC%97%90%EC%8A%A4%EC%9D%B4%2024%EB%85%848%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf
- 425420 티에프이: 티에프이(425420) — 패키지 테스트 부품 토탈 솔루션 업체 — https://ssl.pstatic.net/imgstock/upload/research/company/1703204954624.pdf
- 252990 샘씨엔에스: 샘씨엔에스(252990) — 프로브카드 필수 부품 세라믹 STF — https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/08/06/240807_semcns.pdf
- 080580 오킨스전자: 오킨스전자(080580) — 반도체 검사용 소켓 및 테스트 전문기업 — https://w4.kirs.or.kr/download/research/241212_%EB%B0%98%EB%8F%84%EC%B2%B4_%EC%98%A4%ED%82%A8%EC%8A%A4%EC%A0%84%EC%9E%90%28080580%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EA%B2%80%EC%82%AC%EC%9A%A9%20%EC%86%8C%EC%BC%93%20%EB%B0%8F%20%EB%B0%98%EB%8F%84%EC%B2%B4%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf
- 253590 네오셈: 네오셈(253590) — SSD/CXL tester automation and 2024 report — https://stock.pstatic.net/stock-research/company/74/20241220_company_638503000.pdf

## 8. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later coding-agent implementation session. Do not re-run web research.
Ingest this MD as a v12 residual research result. Validate JSONL trigger rows and ensure:
1. filename round/loop/large_sector/canonical match metadata,
2. trigger rows have complete entry_date, entry_price, MFE/MAE 30/90/180D,
3. all rows use price_basis=tradable_raw and price_adjustment_status=raw_unadjusted_marcap,
4. no corporate-action candidate overlaps the row's 180D window,
5. source_proxy_only=false and evidence_url_pending=false are preserved,
6. apply only shadow candidate evaluation, not production scoring changes.

Candidate shadow rule:
C08_TEST_SOCKET_CUSTOMER_QUALITY_REQUIRES_QUALIFICATION_REORDER_AND_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP

Expected effect:
- strengthen C08 Stage3 gate against product-category-only evidence,
- preserve clean socket/test-service positives with low MAE,
- apply local 4B overlay to high-MFE but high-post-peak-drawdown rows,
- avoid converting HBM/DDR5/CXL/probe-card adjacency into unguarded Stage3-Green.
```

## 10. Completion state

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / C08 quality holdout
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_holdout_only_if_new_customer_qualification_path | C19_BRAND_RETAIL_INVENTORY_MARGIN_quality_holdout | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
