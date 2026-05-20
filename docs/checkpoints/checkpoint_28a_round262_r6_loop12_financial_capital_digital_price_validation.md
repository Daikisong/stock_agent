# Checkpoint 28A Round 262 R6 Loop 12 Financial Capital Digital Price Validation

## 반영 내용

- `docs/round/round_262.md`의 R6 금융·자본배분·디지털금융 가격경로 검증 라운드를 코드화했다.
- 금융지주 value-up, 증권주 거래대금 cycle, 보험 NAV capital release, 은행 디지털자산 지분 option, NAVER/Dunamu platform trust, Toss FacePay, KakaoBank governance gate, stablecoin/FX gate를 calibration-only case record로 만들었다.
- `BROKERAGE_MARKET_VOLUME_CYCLE`, `BANK_DIGITAL_ASSET_EQUITY_OPTION`, `FINTECH_SUPERAPP_BIOMETRIC_PAYMENT`, `STABLECOIN_POLICY_OVERHEAT_FX_GATE` canonical archetype을 추가했다.
- full adjusted OHLC가 없는 항목은 reported anchor 또는 `price_data_unavailable_after_deep_search` 상태로 남겼다.
- production scoring, candidate generation, StageClassifier threshold는 변경하지 않았다.

## 핵심 가드레일

R6 Stage 3-Green은 `저PBR`, `value-up`, `증권주`, `디지털자산`, `stablecoin`, `IPO` 라벨만으로 만들지 않는다. 예를 들어 증권주가 KOSPI 7000 돌파일에 +13.5% 움직여도, brokerage fee/IB revenue/ROE가 확인되지 않으면 구조적 Green이 아니라 cycle Stage 2 또는 4B-watch다.

필수 확인 축:

- ROE 지속성
- CET1 / K-ICS / capital buffer
- credit cost / PF risk 안정
- 실제 자사주 소각 또는 반복 배당
- brokerage / IB / trading income 지속성
- regulated digital revenue 또는 equity-method income
- platform / exchange trust
- biometric / data privacy control
- FX outflow / stablecoin macro risk 통과
- evidence 이후 가격경로

금지 패턴:

- low PBR only
- policy value-up only
- market volume spike only
- stablecoin theme only
- digital asset equity option only
- major shareholder legal risk present
- exchange trust incident present
- privacy or data gate unresolved

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Korean financial holding value-up basket | Stage 2, not Green | 금융지주 +4.2%, KOSPI +6.45%, 상대 -2.25pp. ROE/CET1/credit cost와 실제 환원 확인 전 Green 금지 |
| Korean securities firms basket | cyclical_success + 4B-watch | 증권주 +13.5%, KOSPI 대비 +7.05pp. 거래대금 cycle이므로 revenue/ROE 확인 전 Green 금지 |
| Samsung Life | Stage 2 regulatory watch | 삼성전자 지분 매각 1.3조원. K-ICS/CSM/use of proceeds 확인 필요 |
| Hana Financial / Dunamu | Stage 2 digital-asset equity option | Dunamu 6.55% 지분, implied value 15.27조원. 지분법 이익과 exchange trust 필요 |
| NAVER / Dunamu | event premium + 4C-watch | deal value 15.13조원, 초기 +7% 후 -4.2%, 이상출금 540억원 trust gate |
| Toss / FacePay | unlisted Stage 2 + privacy watch | FacePay 480만 사용자, 33만 merchant. take-rate/credit cost/privacy 확인 필요 |
| Kakao / KakaoBank | governance 4C-watch | founder legal risk와 bank ownership suitability gate |
| Stablecoin policy basket | overheat + FX 4C-watch | 관련주 2~3배 움직임, Q1 stablecoin 거래 57조원, FX outflow risk |

## 산출물

- `src/e2r/sector/round262_r6_loop12_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round262_r6_loop12_report.py`
- `tests/test_round262_r6_loop12_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop12_round262.jsonl`
- `data/sector_taxonomy/round262_r6_loop12_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round262_r6_loop12_financial_capital_digital_price_validation/`

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation 입력 사용 없음
- Stage 3-Green threshold 완화 없음
- full OHLC, stage price, ROE, CET1, K-ICS, credit cost, regulated digital revenue, FX stability 미발명
