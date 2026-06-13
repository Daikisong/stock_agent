# E2R v12 Residual Research — R5 / L5 / C20 BEAUTY_FOOD_GLOBAL_DISTRIBUTION / loop 168

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R5
selected_loop = 168
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = mixed_k_beauty_k_food_global_distribution_reorder_margin_leaf_set
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
```

## 1. Selection / no-repeat rationale

원본 No-Repeat Index에서 C20은 78 rows로 Priority 2 품질보강 구역이다. 이번 세션에서 P0/P1 및 thin-P2 축을 상당 부분 채운 뒤, 아직 직접 다루지 않은 L5 소비재의 K-beauty/K-food global distribution 축을 보강한다. C20은 이미 row 수가 부족한 단계는 아니므로, 단순 row 증량보다 URL/proxy 보강, positive/counterexample 균형, high-MAE/4B exit guard의 품질 확인을 우선한다.

이번 MD는 세션 내 기존 loop 121~167과 hard duplicate를 만들지 않는다. hard duplicate key는 `canonical_archetype_id + symbol + trigger_type + entry_date`로 확인했고, 이번 case set은 C20 안에서 K-food export, global ODM, sun-care ODM, hit-product channel expansion, legacy beauty rebound trap, stable global food low-alpha, food export cost-pressure trap을 분리한다.

```text
index_baseline_coverage_before: C20 rows 78
index_baseline_coverage_after_if_accepted: C20 rows 87
new_independent_case_count: 9
usable_trigger_row_count: 9
representative_trigger_count: 9
positive_case_count: 5
counterexample_count: 4
4B_watch_or_overlay_count: 5
current_profile_error_count: 9
```

## 2. Price atlas validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = entry_date close c
MFE_MAE_rule = entry 이후 N개 tradable row 안의 max high / min low vs entry_price
forward_window_required = 180 tradable rows
manifest_after_date_prices_fabricated = false
```

모든 selected row는 2024년 entry이고 stock-web manifest max date 2026-02-20 이전에 180 trading-row window가 충분하다. profile 기준 2024 entry~D+180 corporate-action overlap은 관찰되지 않았거나 과거 split candidate가 2024 window와 겹치지 않는 것으로 처리했다.

## 3. Case table

| case | symbol | trigger | label | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---:|---|---|---:|---:|---|
| 삼양식품 | 003230 | Stage2-Actionable / 2024-05-17 | positive | 60.81 / 2.02 | 97.54 / 2.02 | 1Q24 해외 매출 +83%, 미국·중국 mainstream channel 확장, 해외 비중 75%, OP +235%로 channel reorder가 margin으로 전환된 케이스. |
| 코스맥스 | 192820 | Stage2-Actionable / 2024-05-13 | positive_with_4B_overlay | 31.9 / -26.44 | 31.9 / -26.44 | Q1 실적 beat, 중국/미국 ODM 고객 수요와 OTC sun-care launch가 붙었지만 90D/180D MAE가 깊어 late-entry exit guard가 필요한 케이스. |
| 한국콜마 | 161890 | Stage2-Actionable / 2024-05-13 | positive | 42.0 / -5.64 | 43.09 / -9.91 | 선케어/색조 수출, 미국·중국 자회사 개선, 영업이익 전환/개선이 확인되어 C20의 reorder-margin bridge가 가격경로와 맞았다. |
| 코스메카코리아 | 241710 | Stage2-Actionable / 2024-05-13 | positive | 119.0 / -3.73 | 122.85 / -3.73 | Englewood/미국 indie brand 수요, 1H24 매출·영업이익 증가, ODM operating leverage가 강하게 맞물린 구조적 positive. |
| 브이티 | 018290 | Stage2-Actionable / 2024-05-14 | positive | 56.86 / -2.55 | 72.55 / -2.55 | Reedle Shot 중심 매출·OP 급증, 일본/국내/동남아/미국/유럽 확장, product-channel repeatability가 확인된 positive. |
| 아모레퍼시픽 | 090430 | Stage2-Watch / 2024-04-30 | counterexample | 18.29 / -31.62 | 18.29 / -41.3 | COSRX/서구권 성장 vocabulary는 있었지만 중국 손실과 duty-free/legacy brand drag가 남아, 90D/180D MAE가 깊게 나온 반례. |
| LG생활건강 | 051900 | Stage2-Watch / 2024-04-26 | counterexample | 22.45 / -18.11 | 22.45 / -24.87 | Q1 영업이익 반등과 중국/북미 수익성 개선은 있었지만, durable global reorder와 legacy duty-free/China recovery가 불충분해 90D 이후 drawdown이 컸다. |
| 오리온 | 271560 | Stage2-Watch / 2024-05-14 | counterexample | 16.87 / -10.41 | 18.51 / -10.41 | 중국·베트남·러시아 등 글로벌 현지법인과 비용효율은 안정적이지만, C20 rerating trigger로 보기에는 MFE가 낮고 MAE 대비 alpha가 약한 케이스. |
| 롯데웰푸드 | 280360 | Stage2-Watch / 2024-08-14 | counterexample | 1.23 / -36.69 | 1.23 / -38.84 | Pepero/India/Kazakhstan/global export narrative는 있었지만 원가·카카오·consensus miss와 가격경로 하락이 강해 C20 Actionable을 막아야 하는 반례. |

## 4. Evidence notes

### 삼양식품 (003230) — positive

- trigger_date: `2024-05-16` / entry_date: `2024-05-17` / entry_price: `446500.0`
- evidence: 1Q24 해외 매출 +83%, 미국·중국 mainstream channel 확장, 해외 비중 75%, OP +235%로 channel reorder가 margin으로 전환된 케이스.
- price path: 30D MFE/MAE `60.81 / 7.17`, 90D `60.81 / 2.02`, 180D `97.54 / 2.02`
- source_urls: https://www.asiae.co.kr/en/article/2024051617352402210, https://www.thevaluenews.co.kr/news/183227

### 코스맥스 (192820) — positive_with_4B_overlay

- trigger_date: `2024-05-13` / entry_date: `2024-05-13` / entry_price: `157700.0`
- evidence: Q1 실적 beat, 중국/미국 ODM 고객 수요와 OTC sun-care launch가 붙었지만 90D/180D MAE가 깊어 late-entry exit guard가 필요한 케이스.
- price path: 30D MFE/MAE `31.9 / -2.16`, 90D `31.9 / -26.44`, 180D `31.9 / -26.44`
- source_urls: https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2321271, https://www.asiae.co.kr/en/article/2024051314441247256

### 한국콜마 (161890) — positive

- trigger_date: `2024-05-10` / entry_date: `2024-05-13` / entry_price: `55000.0`
- evidence: 선케어/색조 수출, 미국·중국 자회사 개선, 영업이익 전환/개선이 확인되어 C20의 reorder-margin bridge가 가격경로와 맞았다.
- price path: 30D MFE/MAE `36.36 / -5.64`, 90D `42.0 / -5.64`, 180D `43.09 / -9.91`
- source_urls: https://www.kolmar.co.kr/eng/ir/finance_colma.php, https://www.mk.co.kr/en/business/11312588

### 코스메카코리아 (241710) — positive

- trigger_date: `2024-05-10` / entry_date: `2024-05-13` / entry_price: `44200.0`
- evidence: Englewood/미국 indie brand 수요, 1H24 매출·영업이익 증가, ODM operating leverage가 강하게 맞물린 구조적 positive.
- price path: 30D MFE/MAE `81.9 / -3.73`, 90D `119.0 / -3.73`, 180D `122.85 / -3.73`
- source_urls: https://www.cosmecca.com/eng/ir/ir_data.php, https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2324591

### 브이티 (018290) — positive

- trigger_date: `2024-05-14` / entry_date: `2024-05-14` / entry_price: `25500.0`
- evidence: Reedle Shot 중심 매출·OP 급증, 일본/국내/동남아/미국/유럽 확장, product-channel repeatability가 확인된 positive.
- price path: 30D MFE/MAE `56.86 / -2.55`, 90D `56.86 / -2.55`, 180D `72.55 / -2.55`
- source_urls: https://en.yna.co.kr/view/AEN20240514006200320, https://www.asiae.co.kr/en/article/2024051415185928748

### 아모레퍼시픽 (090430) — counterexample

- trigger_date: `2024-04-30` / entry_date: `2024-04-30` / entry_price: `169500.0`
- evidence: COSRX/서구권 성장 vocabulary는 있었지만 중국 손실과 duty-free/legacy brand drag가 남아, 90D/180D MAE가 깊게 나온 반례.
- price path: 30D MFE/MAE `18.29 / -4.78`, 90D `18.29 / -31.62`, 180D `18.29 / -41.3`
- source_urls: https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2326348, https://www.globalcosmeticsnews.com/amorepacific-q2-2024-net-sales-down-but-cosrx-acquisition-boosts-net-profit/

### LG생활건강 (051900) — counterexample

- trigger_date: `2024-04-25` / entry_date: `2024-04-26` / entry_price: `392000.0`
- evidence: Q1 영업이익 반등과 중국/북미 수익성 개선은 있었지만, durable global reorder와 legacy duty-free/China recovery가 불충분해 90D 이후 drawdown이 컸다.
- price path: 30D MFE/MAE `22.45 / 0.13`, 90D `22.45 / -18.11`, 180D `22.45 / -24.87`
- source_urls: https://www.asiae.co.kr/en/article/2024042516153988285, https://en.yna.co.kr/view/AEN20250204008600320

### 오리온 (271560) — counterexample

- trigger_date: `2024-05-14` / entry_date: `2024-05-14` / entry_price: `91300.0`
- evidence: 중국·베트남·러시아 등 글로벌 현지법인과 비용효율은 안정적이지만, C20 rerating trigger로 보기에는 MFE가 낮고 MAE 대비 alpha가 약한 케이스.
- price path: 30D MFE/MAE `16.87 / -0.66`, 90D `16.87 / -10.41`, 180D `18.51 / -10.41`
- source_urls: https://www.orionworld.com/en/investor/irdata.asp, https://www.orionworld.com/en/company/global.asp

### 롯데웰푸드 (280360) — counterexample

- trigger_date: `2024-08-02` / entry_date: `2024-08-14` / entry_price: `162700.0`
- evidence: Pepero/India/Kazakhstan/global export narrative는 있었지만 원가·카카오·consensus miss와 가격경로 하락이 강해 C20 Actionable을 막아야 하는 반례.
- price path: 30D MFE/MAE `1.23 / -22.13`, 90D `1.23 / -36.69`, 180D `1.23 / -38.84`
- source_urls: https://www.lottewellfood.com/en/ir/irnews, https://www.meritzsecurities.com/board/research/report/view.do?reportId=20240802001

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_003230_20240517_SAMYANG_BULDAK_GLOBAL_CHANNEL_REORDER", "symbol": "003230", "company": "삼양식품", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_BULDAK_GLOBAL_MAINSTREAM_CHANNEL_REORDER", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 446500.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage3-Yellow candidate", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.81, "MAE_30D_pct": 7.17, "MFE_90D_pct": 60.81, "MAE_90D_pct": 2.02, "MFE_180D_pct": 97.54, "MAE_180D_pct": 2.02, "peak_180D_date": "2025-02-14", "peak_180D_price": 882000.0, "trough_180D_date": "2024-09-09", "trough_180D_price": 455500.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "1Q24 해외 매출 +83%, 미국·중국 mainstream channel 확장, 해외 비중 75%, OP +235%로 channel reorder가 margin으로 전환된 케이스.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024051617352402210", "https://www.thevaluenews.co.kr/news/183227"], "current_profile_error_type": "too_late_without_global_reorder_margin_bridge", "shadow_rule_effect": "positive_unlock", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage2-Actionable|2024-05-17"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_192820_20240513_COSMAX_US_INDIE_ODM_HIGH_MAE", "symbol": "192820", "company": "코스맥스", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_ODM_US_INDIE_CUSTOMER_REORDER", "trigger_date": "2024-05-13", "entry_date": "2024-05-13", "entry_price": 157700.0, "trigger_type": "Stage2-Actionable", "case_label": "positive_with_4B_overlay", "proposed_stage": "Stage2-Actionable + local 4B exit guard", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.9, "MAE_30D_pct": -2.16, "MFE_90D_pct": 31.9, "MAE_90D_pct": -26.44, "MFE_180D_pct": 31.9, "MAE_180D_pct": -26.44, "peak_180D_date": "2024-06-14", "peak_180D_price": 208000.0, "trough_180D_date": "2024-08-13", "trough_180D_price": 116000.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "Q1 실적 beat, 중국/미국 ODM 고객 수요와 OTC sun-care launch가 붙었지만 90D/180D MAE가 깊어 late-entry exit guard가 필요한 케이스.", "evidence_urls": ["https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2321271", "https://www.asiae.co.kr/en/article/2024051314441247256"], "current_profile_error_type": "misses_post_trigger_high_mae_exit_guard", "shadow_rule_effect": "positive_but_exit_guard", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|Stage2-Actionable|2024-05-13"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_161890_20240513_KOLMAR_SUNCARE_US_ODM", "symbol": "161890", "company": "한국콜마", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_SUNCARE_US_ODM_REORDER_MARGIN", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 55000.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage2-Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.36, "MAE_30D_pct": -5.64, "MFE_90D_pct": 42.0, "MAE_90D_pct": -5.64, "MFE_180D_pct": 43.09, "MAE_180D_pct": -9.91, "peak_180D_date": "2024-09-30", "peak_180D_price": 78700.0, "trough_180D_date": "2024-12-09", "trough_180D_price": 49550.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "선케어/색조 수출, 미국·중국 자회사 개선, 영업이익 전환/개선이 확인되어 C20의 reorder-margin bridge가 가격경로와 맞았다.", "evidence_urls": ["https://www.kolmar.co.kr/eng/ir/finance_colma.php", "https://www.mk.co.kr/en/business/11312588"], "current_profile_error_type": "underweights_suncare_export_odm_reorder_bridge", "shadow_rule_effect": "positive_unlock", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|161890|Stage2-Actionable|2024-05-13"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_241710_20240513_COSMECCA_ENGLEWOOD_US_INDIE", "symbol": "241710", "company": "코스메카코리아", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_ODM_ENGLEWOOD_INDIE_BRAND_REORDER", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 44200.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage3-Yellow candidate", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 81.9, "MAE_30D_pct": -3.73, "MFE_90D_pct": 119.0, "MAE_90D_pct": -3.73, "MFE_180D_pct": 122.85, "MAE_180D_pct": -3.73, "peak_180D_date": "2024-09-27", "peak_180D_price": 98500.0, "trough_180D_date": "2024-05-17", "trough_180D_price": 42550.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "Englewood/미국 indie brand 수요, 1H24 매출·영업이익 증가, ODM operating leverage가 강하게 맞물린 구조적 positive.", "evidence_urls": ["https://www.cosmecca.com/eng/ir/ir_data.php", "https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2324591"], "current_profile_error_type": "too_late_on_us_indie_odm_operating_leverage", "shadow_rule_effect": "positive_unlock", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|241710|Stage2-Actionable|2024-05-13"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_018290_20240514_VT_REEDLESHOT_JAPAN_US_EU_EXPANSION", "symbol": "018290", "company": "브이티", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_HIT_PRODUCT_REORDER_JAPAN_US_EU_CHANNEL_EXPANSION", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 25500.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage2-Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.86, "MAE_30D_pct": -2.55, "MFE_90D_pct": 56.86, "MAE_90D_pct": -2.55, "MFE_180D_pct": 72.55, "MAE_180D_pct": -2.55, "peak_180D_date": "2024-12-16", "peak_180D_price": 44000.0, "trough_180D_date": "2024-05-16", "trough_180D_price": 24850.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "Reedle Shot 중심 매출·OP 급증, 일본/국내/동남아/미국/유럽 확장, product-channel repeatability가 확인된 positive.", "evidence_urls": ["https://en.yna.co.kr/view/AEN20240514006200320", "https://www.asiae.co.kr/en/article/2024051415185928748"], "current_profile_error_type": "underweights_hit_product_reorder_margin_bridge_when_channel_expands", "shadow_rule_effect": "positive_unlock", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|018290|Stage2-Actionable|2024-05-14"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_090430_20240430_AMORE_COSRX_OFFSET_CHINA_DRAG", "symbol": "090430", "company": "아모레퍼시픽", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_BRAND_COSRX_OFFSET_CHINA_DRAG", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 169500.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "proposed_stage": "Stage2-Watch / local 4B risk", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.29, "MAE_30D_pct": -4.78, "MFE_90D_pct": 18.29, "MAE_90D_pct": -31.62, "MFE_180D_pct": 18.29, "MAE_180D_pct": -41.3, "peak_180D_date": "2024-05-31", "peak_180D_price": 200500.0, "trough_180D_date": "2024-12-09", "trough_180D_price": 99500.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "COSRX/서구권 성장 vocabulary는 있었지만 중국 손실과 duty-free/legacy brand drag가 남아, 90D/180D MAE가 깊게 나온 반례.", "evidence_urls": ["https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2326348", "https://www.globalcosmeticsnews.com/amorepacific-q2-2024-net-sales-down-but-cosrx-acquisition-boosts-net-profit/"], "current_profile_error_type": "false_positive_if_cosrx_offset_ignores_china_loss_and_mae", "shadow_rule_effect": "false_positive_block", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|Stage2-Watch|2024-04-30"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_051900_20240426_LGHNH_Q1_REBOUND_DURABILITY_GAP", "symbol": "051900", "company": "LG생활건강", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_TURNAROUND_GLOBAL_DURABILITY_GAP", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 392000.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "proposed_stage": "Stage2-Watch + 4B exit guard", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.45, "MAE_30D_pct": 0.13, "MFE_90D_pct": 22.45, "MAE_90D_pct": -18.11, "MFE_180D_pct": 22.45, "MAE_180D_pct": -24.87, "peak_180D_date": "2024-05-23", "peak_180D_price": 480000.0, "trough_180D_date": "2025-01-20", "trough_180D_price": 294500.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "Q1 영업이익 반등과 중국/북미 수익성 개선은 있었지만, durable global reorder와 legacy duty-free/China recovery가 불충분해 90D 이후 drawdown이 컸다.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024042516153988285", "https://en.yna.co.kr/view/AEN20250204008600320"], "current_profile_error_type": "overcredits_first_quarter_profit_rebound_without_durable_channel_reorder", "shadow_rule_effect": "exit_guard", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|051900|Stage2-Watch|2024-04-26"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_271560_20240514_ORION_GLOBAL_STABLE_LOW_ALPHA", "symbol": "271560", "company": "오리온", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_GLOBAL_LOCAL_SUBSIDIARY_STABLE_LOW_ALPHA", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 91300.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "proposed_stage": "Stage2-Watch only", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.87, "MAE_30D_pct": -0.66, "MFE_90D_pct": 16.87, "MAE_90D_pct": -10.41, "MFE_180D_pct": 18.51, "MAE_180D_pct": -10.41, "peak_180D_date": "2025-02-12", "peak_180D_price": 108200.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 81800.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "중국·베트남·러시아 등 글로벌 현지법인과 비용효율은 안정적이지만, C20 rerating trigger로 보기에는 MFE가 낮고 MAE 대비 alpha가 약한 케이스.", "evidence_urls": ["https://www.orionworld.com/en/investor/irdata.asp", "https://www.orionworld.com/en/company/global.asp"], "current_profile_error_type": "should_not_promote_stable_global_distribution_without_rerating_trigger", "shadow_rule_effect": "low_alpha_filter", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|271560|Stage2-Watch|2024-05-14"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "case_id": "C20_168_280360_20240814_LOTTE_WELLFOOD_EXPORT_BUT_COST_PRESSURE", "symbol": "280360", "company": "롯데웰푸드", "market": "KOSPI/KOSDAQ", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_FOOD_GLOBAL_PEPPERO_INDIA_KAZAKHSTAN_COST_PRESSURE", "trigger_date": "2024-08-02", "entry_date": "2024-08-14", "entry_price": 162700.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "proposed_stage": "Stage2-Watch / local 4B block", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.23, "MAE_30D_pct": -22.13, "MFE_90D_pct": 1.23, "MAE_90D_pct": -36.69, "MFE_180D_pct": 1.23, "MAE_180D_pct": -38.84, "peak_180D_date": "2024-08-16", "peak_180D_price": 164700.0, "trough_180D_date": "2025-02-03", "trough_180D_price": 99500.0, "calibration_usable": true, "corporate_action_contamination_180D": "none_observed_in_profile_or_no_2024_180D_overlap", "evidence_summary": "Pepero/India/Kazakhstan/global export narrative는 있었지만 원가·카카오·consensus miss와 가격경로 하락이 강해 C20 Actionable을 막아야 하는 반례.", "evidence_urls": ["https://www.lottewellfood.com/en/ir/irnews", "https://www.meritzsecurities.com/board/research/report/view.do?reportId=20240802001"], "current_profile_error_type": "false_positive_if_export_growth_ignores_cacao_cost_and_missed_consensus", "shadow_rule_effect": "false_positive_block", "dedupe_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|280360|Stage2-Watch|2024-08-14"}
```

## 6. Machine-readable score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C20_168_003230_20240517_SAMYANG_BULDAK_GLOBAL_CHANNEL_REORDER", "symbol": "003230", "component_score_breakdown": {"eps_fcf": 90, "visibility": 85, "bottleneck_pricing": 80, "mispricing": 70, "valuation_rerating": 78, "capital_allocation": 45, "info_confidence": 86, "total_sim": 83.0}, "score_return_alignment": "aligned", "notes": "1Q24 해외 매출 +83%, 미국·중국 mainstream channel 확장, 해외 비중 75%, OP +235%로 channel reorder가 margin으로 전환된 케이스."}
{"row_type": "score_simulation", "case_id": "C20_168_192820_20240513_COSMAX_US_INDIE_ODM_HIGH_MAE", "symbol": "192820", "component_score_breakdown": {"eps_fcf": 82, "visibility": 75, "bottleneck_pricing": 72, "mispricing": 62, "valuation_rerating": 68, "capital_allocation": 40, "info_confidence": 78, "total_sim": 76.0}, "score_return_alignment": "aligned", "notes": "Q1 실적 beat, 중국/미국 ODM 고객 수요와 OTC sun-care launch가 붙었지만 90D/180D MAE가 깊어 late-entry exit guard가 필요한 케이스."}
{"row_type": "score_simulation", "case_id": "C20_168_161890_20240513_KOLMAR_SUNCARE_US_ODM", "symbol": "161890", "component_score_breakdown": {"eps_fcf": 82, "visibility": 78, "bottleneck_pricing": 70, "mispricing": 70, "valuation_rerating": 70, "capital_allocation": 42, "info_confidence": 80, "total_sim": 77.5}, "score_return_alignment": "aligned", "notes": "선케어/색조 수출, 미국·중국 자회사 개선, 영업이익 전환/개선이 확인되어 C20의 reorder-margin bridge가 가격경로와 맞았다."}
{"row_type": "score_simulation", "case_id": "C20_168_241710_20240513_COSMECCA_ENGLEWOOD_US_INDIE", "symbol": "241710", "component_score_breakdown": {"eps_fcf": 88, "visibility": 82, "bottleneck_pricing": 78, "mispricing": 76, "valuation_rerating": 82, "capital_allocation": 42, "info_confidence": 78, "total_sim": 82.0}, "score_return_alignment": "aligned", "notes": "Englewood/미국 indie brand 수요, 1H24 매출·영업이익 증가, ODM operating leverage가 강하게 맞물린 구조적 positive."}
{"row_type": "score_simulation", "case_id": "C20_168_018290_20240514_VT_REEDLESHOT_JAPAN_US_EU_EXPANSION", "symbol": "018290", "component_score_breakdown": {"eps_fcf": 86, "visibility": 76, "bottleneck_pricing": 82, "mispricing": 72, "valuation_rerating": 75, "capital_allocation": 38, "info_confidence": 76, "total_sim": 79.0}, "score_return_alignment": "aligned", "notes": "Reedle Shot 중심 매출·OP 급증, 일본/국내/동남아/미국/유럽 확장, product-channel repeatability가 확인된 positive."}
{"row_type": "score_simulation", "case_id": "C20_168_090430_20240430_AMORE_COSRX_OFFSET_CHINA_DRAG", "symbol": "090430", "component_score_breakdown": {"eps_fcf": 58, "visibility": 50, "bottleneck_pricing": 55, "mispricing": 45, "valuation_rerating": 46, "capital_allocation": 40, "info_confidence": 70, "total_sim": 57.0}, "score_return_alignment": "counterexample_aligned", "notes": "COSRX/서구권 성장 vocabulary는 있었지만 중국 손실과 duty-free/legacy brand drag가 남아, 90D/180D MAE가 깊게 나온 반례."}
{"row_type": "score_simulation", "case_id": "C20_168_051900_20240426_LGHNH_Q1_REBOUND_DURABILITY_GAP", "symbol": "051900", "component_score_breakdown": {"eps_fcf": 62, "visibility": 54, "bottleneck_pricing": 58, "mispricing": 50, "valuation_rerating": 50, "capital_allocation": 42, "info_confidence": 72, "total_sim": 60.0}, "score_return_alignment": "counterexample_aligned", "notes": "Q1 영업이익 반등과 중국/북미 수익성 개선은 있었지만, durable global reorder와 legacy duty-free/China recovery가 불충분해 90D 이후 drawdown이 컸다."}
{"row_type": "score_simulation", "case_id": "C20_168_271560_20240514_ORION_GLOBAL_STABLE_LOW_ALPHA", "symbol": "271560", "component_score_breakdown": {"eps_fcf": 60, "visibility": 70, "bottleneck_pricing": 54, "mispricing": 42, "valuation_rerating": 42, "capital_allocation": 46, "info_confidence": 72, "total_sim": 58.0}, "score_return_alignment": "counterexample_aligned", "notes": "중국·베트남·러시아 등 글로벌 현지법인과 비용효율은 안정적이지만, C20 rerating trigger로 보기에는 MFE가 낮고 MAE 대비 alpha가 약한 케이스."}
{"row_type": "score_simulation", "case_id": "C20_168_280360_20240814_LOTTE_WELLFOOD_EXPORT_BUT_COST_PRESSURE", "symbol": "280360", "component_score_breakdown": {"eps_fcf": 48, "visibility": 52, "bottleneck_pricing": 50, "mispricing": 35, "valuation_rerating": 35, "capital_allocation": 40, "info_confidence": 65, "total_sim": 50.0}, "score_return_alignment": "counterexample_aligned", "notes": "Pepero/India/Kazakhstan/global export narrative는 있었지만 원가·카카오·consensus miss와 가격경로 하락이 강해 C20 Actionable을 막아야 하는 반례."}
```

## 7. Aggregate row JSON

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md",
  "selected_round": "R5",
  "selected_loop": 168,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
  "index_baseline_rows_before": 78,
  "index_baseline_rows_after_if_accepted": 87,
  "new_independent_case_count": 9,
  "usable_trigger_row_count": 9,
  "representative_trigger_count": 9,
  "positive_case_count": 5,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 5,
  "current_profile_error_count": 9,
  "avg_MFE_90D_pct": 41.05,
  "avg_MAE_90D_pct": -14.8,
  "avg_MFE_180D_pct": 47.6,
  "avg_MAE_180D_pct": -17.34,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "price_source": "Songdaiki/stock-web",
  "do_not_propose_new_weight_delta": false
}
```

## 8. Residual contribution summary

이번 C20 품질보강의 residual은 “global distribution vocabulary”와 “실제 reorder / owned-channel / ODM customer expansion / margin conversion” 사이의 간극이다. Samyang, Cosmecca, VT, Kolmar는 제품·채널·수출/ODM 수요가 영업이익으로 전환되면서 가격경로가 잘 맞았다. 반면 Amorepacific, LG생활건강, Orion, Lotte Wellfood는 해외/글로벌 키워드가 있어도 legacy China drag, cost pressure, consensus miss, low-alpha stability 때문에 Stage2-Actionable로 올리면 오탐이 된다. Cosmax는 방향은 맞았지만 90D 이후 MAE가 커서 positive와 exit guard를 동시에 남겨야 한다.

```text
sector_specific_rule_candidate = L5_GLOBAL_DISTRIBUTION_REORDER_MARGIN_AND_EXIT_GATE_V1
canonical_archetype_rule_candidate = C20_REORDER_CHANNEL_MARGIN_CONVERSION_AND_LEGACY_DRAG_GATE_V1
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c20_reorder_channel_margin_conversion_and_legacy_drag_gate
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|local_4b_watch_guard
existing_axis_weakened = null
```

### Proposed rule wording

C20에서 “K-beauty/K-food 글로벌 수혜, 해외 매출 증가, 미국·일본·중국 채널, ODM 고객 확대”라는 단어만으로 Stage2-Actionable을 주지 않는다. 다음 중 적어도 하나의 **distribution/reorder bridge**와 하나의 **conversion bridge**가 같이 필요하다.

- distribution/reorder bridge: mainstream retailer/channel 입점, 재주문/reorder, ODM 핵심 고객 SKU 증가, owned/global channel 확장, 제품별 sell-through 또는 repeat demand.
- conversion bridge: 영업이익률/OP 증가, 해외 매출 비중 상승에 따른 margin mix, ASP/FX/mix benefit, 재고·원가·판관비 통제, consensus/revision 상향.
- block/guard: China/duty-free drag, cacao/raw-material cost pressure, one-quarter rebound, stable low-alpha food distribution, 보고서/실적 발표 후 이미 가격이 산소를 태운 high-MAE entry는 Stage2-Watch 또는 local 4B exit guard로 낮춘다.

## 9. Validation scope

```json
{
  "row_type": "validation_scope",
  "must_include_complete_30_90_180_mfe_mae": true,
  "trigger_rows_missing_required_price_fields": 0,
  "standard_v12_filename": "e2r_stock_web_v12_residual_round_R5_loop_168_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md",
  "filename_matches_required_regex": true,
  "round_sector_consistency": "pass",
  "compact_filename_forbidden_observed": false,
  "corporate_action_contaminated_180D_rows": 0,
  "insufficient_forward_window_rows": 0,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0,
  "narrative_only_rows": 0,
  "production_scoring_changed": false,
  "handoff_prompt_executed_now": false
}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.
Batch-ingest this MD together with other v12 residual research files.
Validate filename, metadata round/loop consistency, canonical_archetype_id, large_sector_id, trigger JSONL rows, and complete 30/90/180D MFE/MAE fields.
If validation passes, consider C20_REORDER_CHANNEL_MARGIN_CONVERSION_AND_LEGACY_DRAG_GATE_V1 as a shadow rule candidate only.
Do not loosen Stage3-Green global thresholds.
Do not apply a price-only positive patch.
Use the positive/counterexample split to refine C20 Stage2-Actionable bridge requirements and local 4B exit guards.
```

## 11. Next research state

```text
completed_round = R5
completed_loop = 168
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```