# Checkpoint 28A Round 222 R5 Loop 9 Consumer Retail Brand Price Validation

## Scope

`docs/round/round_222.md`를 반영해 소비재·유통·브랜드 가격경로 검증 팩을 추가했다. 이 라운드는 캘리브레이션/평가용이며 생산 scoring, StageClassifier, 후보 생성 로직은 바꾸지 않았다.

쉬운 예시:

- `Ulta/Sephora/Target 입점 논의`는 Stage 2 attention이다. 실제 매장 sell-through와 반복 주문이 확인되어야 Stage 3 후보가 된다.
- `IPO 직후 2배 상승`은 구조 증거가 아니라 4B-watch다.
- `중국 관광객 무비자 정책`은 event premium이다. 객단가, 면세 매출, OPM 전에는 Green이 아니다.

## Files Added

- `src/e2r/sector/round222_r5_loop9_consumer_retail_brand_price_validation.py`
- `src/e2r/cli/build_round222_r5_loop9_report.py`
- `tests/test_round222_r5_loop9_consumer_retail_brand_price_validation.py`
- `data/e2r_case_library/cases_r5_loop9_round222.jsonl`
- `data/sector_taxonomy/round222_r5_loop9_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round222_r5_loop9_consumer_retail_brand_price_validation/`

## Case Pack

Round 222 adds eight calibration cases:

| Case | Type | Main Decision |
|---|---|---|
| Samyang Buldak export regulatory watch | structural_success | Export, ASP, OP revision support Stage 3 candidate; Denmark recall remains regulatory watch. |
| Nongshim Shin global staple / Toomba | success_candidate | Global staple and product extension are Stage 2 until OPM/EPS/sell-through confirm. |
| APR / Medicube | structural_success | Strong K-beauty device rerating candidate, but fourfold rally requires 4B-watch. |
| d'Alba / Silicon2 / indie K-beauty basket | overheat | Retail talks and e-commerce growth are Stage 2; debut rally is event/overheat. |
| CJ / Olive Young | success_candidate | Platform exposure is Stage 2 until listed earnings bridge and store economics confirm. |
| AmorePacific legacy China exposure | failed_rerating | K-beauty macro is not enough; China exposure and Q2 miss are thesis-break watch. |
| Hyundai Department / Hotel Shilla / Hankook Cosmetics | event_premium | Visa-free tourism policy is event premium until tourist spend and OPM confirm. |
| F&F / TaylorMade optionality | event_premium | M&A optionality is Stage 1/2 event until transaction, financing, and EPS accretion confirm. |

## Canonical Alias Handling

The round text uses several labels that are mapped to existing canonical archetypes instead of expanding production enums blindly.

Examples:

- `K_FOOD_EXPORT_RECURRING` -> `EXPORT_RECURRING_CONSUMER`
- `K_BEAUTY_DEVICE_GLOBAL_BRAND` -> `BEAUTY_DEVICE_EXPORT`
- `K_BEAUTY_INDIE_BRAND_US_CHANNEL` -> `K_BEAUTY_BRAND_US_CHANNEL`
- `LEGACY_BEAUTY_CHINA_EXPOSURE_4C` -> `CHINA_CONSUMER_EXPOSURE_4C`
- `TOURISM_RETAIL_DUTYFREE_EVENT` -> `TOURISM_POLICY_EVENT`
- `APPAREL_M_AND_A_OPTIONALITY` -> `APPAREL_FAST_FASHION_BRAND_OEM`

## Green Guardrails

Stage 3-Green remains strict. Required evidence includes:

- repeat purchase or repeat demand
- overseas sales mix growth
- channel sell-through confirmed
- ASP or product mix improvement
- OPM improvement
- inventory and receivables stable
- tariff/recall/regulation passed
- single-SKU or single-device risk managed
- price path after evidence

Forbidden Green shortcuts include:

- viral TikTok only
- brand heat only
- retail talks without sell-through
- IPO or debut rally only
- influencer endorsement only
- M&A optionality without EPS
- China decline without offset
- tourism policy without spend or OPM
- private affiliate value without listed earnings bridge

## Price Validation Status

Full OHLC paths are not complete. The pack stores reported event anchors and explicitly marks:

- `price_validation_completed = partial_with_reported_price_anchors`
- `full_ohlc_complete = false`

This means the report can say “APR was 158,300 KRW at the Stage 2 anchor” or “tourism retail names moved +7.1%/+4.8%/+9.9% on the policy day,” but it must not invent 90D/180D/1Y MFE/MAE without adjusted daily prices.

## Verification

Commands:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m unittest tests.test_round222_r5_loop9_consumer_retail_brand_price_validation -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m e2r.cli.build_round222_r5_loop9_report
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m unittest discover -s tests -v
```

Result:

- Round 222 targeted tests: 12 tests passed.
- Full test suite: 2747 tests passed.
- Report CLI completed and wrote case JSONL, audit JSON, markdown, and CSV outputs.

## What Not To Change

- Do not apply these shadow weights to production scoring yet.
- Do not use Round 222 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not treat viral, IPO/debut rally, retail talks, tourism policy, influencer, M&A optionality, or China macro narratives as Green evidence.
- Do not invent full OHLC, stage prices, MFE/MAE, or business metrics.
