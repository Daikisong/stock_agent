# E2R v12 Residual Research — R8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
selected_round = R8
selected_loop = 143
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C28 software/security contract retention, source-proxy repair, ARR/renewal/managed-service bridge vs AI/security theme blowoff split
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = SECURITY_SOFTWARE_CONTRACT_RETENTION_ARR_MANAGED_SERVICE_GATE
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

No-Repeat Index 누적 장부는 현재 C01~C32가 모두 80 representative rows를 넘었으므로 단순 row fill이 아니라 URL/proxy 품질, complete MFE/MAE, entry 기준 보강이 우선이라고 지시한다. C28은 `270 rows / 52 symbols / positives-counter 39/87 / 4B-4C 48/3 / weights 20/24/8/16/14/8/10`으로 이미 수량은 충분하지만 counterexample와 source-proxy가 많고 4C path가 얇다. 따라서 이번 loop는 software/security theme을 추가로 반복하는 것이 아니라, **계약 유지·ARR·managed service·반복 사용·current revenue/OP bridge가 있는 positive**와 **제품 출시/AI·보안 단어만 있고 contract-retention bridge가 없는 false positive**를 분리한다.

이번 연구는 직전 R8 C26/C27과 겹치지 않는다. C26은 플랫폼/광고 operating leverage, C27은 콘텐츠/IP monetization이었고, 이번 C28은 software/security contract retention이다.

## 2. Stock-Web price atlas validation

Stock-Web manifest 기준:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14,354,401
symbol_count = 5,414
corporate_action_contaminated windows = blocked by default
```

Entry는 evidence date가 장중/당일 확인 가능하다고 보는 경우 당일 종가, 보도/공시 시각이 장마감 이후 또는 불명확하면 다음 tradable date를 원칙으로 둔다. 아래 8개 row는 모두 manifest max_date 이후 forward window를 만들지 않으며, 30D/90D/180D MFE·MAE를 모두 채웠다.

## 3. Novelty / duplicate gate

```text
new_independent_case_count = 8
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 8
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 1
stage4c_case_count = 3
source_proxy_only_count = 4
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 6
same_entry_duplicate_count = 0
```

## 4. Case table

| case_id | symbol | name | trigger_date | trigger_type | evidence family | outcome | source_proxy_only | judgement |
|---|---:|---|---|---|---|---|---:|---|
| C28-01 | 012510 | 더존비즈온 | 2024-11-05 | Stage3-Green | official_earnings_cloud_erp_ai_contracts | positive | false | clean_positive_contract_revenue_bridge |
| C28-02 | 263860 | 지니언스 | 2024-02-26 | Stage4C | official_revenue_milestone_without_forward_confirmation | counterexample | false | hard_4c_or_not_usable_until_current_year_contract_reacceleration |
| C28-03 | 263860 | 지니언스 | 2024-11-14 | Stage3-Green | q3_op_reacceleration_nac_cloud_managed_service | positive | true | positive_reacceleration_after_confirmed_quarter |
| C28-04 | 053800 | 안랩 | 2025-02-11 | Stage3-Yellow | q4_profit_mdr_mss_solution_service_bridge | positive_with_4b_watch | true | yellow_positive_with_local_4b_watch |
| C28-05 | 030520 | 한컴 | 2024-11-07 | Stage3-Green | q3_profit_cloud_saas_product_bridge | positive | true | clean_positive_cloud_saas_profit_conversion |
| C28-06 | 042510 | 라온시큐어 | 2024-04-30 | Stage4C | official_product_launch_without_contract_retention_conversion | counterexample | false | hard_4c_contract_retention_bridge_missing |
| C28-07 | 067920 | 이글루 | 2024-03-25 | Stage4C | conference_product_showcase_without_contract_arr_bridge | counterexample | true | hard_4c_or_source_quality_cap_until_contract_evidence |
| C28-08 | 136540 | 윈스 | 2024-08-01 | Stage4B | official_award_product_breadth_without_forward_conversion | counterexample | false | 4b_watch_source_quality_cap_not_green |


## 5. Actual Stock-Web entry OHLC rows

| case_id | symbol | entry_date | market | open | high | low | close/entry | volume |
|---|---:|---|---|---:|---:|---:|---:|---:|
| C28-01 | 012510 | 2024-11-05 | KOSPI | 59,000 | 59,000 | 53,700 | 57,300 | 431,165 |
| C28-02 | 263860 | 2024-02-26 | KOSDAQ | 13,170 | 13,300 | 12,950 | 13,030 | 26,471 |
| C28-03 | 263860 | 2024-11-14 | KOSDAQ | 9,100 | 9,590 | 9,080 | 9,430 | 26,960 |
| C28-04 | 053800 | 2025-02-11 | KOSDAQ | 72,600 | 74,900 | 71,700 | 73,400 | 100,338 |
| C28-05 | 030520 | 2024-11-07 | KOSDAQ | 19,440 | 19,580 | 18,310 | 18,320 | 812,444 |
| C28-06 | 042510 | 2024-04-30 | KOSDAQ | 2,355 | 2,415 | 2,345 | 2,360 | 239,661 |
| C28-07 | 067920 | 2024-03-25 | KOSDAQ | 6,300 | 6,300 | 6,140 | 6,240 | 51,381 |
| C28-08 | 136540 | 2024-08-01 | KOSDAQ | 13,600 | 13,700 | 13,250 | 13,420 | 11,437 |


## 6. Forward price path — 30D / 90D / 180D

| case_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_180D | trough_180D |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| C28-01 | 57,300 | 27.92 | -6.28 | 60.56 | -6.28 | 60.56 | -13.00 | 2025-02-07 @ 92,000 | 2025-04-09 @ 49,850 |
| C28-02 | 13,030 | 5.30 | -11.13 | 5.30 | -32.54 | 5.30 | -36.22 | 2024-03-13 @ 13,720 | 2024-07-19 @ 8,310 |
| C28-03 | 9,430 | 16.54 | -9.01 | 40.51 | -9.01 | 153.45 | -9.01 | 2025-07-11 @ 23,900 | 2024-12-09 @ 8,580 |
| C28-04 | 73,400 | 11.99 | -3.27 | 58.99 | -19.07 | 58.99 | -20.98 | 2025-04-07 @ 116,700 | 2025-10-20 @ 58,000 |
| C28-05 | 18,320 | 46.02 | -0.05 | 46.02 | -0.05 | 95.96 | -5.40 | 2025-06-23 @ 35,900 | 2025-04-07 @ 17,330 |
| C28-06 | 2,360 | 9.75 | -1.06 | 9.96 | -28.43 | 9.96 | -30.08 | 2024-08-30 @ 2,595 | 2024-12-09 @ 1,650 |
| C28-07 | 6,240 | 12.02 | -4.33 | 12.02 | -14.42 | 12.02 | -24.20 | 2024-03-26 @ 6,990 | 2024-11-15 @ 4,730 |
| C28-08 | 13,420 | 2.09 | -10.58 | 17.36 | -10.80 | 17.36 | -23.10 | 2024-11-05 @ 15,750 | 2025-02-14 @ 10,320 |


## 7. Evidence source map

| case_id | evidence source | role |
|---|---|---|
| C28-01 | https://www.douzone.com/media/media_room_read.jsp?id=2712 | 더존비즈온 3Q24 연결 매출 970억/OP 201억, 6분기 연속 성장, 클라우드 ERP·그룹웨어·EDM 매출 확대, ONE AI 출시 4개월 1,000개+ 도입계약. |
| C28-02 | https://www.genians.com/news/genians-achieves-milestone-revenue-growth-nac-innovation-and-global-expansion/ | Genians 2023 매출 milestone 및 19년 연속 흑자, NAC/ZTNA 성장 문구는 있으나 trigger 이후 90D/180D 경로가 깊은 MAE로 실패. |
| C28-03 | https://www.asiae.co.kr/en/article/2024111414345064506; https://www.genians.com/news/genians-achieves-milestone-revenue-growth-nac-innovation-and-global-expansion/ | Q3 2024 매출 104억(+34.9%), OP 22억(+660.8%), NAC 수요와 Cloud NAC Managed Service 고객 확보가 붙은 재가속 케이스. |
| C28-04 | https://biz.chosun.com/en/en-it/2025/02/11/VZQEWI5OWZCTJLYCXKYJB5JTL4/; https://www.ahnlab.com/en/product/service-plus; https://www.ahnlab.com/en/service/managed-security-service | 4Q24 OP 156억(+34.3%) 보도와 AhnLab MDR/MSS/Cloud Managed Service 제품·서비스 폭. 가격 MFE는 강하지만 180D MAE -20.98%로 Green은 drawdown-aware cap 필요. |
| C28-05 | https://www.asiae.co.kr/en/article/2024110710222009473; https://www.hancom.com/about/ir/notice; https://www.hancom.com/en/about/company | Q3 2024 매출 711.6억(+24.9%), OP 84.8억(+159.9%)와 클라우드 SaaS 상업화 성과. 공식 IR/제품 페이지는 AI·Docs·SDK 제품군을 뒷받침. |
| C28-06 | https://www.raon.com/ko/about/news_list/view/349 | OmniOne Digital ID 기반 DID ISIC 오픈과 글로벌 파트너십은 직접 제품/파트너 evidence지만, current revenue·retention bridge가 약해 90D/180D deep MAE. |
| C28-07 | https://m.boannews.com/html/detail.html?idx=127967 | SPiDER ExD/SIEM/SOAR/AI product showcase는 기술·제품 노출이지만, named enterprise contract/renewal/ARR bridge가 없어 180D MAE -24.2%. |
| C28-08 | https://wins21.com/eng/company/history.html; https://www.wins21.com/kor/main/main.html | WINS 공식 history의 2024 전략물자 수출관리 장관상과 네트워크·AI·클라우드·보안관제·유지관리 제품 폭은 있으나, current contract retention/revenue bridge가 약해 180D MAE -23.1%. |


## 8. Score simulation and residual classification

Current C28 weight basis from No-Repeat Index is:

```text
EPS/Vis/Bott/Mis/Val/Cap/Info = 20/24/8/16/14/8/10
```

| case_id | component EPS/Vis/Bott/Mis/Val/Cap/Info | current_total | shadow_total | current profile error | v12 residual judgement |
|---|---|---:|---:|---|---|
| C28-01 | 19/24/7/14/12/7/6 | 89 | 91 | none_or_slightly_too_late | clean_positive_contract_revenue_bridge |
| C28-02 | 14/20/5/12/9/5/8 | 73 | 66 | false_positive_if_revenue_milestone_overweighted | hard_4c_or_not_usable_until_current_year_contract_reacceleration |
| C28-03 | 18/24/7/14/12/6/8 | 89 | 92 | too_late_if_managed_service_visibility_underweighted | positive_reacceleration_after_confirmed_quarter |
| C28-04 | 16/22/6/13/11/7/7 | 82 | 81 | green_overpromotion_risk_if_mfe_only | yellow_positive_with_local_4b_watch |
| C28-05 | 18/23/5/14/12/6/10 | 88 | 91 | none_or_too_late_if_ai_product_monetization_underweighted | clean_positive_cloud_saas_profit_conversion |
| C28-06 | 12/17/5/12/8/4/6 | 64 | 58 | false_positive_if_product_launch_overweighted | hard_4c_contract_retention_bridge_missing |
| C28-07 | 11/16/5/12/8/4/6 | 62 | 56 | false_positive_if_security_product_theme_overweighted | hard_4c_or_source_quality_cap_until_contract_evidence |
| C28-08 | 12/18/5/12/9/5/6 | 67 | 61 | false_positive_if_award_product_breadth_overweighted | 4b_watch_source_quality_cap_not_green |


### Component interpretation

- `EPS` is kept important but not dominant. C28 winners need visible revenue/OP conversion, not only product screenshots.
- `Vis` should rise because ARR, renewal, managed security service, enterprise contract retention, and public/large-enterprise deployment are the core proof objects.
- `Bott` is lower than semiconductor/defense because software/security product scarcity is often narrative-heavy unless named customer or retention evidence exists.
- `Mis` and `Val` should be capped where price moved before contract evidence.
- `Info` should rise because source quality is decisive: product launch, conference demo, and generic AI/security vocabulary are not enough.

## 9. Case-level notes

### C28-01 — 더존비즈온 / official earnings + cloud ERP + ONE AI adoption contracts

This is a clean C28 positive. The evidence is not merely “AI software.” It includes 3Q24 revenue/OP growth, six-quarter growth continuation, cloud ERP/groupware/EDM sales lift, and ONE AI adoption contracts above 1,000 in four months. The price path validates the evidence: MFE_90D and MFE_180D both reached +60.56%, while the 180D trough was manageable at -13.00%.

Judgement: Stage3-Green valid, but still contract/revenue bridge-based rather than AI-word-based.

### C28-02 — 지니언스 / early revenue milestone but no immediate forward rerating

The February 2024 official milestone is real: NAC-driven ZTNA, revenue milestone, and 19 consecutive years of profitability. However, the entry was too early for E2R promotion. Forward MFE capped at +5.30% while MAE_90D/180D fell to -32.54%/-36.22%.

Judgement: revenue milestone alone is insufficient. Require current-year quarter reacceleration or managed-service/contract visibility before positive promotion.

### C28-03 — 지니언스 / Q3 reacceleration and Cloud NAC Managed Service

The November 2024 Q3 evidence is much stronger. It adds OP reacceleration, revenue growth, NAC demand from governments/large enterprises, and Cloud NAC Managed Service customers. The price path confirms the distinction: MFE_180D reached +153.45% with max MAE only -9.01%.

Judgement: same symbol, different trigger family. This is positive because revenue/OP reacceleration and managed-service bridge appeared.

### C28-04 — 안랩 / cybersecurity service portfolio + Q4 profit, but deep 180D drawdown

The Q4 profit trigger and AhnLab MDR/MSS/Cloud Managed Service portfolio provide a plausible C28 bridge. The forward path had strong MFE_90D +58.99%, but 180D MAE reached -20.98% after the peak.

Judgement: Stage3-Yellow positive with local 4B watch, not unconditional Green. C28 needs drawdown-aware confirmation when the rerating arrives in a sharp price wave.

### C28-05 — 한컴 / cloud SaaS and AI document software conversion

Hancom is a clean positive in this sample. Q3 sales/OP expansion and cloud SaaS commercialization were visible, while official IR/product pages show the AI/document software product direction. The path was strong and low-MAE: MFE_180D +95.96%, MAE_180D -5.40%.

Judgement: Stage3-Green valid when cloud SaaS profit conversion is present.

### C28-06 — 라온시큐어 / product launch without retention/revenue bridge

OmniOne Digital ID / DID ISIC is direct and official evidence, but it is still closer to product/partnership launch than recurring contract retention or current revenue conversion. Price confirms this: MAE_180D -30.08% with limited MFE.

Judgement: Stage4C for missing revenue-retention bridge despite official product evidence.

### C28-07 — 이글루 / SIEM/SOAR/AI showcase without contract bridge

SPiDER ExD, SIEM, AI, SOAR are relevant C28 vocabulary, but the source is an event/product showcase. No named contract, ARR, renewal, managed-service customer, or current OP bridge is present at the trigger. MFE stayed at +12.02% while MAE_180D reached -24.20%.

Judgement: hard 4C or source-quality cap until contract evidence appears.

### C28-08 — 윈스 / product breadth and awards without current conversion

WINS has credible network/AI/cloud security and maintenance/service breadth, and official history includes 2024 awards/status. But this still does not prove current contract retention or ARR-style conversion. The 180D path produced only +17.36% MFE and -23.10% MAE.

Judgement: Stage4B watch/source-quality cap. Product breadth is not contract retention.

## 10. Machine-readable trigger JSONL

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-01", "symbol": "012510", "name": "더존비즈온", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ERP_CLOUD_AI_CONTRACT_RETENTION_BRIDGE", "trigger_type": "Stage3-Green", "trigger_date": "2024-11-05", "entry_date": "2024-11-05", "entry_price": 57300, "entry_ohlc": {"o": 59000, "h": 59000, "l": 53700, "c": 57300, "v": 431165, "m": "KOSPI"}, "MFE_30D_pct": 27.92, "MFE_30D_date": "2024-11-29", "MFE_30D_price": 73300, "MAE_30D_pct": -6.28, "MAE_30D_date": "2024-11-05", "MAE_30D_price": 53700, "MFE_90D_pct": 60.56, "MFE_90D_date": "2025-02-07", "MFE_90D_price": 92000, "MAE_90D_pct": -6.28, "MAE_90D_date": "2024-11-05", "MAE_90D_price": 53700, "MFE_180D_pct": 60.56, "MFE_180D_date": "2025-02-07", "MFE_180D_price": 92000, "MAE_180D_pct": -13.0, "MAE_180D_date": "2025-04-09", "MAE_180D_price": 49850, "calibration_usable": true, "same_entry_group_id": "012510_2024-11-05", "dedupe_representative_for_aggregate": true, "outcome_label": "positive", "evidence_family": "official_earnings_cloud_erp_ai_contracts", "evidence_url": ["https://www.douzone.com/media/media_room_read.jsp?id=2712"], "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 89, "shadow_profile_total_score": 91, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "19/24/7/14/12/7/6", "v12_residual_judgement": "clean_positive_contract_revenue_bridge"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-02", "symbol": "263860", "name": "지니언스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NAC_ZTNA_REVENUE_MILESTONE_EARLY_CONFIRMATION_FAILURE", "trigger_type": "Stage4C", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 13030, "entry_ohlc": {"o": 13170, "h": 13300, "l": 12950, "c": 13030, "v": 26471, "m": "KOSDAQ"}, "MFE_30D_pct": 5.3, "MFE_30D_date": "2024-03-13", "MFE_30D_price": 13720, "MAE_30D_pct": -11.13, "MAE_30D_date": "2024-03-07", "MAE_30D_price": 11580, "MFE_90D_pct": 5.3, "MFE_90D_date": "2024-03-13", "MFE_90D_price": 13720, "MAE_90D_pct": -32.54, "MAE_90D_date": "2024-07-03", "MAE_90D_price": 8790, "MFE_180D_pct": 5.3, "MFE_180D_date": "2024-03-13", "MFE_180D_price": 13720, "MAE_180D_pct": -36.22, "MAE_180D_date": "2024-07-19", "MAE_180D_price": 8310, "calibration_usable": true, "same_entry_group_id": "263860_2024-02-26", "dedupe_representative_for_aggregate": true, "outcome_label": "counterexample", "evidence_family": "official_revenue_milestone_without_forward_confirmation", "evidence_url": ["https://www.genians.com/news/genians-achieves-milestone-revenue-growth-nac-innovation-and-global-expansion/"], "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 73, "shadow_profile_total_score": 66, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "14/20/5/12/9/5/8", "v12_residual_judgement": "hard_4c_or_not_usable_until_current_year_contract_reacceleration"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-03", "symbol": "263860", "name": "지니언스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NAC_CLOUD_NAC_MANAGED_SERVICE_REACCELERATION", "trigger_type": "Stage3-Green", "trigger_date": "2024-11-14", "entry_date": "2024-11-14", "entry_price": 9430, "entry_ohlc": {"o": 9100, "h": 9590, "l": 9080, "c": 9430, "v": 26960, "m": "KOSDAQ"}, "MFE_30D_pct": 16.54, "MFE_30D_date": "2024-11-26", "MFE_30D_price": 10990, "MAE_30D_pct": -9.01, "MAE_30D_date": "2024-12-09", "MAE_30D_price": 8580, "MFE_90D_pct": 40.51, "MFE_90D_date": "2025-03-26", "MFE_90D_price": 13250, "MAE_90D_pct": -9.01, "MAE_90D_date": "2024-12-09", "MAE_90D_price": 8580, "MFE_180D_pct": 153.45, "MFE_180D_date": "2025-07-11", "MFE_180D_price": 23900, "MAE_180D_pct": -9.01, "MAE_180D_date": "2024-12-09", "MAE_180D_price": 8580, "calibration_usable": true, "same_entry_group_id": "263860_2024-11-14", "dedupe_representative_for_aggregate": true, "outcome_label": "positive", "evidence_family": "q3_op_reacceleration_nac_cloud_managed_service", "evidence_url": ["https://www.asiae.co.kr/en/article/2024111414345064506", "https://www.genians.com/news/genians-achieves-milestone-revenue-growth-nac-innovation-and-global-expansion/"], "source_proxy_only": true, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 89, "shadow_profile_total_score": 92, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "18/24/7/14/12/6/8", "v12_residual_judgement": "positive_reacceleration_after_confirmed_quarter"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-04", "symbol": "053800", "name": "안랩", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CYBERSECURITY_MDR_MSS_SERVICE_OPERATING_LEVERAGE", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-02-11", "entry_date": "2025-02-11", "entry_price": 73400, "entry_ohlc": {"o": 72600, "h": 74900, "l": 71700, "c": 73400, "v": 100338, "m": "KOSDAQ"}, "MFE_30D_pct": 11.99, "MFE_30D_date": "2025-03-24", "MFE_30D_price": 82200, "MAE_30D_pct": -3.27, "MAE_30D_date": "2025-03-10", "MAE_30D_price": 71000, "MFE_90D_pct": 58.99, "MFE_90D_date": "2025-04-07", "MFE_90D_price": 116700, "MAE_90D_pct": -19.07, "MAE_90D_date": "2025-05-19", "MAE_90D_price": 59400, "MFE_180D_pct": 58.99, "MFE_180D_date": "2025-04-07", "MFE_180D_price": 116700, "MAE_180D_pct": -20.98, "MAE_180D_date": "2025-10-20", "MAE_180D_price": 58000, "calibration_usable": true, "same_entry_group_id": "053800_2025-02-11", "dedupe_representative_for_aggregate": true, "outcome_label": "positive_with_4b_watch", "evidence_family": "q4_profit_mdr_mss_solution_service_bridge", "evidence_url": ["https://biz.chosun.com/en/en-it/2025/02/11/VZQEWI5OWZCTJLYCXKYJB5JTL4/", "https://www.ahnlab.com/en/product/service-plus", "https://www.ahnlab.com/en/service/managed-security-service"], "source_proxy_only": true, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 82, "shadow_profile_total_score": 81, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "16/22/6/13/11/7/7", "v12_residual_judgement": "yellow_positive_with_local_4b_watch"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-05", "symbol": "030520", "name": "한컴", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DOCUMENT_SW_CLOUD_SAAS_AI_PRODUCT_MONETIZATION", "trigger_type": "Stage3-Green", "trigger_date": "2024-11-07", "entry_date": "2024-11-07", "entry_price": 18320, "entry_ohlc": {"o": 19440, "h": 19580, "l": 18310, "c": 18320, "v": 812444, "m": "KOSDAQ"}, "MFE_30D_pct": 46.02, "MFE_30D_date": "2024-12-02", "MFE_30D_price": 26750, "MAE_30D_pct": -0.05, "MAE_30D_date": "2024-11-07", "MAE_30D_price": 18310, "MFE_90D_pct": 46.02, "MFE_90D_date": "2024-12-02", "MFE_90D_price": 26750, "MAE_90D_pct": -0.05, "MAE_90D_date": "2024-11-07", "MAE_90D_price": 18310, "MFE_180D_pct": 95.96, "MFE_180D_date": "2025-06-23", "MFE_180D_price": 35900, "MAE_180D_pct": -5.4, "MAE_180D_date": "2025-04-07", "MAE_180D_price": 17330, "calibration_usable": true, "same_entry_group_id": "030520_2024-11-07", "dedupe_representative_for_aggregate": true, "outcome_label": "positive", "evidence_family": "q3_profit_cloud_saas_product_bridge", "evidence_url": ["https://www.asiae.co.kr/en/article/2024110710222009473", "https://www.hancom.com/about/ir/notice", "https://www.hancom.com/en/about/company"], "source_proxy_only": true, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 88, "shadow_profile_total_score": 91, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "18/23/5/14/12/6/10", "v12_residual_judgement": "clean_positive_cloud_saas_profit_conversion"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-06", "symbol": "042510", "name": "라온시큐어", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "DIGITAL_ID_DID_GLOBAL_PARTNERSHIP_NO_REVENUE_RETENTION_BRIDGE", "trigger_type": "Stage4C", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 2360, "entry_ohlc": {"o": 2355, "h": 2415, "l": 2345, "c": 2360, "v": 239661, "m": "KOSDAQ"}, "MFE_30D_pct": 9.75, "MFE_30D_date": "2024-05-03", "MFE_30D_price": 2590, "MAE_30D_pct": -1.06, "MAE_30D_date": "2024-05-30", "MAE_30D_price": 2335, "MFE_90D_pct": 9.96, "MFE_90D_date": "2024-08-30", "MFE_90D_price": 2595, "MAE_90D_pct": -28.43, "MAE_90D_date": "2024-08-05", "MAE_90D_price": 1689, "MFE_180D_pct": 9.96, "MFE_180D_date": "2024-08-30", "MFE_180D_price": 2595, "MAE_180D_pct": -30.08, "MAE_180D_date": "2024-12-09", "MAE_180D_price": 1650, "calibration_usable": true, "same_entry_group_id": "042510_2024-04-30", "dedupe_representative_for_aggregate": true, "outcome_label": "counterexample", "evidence_family": "official_product_launch_without_contract_retention_conversion", "evidence_url": ["https://www.raon.com/ko/about/news_list/view/349"], "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 64, "shadow_profile_total_score": 58, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "12/17/5/12/8/4/6", "v12_residual_judgement": "hard_4c_contract_retention_bridge_missing"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-07", "symbol": "067920", "name": "이글루", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "SIEM_SOAR_AI_PRODUCT_SHOWCASE_NO_CONTRACT_BRIDGE", "trigger_type": "Stage4C", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 6240, "entry_ohlc": {"o": 6300, "h": 6300, "l": 6140, "c": 6240, "v": 51381, "m": "KOSDAQ"}, "MFE_30D_pct": 12.02, "MFE_30D_date": "2024-03-26", "MFE_30D_price": 6990, "MAE_30D_pct": -4.33, "MAE_30D_date": "2024-04-19", "MAE_30D_price": 5970, "MFE_90D_pct": 12.02, "MFE_90D_date": "2024-03-26", "MFE_90D_price": 6990, "MAE_90D_pct": -14.42, "MAE_90D_date": "2024-08-02", "MAE_90D_price": 5340, "MFE_180D_pct": 12.02, "MFE_180D_date": "2024-03-26", "MFE_180D_price": 6990, "MAE_180D_pct": -24.2, "MAE_180D_date": "2024-11-15", "MAE_180D_price": 4730, "calibration_usable": true, "same_entry_group_id": "067920_2024-03-25", "dedupe_representative_for_aggregate": true, "outcome_label": "counterexample", "evidence_family": "conference_product_showcase_without_contract_arr_bridge", "evidence_url": ["https://m.boannews.com/html/detail.html?idx=127967"], "source_proxy_only": true, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 62, "shadow_profile_total_score": 56, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "11/16/5/12/8/4/6", "v12_residual_judgement": "hard_4c_or_source_quality_cap_until_contract_evidence"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "case_id": "C28-08", "symbol": "136540", "name": "윈스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_AI_CLOUD_SECURITY_BREADTH_WITHOUT_CURRENT_RETENTION_BRIDGE", "trigger_type": "Stage4B", "trigger_date": "2024-08-01", "entry_date": "2024-08-01", "entry_price": 13420, "entry_ohlc": {"o": 13600, "h": 13700, "l": 13250, "c": 13420, "v": 11437, "m": "KOSDAQ"}, "MFE_30D_pct": 2.09, "MFE_30D_date": "2024-08-01", "MFE_30D_price": 13700, "MAE_30D_pct": -10.58, "MAE_30D_date": "2024-08-05", "MAE_30D_price": 12000, "MFE_90D_pct": 17.36, "MFE_90D_date": "2024-11-05", "MFE_90D_price": 15750, "MAE_90D_pct": -10.8, "MAE_90D_date": "2024-12-09", "MAE_90D_price": 11970, "MFE_180D_pct": 17.36, "MFE_180D_date": "2024-11-05", "MFE_180D_price": 15750, "MAE_180D_pct": -23.1, "MAE_180D_date": "2025-02-14", "MAE_180D_price": 10320, "calibration_usable": true, "same_entry_group_id": "136540_2024-08-01", "dedupe_representative_for_aggregate": true, "outcome_label": "counterexample", "evidence_family": "official_award_product_breadth_without_forward_conversion", "evidence_url": ["https://wins21.com/eng/company/history.html", "https://www.wins21.com/kor/main/main.html"], "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_180D_contaminated": false, "current_profile_total_score": 67, "shadow_profile_total_score": 61, "component_score_breakdown_EPS_Vis_Bott_Mis_Val_Cap_Info": "12/18/5/12/9/5/6", "v12_residual_judgement": "4b_watch_source_quality_cap_not_green"}
```

## 11. Shadow weight proposal

```text
new_axis_proposed = C28_CONTRACT_RETENTION_ARR_MANAGED_SERVICE_BRIDGE_GATE
production_scoring_changed = false
shadow_weight_only = true

default_current_C28_weight = 20/24/8/16/14/8/10
suggested_shadow_weight_after = 18/27/7/13/12/8/15
suggested_shadow_weight_delta = -2/+3/-1/-3/-2/0/+5
```

Rationale:

1. Increase `earnings_visibility` because C28 winners are recognized when contract retention, managed service, SaaS monetization, or enterprise/public deployment turns into visible revenue/OP.
2. Increase `information_confidence` because C28 false positives often come from soft claims: AI/security/product launch/conference demo without customer, contract, renewal, or ARR evidence.
3. Reduce `market_mispricing` and `valuation_rerating` because C28 price waves can front-run weak product narratives and then reverse sharply.
4. Keep `capital_allocation` unchanged; it is useful but not the core C28 proof object.

## 12. Canonical rule candidate

```text
C28 positive-stage gate:
  Require at least two of:
    - named enterprise/public customer, contract, renewal, or recurring managed-service customer evidence
    - ARR/SaaS/subscription/managed security service revenue visibility
    - current quarter revenue/OP acceleration tied to product/service adoption
    - retention/renewal/expansion evidence, not just new product launch
    - official company IR/disclosure or high-quality direct source

C28 cap/4B/4C triggers:
  Apply Stage4B watch or Stage4C cap when evidence is only:
    - AI/security/cloud/product vocabulary
    - conference product showcase
    - award/status/history page
    - partner launch without current revenue/retention conversion
    - source-proxy-only news without company-level contract/revenue proof
```

## 13. Residual contribution summary

```text
loop_contribution_label = C28_contract_retention_arr_managed_service_quality_repair
sector_specific_rule_candidate = L8 software/security는 product launch나 AI/security vocabulary만으로 Stage2-Actionable을 열지 않고, contract-retention/ARR/managed-service/current revenue bridge를 요구한다.
canonical_archetype_rule_candidate = C28은 recurring contract economics가 핵심이다. named product만 있으면 Watch/4B cap, current revenue/OP/managed-service/customer bridge가 붙으면 Stage2-Actionable/Yellow/Green을 허용한다.
current_profile_error_types:
  - false_positive_if_product_launch_overweighted
  - false_positive_if_security_conference_demo_overweighted
  - green_overpromotion_risk_if_MFE_only
  - too_late_if_managed_service_visibility_underweighted
```

## 14. Batch Ingest Self-Audit

```text
standard_v12_filename = pass
compact_filename_used = false
metadata_round_matches_filename = pass
metadata_loop_matches_filename = pass
large_sector_id_present = pass
canonical_archetype_id_present = pass
trigger_type_canonical_stage_label_only = pass
all_usable_trigger_rows_have_entry_date = pass
all_usable_trigger_rows_have_entry_price = pass
all_usable_trigger_rows_have_MFE_30D_pct = pass
all_usable_trigger_rows_have_MFE_90D_pct = pass
all_usable_trigger_rows_have_MFE_180D_pct = pass
all_usable_trigger_rows_have_MAE_30D_pct = pass
all_usable_trigger_rows_have_MAE_90D_pct = pass
all_usable_trigger_rows_have_MAE_180D_pct = pass
source_proxy_only_flag_present = pass
evidence_url_pending_flag_present = pass
calibration_usable_flag_present = pass
same_entry_group_id_present = pass
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 15. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not use this handoff as live-trading advice. Do not run stock discovery.

Input research file:
- e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Task:
1. Parse all row_type=trigger JSONL rows.
2. Validate standard v12 filename and metadata consistency.
3. Validate C28 canonical scope and L8 large sector scope.
4. Validate complete 30D/90D/180D MFE/MAE fields.
5. Dedupe by canonical_archetype_id + symbol + trigger_type + trigger_date + entry_date + evidence_family.
6. Treat source_proxy_only=true rows as quality-capped. They may support guardrails and error taxonomy, but should not by themselves promote a positive scoring patch.
7. Consider shadow-only candidate axis:
   C28_CONTRACT_RETENTION_ARR_MANAGED_SERVICE_BRIDGE_GATE
8. Do not loosen Stage3-Green. Do not change production scoring without batch validation.
```

## 16. Completion state

```text
completed_round = R8
completed_loop = 143
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C28 software/security contract retention, source-proxy repair, ARR/renewal/managed-service bridge vs AI/security theme blowoff split
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE; C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK; C31_POLICY_SUBSIDY_LEGISLATION_EVENT; C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP; R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
