# Checkpoint 28A Round 97 - R5 Loop 5 Consumer / Retail / Brand

## 목적

`docs/round/round_97.md`의 소비재·유통·브랜드 보정안을 코드화했다.

이번 라운드는 생산 scoring을 바꾸지 않는다. 케이스 라이브러리와 shadow weight 표를 확장해, 이후 섹터별 점수비중을 조정하기 전 검증 재료를 만든다.

쉬운 예시:

- `미국 입점`은 Stage 2 단서일 수 있다.
- 하지만 `sell-through`, `재주문`, `OPM`, `재고/매출채권 안정`이 없으면 Stage 3-Green 증거로 쓰지 않는다.
- `TikTok 매출`도 마찬가지다. 할인율, CAC, creator commission이 크면 매출 성장이 아니라 마진 훼손일 수 있다.

## 반영 파일

- `src/e2r/sector/round97_r5_loop5_consumer_retail_brand.py`
- `src/e2r/cli/build_round97_r5_loop5_report.py`
- `tests/test_round97_r5_loop5_consumer_retail_brand.py`
- `data/e2r_case_library/cases_r5_loop5_round97.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round97_r5_loop5_v5.csv`
- `output/e2r_round97_r5_loop5_consumer_retail_brand/`

## 핵심 변경

- R5 Loop 5 target 23개를 정의했다.
- 케이스 후보 16개를 추가했다.
- 새 canonical archetype `K_BEAUTY_RETAIL_PLATFORM`을 추가했다.
- `K_FOOD_SINGLE_HERO_PRODUCT`, `K_BEAUTY_EXPORT_DISTRIBUTION`, `BEAUTY_DEVICE_EXPORT`, `RETAIL_ECOMMERCE_LOGISTICS`, `APPAREL_FAST_FASHION_BRAND_OEM`, `ULTRA_LOW_COST_CROSSBORDER_PLATFORM`, `HOME_APPLIANCE_HARDWARE_CYCLE`의 Loop 5 shadow weight를 문서 기준으로 조정했다.
- `store_level_sales`, `store_level_margin`, disclosure confidence 관련 backfill 필드를 추가했다.

## 생성 산출물 요약

- target_count: 23
- case_candidate_count: 16
- success_candidate_count: 6
- event_premium_count: 2
- stage4b_case_count: 3
- stage4c_case_count: 7
- green_possible_count: 5
- watch_yellow_first_count: 10
- redteam_first_count: 8
- gate_only_target_count: 5

## Green Guardrail

R5에서 Green 후보가 되려면 “잘 팔린다”만으로는 부족하다.

필요한 증거 예시:

- K푸드: 수출 증가, ASP, CAPA, OP/EPS 상향, 반복 SKU, 재고 안정
- K뷰티: 미국/일본/유럽 채널, sell-through, 재주문, OPM/FCF, 매출채권 안정
- beauty device: device ASP, units sold, device margin, 반복 skincare/소모품, 안전규제
- 렌탈 생활가전: 렌탈 계정, 해지율, 관리서비스 반복매출, FCF

RedTeam gate 예시:

- 식품 리콜, 국가별 판매제한
- 데이터 유출, 공급업체 압박, 대금지연
- shipment와 sell-through 괴리
- 관세, import review, de minimis 변화
- 할인율, affiliate CAC, creator commission으로 인한 마진 훼손

## 생산 로직 영향

- production_scoring_changed: false
- case_records_are_candidate_generation_input: false
- `features.py`, `staging.py`, `red_team.py`, `e2r_standard_flow.py`는 라운드 97 팩을 import하지 않는다.

## 검증

전용 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_round97_r5_loop5_consumer_retail_brand -v
```

결과:

- 11 tests OK

## 다음 작업

R6 Loop 5에서는 금융·자본배분·디지털금융 쪽에서 ROE/PBR, 주주환원, credit risk, 디지털 금융 trust risk를 같은 방식으로 case pack에 반영한다.
