# Checkpoint 28A Round 288 R6 Loop 14 Finance Capital Allocation Digital Finance Price Validation

## 반영 범위

- 입력 문서: `docs/round/round_288.md`
- analyst round id: `round_216`
- 대섹터: `FINANCE_CAPITAL_ALLOCATION_DIGITAL_FINANCE`
- 신규/정규화 canonical archetype: 8개
- 신규 case record: 8개
- production scoring 변경: 없음
- candidate generation input 변경: 없음
- shadow weight only: true

이번 라운드는 금융지주 Value-Up, 지주 할인, 주주환원 실패, 인터넷은행 IPO, 디지털은행 지배구조 리스크, 디지털자산 M&A, 은행의 디지털자산 지분, PE/CB/stablecoin 이벤트를 검증팩으로 구조화했다.

## 생성 파일

- `src/e2r/sector/round288_r6_loop14_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round288_r6_loop14_report.py`
- `tests/test_round288_r6_loop14_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop14_round288.jsonl`
- `data/sector_taxonomy/round288_r6_loop14_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round288_r6_loop14_financial_capital_digital_price_validation/round288_r6_loop14_price_validation_summary.md`
- `output/e2r_round288_r6_loop14_financial_capital_digital_price_validation/round288_r6_loop14_case_matrix.csv`
- `output/e2r_round288_r6_loop14_financial_capital_digital_price_validation/round288_r6_loop14_shadow_weights.csv`
- `output/e2r_round288_r6_loop14_financial_capital_digital_price_validation/round288_r6_loop14_green_gate_review.md`
- `output/e2r_round288_r6_loop14_financial_capital_digital_price_validation/round288_r6_loop14_stage4b_4c_review.md`

## 핵심 결론

| 항목 | 결과 |
|---|---:|
| case records | 8 |
| success candidate | 4 |
| event premium | 2 |
| failed rerating / false-positive guardrail | 2 |
| Stage 3 dated cases | 0 |
| 4B-watch | 7 |
| 4C-watch / strong watch | 4 |
| hard 4C confirmed | 0 |
| full adjusted OHLC complete | false |

예를 들어 `Value-Up 법안`은 문을 열어주는 신호지만, 실제 Stage 3-Green은 `CET1 buffer`, `실제 배당/소각`, `credit cost`, `ROE/PBR rerating`이 닫혀야 가능하다. 마찬가지로 `Naver-Dunamu M&A`는 거래 규모만으로 Green이 아니라, Upbit abnormal withdrawal 같은 custody/internal-control 리스크를 먼저 통과해야 한다.

## 추가된 Green Gate

- CET1 capital buffer
- actual payout execution
- treasury-share cancellation
- credit-cost control
- holdco discount compression
- IPO aftermarket demand
- digital-asset custody/internal control
- AML/KYC regulatory clearance
- CB dilution-adjusted ROIC
- minority shareholder alignment
- evidence 이후 가격경로

## Green 금지 패턴

- Value-Up headline only
- shareholder-return proposal only
- announced buyback without cancellation
- IPO size or customer count only
- crypto exchange market share only
- M&A synergy without custody control
- CB/PE investment headline only
- stablecoin keyword without revenue
- founder legal risk unresolved

## 4B / 4C 판단

이번 라운드에서 직접 hard 4C는 확정하지 않았다. 대신 다음은 strong watch로 남겼다.

- Samsung C&T: shareholder-return proposal failure 후 almost -10%
- KakaoBank/Kakao: founder legal risk와 bank ownership rule
- Naver/Dunamu/Upbit: +7% 초기 반응 후 abnormal withdrawal로 -4.2%
- Samsung SDS/KKR: +20.8% event premium, 그러나 CB dilution-adjusted ROIC와 stablecoin revenue 미확인

## 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round288_r6_loop14_report
PYTHONPATH=src python -m unittest tests.test_round288_r6_loop14_financial_capital_digital_price_validation -v
```

## 남은 작업

- full adjusted OHLC 기반 30D/90D/180D/1Y MFE/MAE backfill
- 금융지주별 CET1, credit cost, payout/cancellation execution 데이터 연결
- 인터넷은행 IPO 후 aftermarket demand와 credit quality 검증
- 디지털자산 M&A/지분투자의 custody, AML/KYC, capital treatment, revenue bridge 검증

이 라운드는 scoring rule 적용이 아니라 calibration/evaluation 자료다. 케이스 record를 candidate generation input으로 쓰면 안 된다.
