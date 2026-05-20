# Checkpoint 28A Round 261 R5 Loop 12 Consumer Retail Brand Price Validation

## 반영 내용

- `docs/round/round_261.md`의 R5 소비재·유통·브랜드 가격검증 라운드를 코드화했다.
- K-food export, H&B retail platform, K-beauty M&A validation, indie K-beauty physical-store test, e-commerce JV data gate, offline grocery distress, global confectionery localization, celebrity food-service event를 canonical archetype으로 고정했다.
- Samyang Foods, CJ Olive Young/CJ Corp, Dr.G/L'Oreal, d'Alba/Silicon2/Cosmax/Kolmar, E-Mart/Alibaba JV, Homeplus/MBK, Lotte Wellfood/Lotte India, Kyochon/Cherrybro/Neuromeka 케이스를 calibration-only case record로 만들었다.
- full adjusted OHLC가 없는 항목은 `price_data_unavailable_after_deep_search` 또는 reported-anchor 상태로 남겼다.
- production scoring, candidate generation, StageClassifier threshold는 변경하지 않았다.

## 핵심 가드레일

R5 Stage 3-Green은 `K-food`, `K-beauty`, `U.S. store`, `M&A`, `JV`, `celebrity event` 같은 라벨로 만들지 않는다. 예를 들어 Jensen Huang 치킨 이벤트로 종목이 +20~30% 움직여도, 같은 점포 매출과 프랜차이즈 마진이 없으면 가격만 움직인 이벤트다.

필수 확인 축:

- 반복구매 / 반복수요
- 해외 sell-through
- physical-store sell-through
- ASP 또는 mix 개선
- OPM / FCF 개선
- 재고·매출채권 안정
- channel retention / reorder
- customer data / platform trust 통과
- evidence 이후 가격경로

금지 패턴:

- K-food / K-beauty label only
- U.S. store plan only
- M&A validation only
- retail talks only
- celebrity food event only
- JV headline only
- offline asset value only
- overseas capex only

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Samyang Foods | structural_success_candidate + 4B-watch | 647,000원, +5.7%, target 830,000원, Q2 OP +84% 추정. 단일 SKU watch 유지 |
| CJ Olive Young / CJ Corp | Stage 2 | H&B global platform evidence는 강하지만 비상장 자회사와 parent earnings bridge 문제가 있음 |
| Dr.G / L'Oreal | Stage 2 validation | K-beauty brand M&A validation. ODM/상장사 매출 bridge 전 Green 금지 |
| d'Alba / Silicon2 / Cosmax / Kolmar | Stage 2 + 4B-watch | U.S. e-commerce growth는 강하지만 physical-store sell-through 전 Green 금지 |
| E-Mart / Alibaba JV | Stage 2 + data gate | E-Mart +5.5%, JV 41% share 기대, Gmarket 50M data. GMV/margin/data compliance 필요 |
| Homeplus / MBK | unlisted sector hard 4C reference | liquidation value 3.7T, assets 6.8T, MBK write-off 2.5T |
| Lotte Wellfood / Lotte India | Stage 2 | India localization과 Pepero capex. parent margin/FCF 확인 필요 |
| Kyochon / Cherrybro / Neuromeka | price_moved_without_evidence | celebrity event로 +20~30% 움직였지만 same-store sales evidence 없음 |

## 산출물

- `src/e2r/sector/round261_r5_loop12_consumer_retail_brand_price_validation.py`
- `src/e2r/cli/build_round261_r5_loop12_report.py`
- `tests/test_round261_r5_loop12_consumer_retail_brand_price_validation.py`
- `data/e2r_case_library/cases_r5_loop12_round261.jsonl`
- `data/sector_taxonomy/round261_r5_loop12_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round261_r5_loop12_consumer_retail_brand_price_validation/`

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation 입력 사용 없음
- Stage 3-Green threshold 완화 없음
- full OHLC, MFE/MAE, sell-through, 재고, 매출채권, FCF 미발명
