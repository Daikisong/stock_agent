# Checkpoint 28A Round 254 R11 Loop 11 Policy Geopolitical Event Price Validation

## 목적

`docs/round/round_254.md`의 R11 정책·지정학·재난·이벤트 가격검증 내용을 calibration-only 데이터팩으로 반영했다.

이번 패치는 production scoring을 바꾸지 않는다. 예를 들어 WGBI 편입과 실제 채권 유입은 좋은 Stage 2 시장구조 증거지만, 특정 회사의 Stage 3-Green이 되려면 회사 매출, EPS/FCF, 자금조달비용, FX 안정 연결이 별도로 필요하다.

## 반영 범위

- 추가 archetype:
  - `GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW`
  - `SHORT_SELLING_MARKET_ACCESS_REFORM`
  - `CORPORATE_GOVERNANCE_VALUEUP_POLICY`
  - `AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK`
  - `GEOPOLITICAL_ENERGY_SECURITY_HARD_4C`
  - `HORMUZ_POLICY_RELIEF_RESPONSE`
  - `FX_LIQUIDITY_STABLECOIN_OUTFLOW`
  - `FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW`
  - `POLICY_HEADLINE_NOT_GREEN`
- 추가 데이터팩:
  - `src/e2r/sector/round254_r11_loop11_policy_geopolitical_event_price_validation.py`
  - `src/e2r/cli/build_round254_r11_loop11_report.py`
  - `tests/test_round254_r11_loop11_policy_geopolitical_event_price_validation.py`

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Martial law crisis | 4C-watch | KOSPI 약 -2%, 원화 2년 저점, 10조원 안정기금 가능성 |
| WGBI inclusion | Stage 2 후보 | WGBI 2.22%, 2025년 11월 외국인 채권 순유입 110.8억 달러 |
| Short-selling reform | Stage 2 후보 | 5년 ban 해제, MSCI 접근성 개선, 100% 과징금 가능 |
| Commercial Act value-up | Stage 2 후보 | 신규 취득 자사주 1년 내 소각, 기존 자사주 6개월 유예 |
| AI dividend/tax shock | 4C-watch | KOSPI 장중 -5.1%, 종가 -2.3%, 세금·재분배 surprise |
| Hormuz/Iran shock | hard 4C | KOSPI -12.06%, KRW 1,505.8, 현대차 -15.8%, 삼성전자 -11.7%, SK하이닉스 -9.6% |
| Hormuz policy response | policy relief | 지원 논의와 에너지 안보 대응은 relief이지 Green 아님 |
| FX stablecoin / kimchi bond | Stage 2 + 4C-watch | stablecoin 57조원 거래, kimchi bond 14년 ban 해제, FX outflow watch |
| $350B U.S. pledge | policy relief + 4C-watch | 3,500억 달러 대미투자 약속, 연 200억 달러 유출 한도, 외평채 한도 증액 |

## Guardrails

- `production_scoring_changed=false`
- `candidate_generation_input=false`
- `shadow_weight_only=true`
- `full_adjusted_ohlc_complete=false`
- 정책 headline만으로 Stage 3-Green 금지
- WGBI/MSCI 기대만으로 Stage 3-Green 금지
- stablecoin theme만으로 Stage 3-Green 금지
- Hormuz/Iran energy shock은 R11 hard 4C reference로 유지

## 산출물

CLI 실행 시 아래 파일이 생성된다.

- `data/e2r_case_library/cases_r11_loop11_round254.jsonl`
- `data/sector_taxonomy/round254_r11_loop11_policy_geopolitical_event_price_validation_audit.json`
- `output/e2r_round254_r11_loop11_policy_geopolitical_event_price_validation/round254_r11_loop11_price_validation_summary.md`
- `output/e2r_round254_r11_loop11_policy_geopolitical_event_price_validation/round254_r11_loop11_case_matrix.csv`
- `output/e2r_round254_r11_loop11_policy_geopolitical_event_price_validation/round254_r11_loop11_shadow_weights.csv`
- `output/e2r_round254_r11_loop11_policy_geopolitical_event_price_validation/round254_r11_loop11_green_gate_review.md`
- `output/e2r_round254_r11_loop11_policy_geopolitical_event_price_validation/round254_r11_loop11_stage4b_4c_review.md`

## 다음 단계

R11은 점수 적용보다 gate 설계가 중요하다. 정책이 실제 법안·예산·자본유입으로 내려오고, 다시 회사 EPS/FCF로 연결되는지 확인하는 shadow scoring 비교가 다음 단계다.
