# Checkpoint 28A Round 71 R5 Loop 3: Consumer / Retail / Brand

## 목적

Round 71은 소비재, 유통, 브랜드 영역에서 `수출 반복수요`와 `일회성 바이럴/채널 입점/규제 리스크`를 분리하기 위한 케이스 팩이다.

예를 들어 `삼양식품 Buldak 수출 성장`은 수출, ASP, OPM, EPS 상향이 같이 확인되면 Green 가능 후보가 될 수 있다. 하지만 `덴마크 리콜`은 같은 브랜드라도 식품안전 4C 감시 오버레이로 따로 기록해야 한다.

## 반영 파일

- `src/e2r/sector/round71_r5_loop3_consumer_retail_brand.py`
- `src/e2r/cli/build_round71_r5_loop3_report.py`
- `tests/test_round71_r5_loop3_consumer_retail_brand.py`
- `data/e2r_case_library/cases_r5_loop3_round71.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round71_r5_loop3_v3.csv`
- `output/e2r_round71_r5_loop3_consumer_retail_brand/`

## 분류 요약

- target_count: 16
- case_candidate_count: 12
- Green possible targets: 5
- Watch / Yellow-first targets: 6
- RedTeam-first targets: 5
- gate-only overlays: 4

## Green 가능 축

- `EXPORT_RECURRING_CONSUMER`
- `K_FOOD_SINGLE_HERO_PRODUCT`
- `K_BEAUTY_EXPORT_DISTRIBUTION`
- `BEAUTY_DEVICE_EXPORT`
- `BEAUTY_OEM_ODM_SUPPLYCHAIN`

이 축들은 매출 성장만으로 Green을 주지 않는다. 수출, 판매 실수요, 재주문, OPM/FCF, 재고/매출채권 안정성, 안전/규제 리스크를 같이 확인해야 한다.

## RedTeam 오버레이

- `FOOD_SAFETY_RECALL_OVERLAY`
- `DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY`
- `CHANNEL_STUFFING_INVENTORY_OVERLAY`
- `TARIFF_IMPORT_REGULATION_OVERLAY`

간단히 말하면 `채널 입점`은 Stage 2 증거가 될 수 있지만, `sell-through`와 `reorder`가 없으면 Green 증거가 아니다. `GMV 성장`도 데이터 유출, 공급업체 대금 지연, 규제 이슈가 있으면 4C 감시가 먼저다.

## 케이스 팩

추가한 주요 케이스:

- `samyang_buldak_export_rerating_case`
- `samyang_buldak_denmark_recall_case`
- `kbeauty_us_export_overtake_france_case`
- `kbeauty_us_tariff_risk_case`
- `apr_medicube_beauty_device_case`
- `medicube_ulta_tiktok_omnichannel_case`
- `coupang_data_breach_case`
- `coupang_supplier_payment_regulation_case`
- `coway_rental_recurring_case`
- `whirlpool_dividend_suspension_case`
- `shein_temu_ip_litigation_case`
- `shein_temu_eu_product_safety_case`

월 단위만 있는 케이스는 날짜를 만들지 않았다. 예를 들어 `2025-08`처럼 월만 확인된 관세 리스크는 `stage4c_date=null`로 두고 `needs_exact_stage_date_backfill`로 표시했다.

## 안전 원칙

- production scoring 변경 없음.
- case library는 candidate generation input이 아님.
- Stage 3-Green threshold를 낮추지 않음.
- 가격, sell-through, reorder, inventory, receivables, churn, tariff rate는 만들지 않음.
- 식품 리콜, 데이터 유출, 공급업체 규제, 관세/수입규제, 채널 스터핑은 RedTeam 필드로 유지.

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round71_r5_loop3_consumer_retail_brand -v
PYTHONPATH=src python -m e2r.cli.build_round71_r5_loop3_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

전체 테스트를 통과한 뒤 커밋했다.
