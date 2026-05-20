# Checkpoint 28A Round 274 R5 Loop 13 Consumer Retail Brand Price Validation

## 반영 범위

- source round: `docs/round/round_274.md`
- analyst round id: `round_202`
- large sector: `CONSUMER_RETAIL_BRAND`
- production scoring changed: `false`
- candidate generation input: `false`
- shadow weight only: `true`
- full adjusted OHLC complete: `false`

이번 라운드는 R5 소비재·유통·브랜드 가격검증 팩이다. APR/Medicube, d'Alba/indie K-beauty, CJ Olive Young, Samyang Foods, 중국 관광·면세·백화점 basket, Shinsegae-AliExpress/Gmarket JV, Homeplus, Jensen fried-chicken event를 case library와 shadow report로 구조화했다.

## 핵심 결론

R5에서 Stage 3-Green은 “K-beauty”, “K-food”, “관광객”, “채널 입점”, “IPO pop”, “유명인 이벤트”가 아니다.

쉬운 예:

- `d'Alba 상장 후 2배`는 좋은 관심 신호지만, Ulta/Costco 매장 sell-through와 리오더 전에는 Green이 아니다.
- `중국 단체관광 비자면제`는 Stage 2 이벤트지만, 면세 spend, 호텔 점유율, 백화점 SSS, 마진 전에는 Green이 아니다.
- `Jensen Huang이 치킨을 먹었다`는 매출 증거가 아니다. SSS와 가맹점 마진이 없으면 4B/event premium이다.

## 추가한 canonical archetype

- `K_BEAUTY_DEVICE_GLOBAL_BRAND_4B`
- `INDIE_K_BEAUTY_US_RETAIL_CHANNEL`
- `H_AND_B_PLATFORM_GLOBALIZATION`
- `CHINA_TOURISM_DUTYFREE_RETAIL_EVENT`
- `CROSS_BORDER_ECOMMERCE_DATA_GATE`
- `GROCERY_RETAIL_CREDIT_4C_REFERENCE`
- `CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM`

기존 `K_FOOD_EXPORT_ASP_CAPACITY`는 Samyang case에 재사용했다.

## Case 요약

| case | 판정 | 핵심 |
|---|---|---|
| APR / Medicube | structural success candidate + 4B-watch | 주가 4배 이상, 해외 매출/미국 매출 강함. 반복구매·교체주기·마진 증거 필요 |
| d'Alba / indie K-beauty | success candidate + overheat | U.S. e-commerce 성장과 retail channel talk는 Stage 2. 물리 매장 sell-through 필요 |
| CJ Olive Young | H&B platform candidate | 비상장 자회사라 CJ Corp Green은 parent value bridge 필요 |
| Samyang Foods | aligned partial Stage 3 candidate | 수출·ASP·CAPA·OP revision 정렬. recall/input-cost 4C-watch 유지 |
| China tourism retail basket | event premium | 관광객 headline이 아니라 spend·SSS·occupancy·margin 필요 |
| Shinsegae-AliExpress/Gmarket JV | success candidate + data gate | 41% share와 50M DB는 Stage 2. 3년 data sharing ban은 Green gate |
| Homeplus | retail credit hard reference | liquidation value > going-concern value, equity write-off. 섹터 4C reference |
| Kyochon / Cherrybro / Neuromeka | price moved without evidence | 유명인 이벤트로 +20~30%, 실제 방문 식당은 비상장. SSS/마진 증거 없음 |

## Green gate 보강

필수 확인 축:

- repeat purchase
- physical-store sell-through
- same-store sales
- gross margin after tariff
- inventory discipline
- channel reorder rate
- parent value bridge
- data governance
- franchise margin
- cash conversion

금지 패턴:

- viral social media only
- celebrity event only
- tourist arrival headline only
- IPO/debut pop only
- channel talks without sell-through
- unlisted subsidiary read-through only
- data sharing regulatory risk
- offline retail credit stress

## 출력 파일

- `data/e2r_case_library/cases_r5_loop13_round274.jsonl`
- `data/sector_taxonomy/round274_r5_loop13_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round274_r5_loop13_consumer_retail_brand_price_validation/round274_r5_loop13_price_validation_summary.md`
- `output/e2r_round274_r5_loop13_consumer_retail_brand_price_validation/round274_r5_loop13_case_matrix.csv`
- `output/e2r_round274_r5_loop13_consumer_retail_brand_price_validation/round274_r5_loop13_green_gate_review.md`
- `output/e2r_round274_r5_loop13_consumer_retail_brand_price_validation/round274_r5_loop13_stage4b_4c_review.md`

## 변경하지 않은 것

- production scoring threshold 변경 없음
- StageClassifier 변경 없음
- candidate generation input 변경 없음
- case library를 live scoring에 주입하지 않음
- full OHLC, MFE/MAE, stage price를 임의로 만들지 않음
