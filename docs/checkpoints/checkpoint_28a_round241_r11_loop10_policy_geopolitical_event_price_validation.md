# Checkpoint 28A Round 241 R11 Loop 10 Policy Geopolitical Event Price Validation

## 반영 내용

- `docs/round/round_241.md`의 R11 Loop 10 내용을 calibration-only 케이스팩으로 구조화했다.
- 신규 canonical archetype을 추가했다:
  - `POLITICAL_INSTITUTIONAL_TRUST_BREAK`
  - `MARKET_STRUCTURE_REFORM`
  - `GLOBAL_INDEX_INCLUSION`
  - `SHORT_SELLING_NORMALIZATION`
  - `AI_WINDFALL_TAX_POLICY_SHOCK`
  - `GEOPOLITICAL_ENERGY_SUPPLY_SHOCK`
  - `FX_LIQUIDITY_POLICY_RESPONSE`
  - `STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO`
  - `POLICY_CONFIDENCE_EVENT_PREMIUM`
  - `POLICY_RELIEF_RESPONSE`
  - `FX_OUTFLOW_TRADE_DEAL_OVERLAY`
  - `MACRO_HARD_4C`
- 신규 CLI를 추가했다:
  - `PYTHONPATH=src python -m e2r.cli.build_round241_r11_loop10_report`
- production scoring과 candidate generation은 변경하지 않았다.

## 케이스 요약

| case | 판정 | 핵심 앵커 |
| --- | --- | --- |
| Martial law political shock | 4C-watch | KOSPI nearly -2%, won two-year low |
| WGBI inclusion | Stage 2 market-structure | expected inflow 80T KRW, WGBI weight 2.22% |
| Short-selling normalization | Stage 2 market-access | five-year ban lifted, MSCI issues over 90% addressed |
| AI dividend/tax shock | 4C-watch | KOSPI intraday -5.1%, close -2.3% |
| Hormuz/Iran energy shock | macro hard 4C | KOSPI -12.06%, KRW 17-year low, Hyundai -15.8% |
| Hormuz policy response | Stage 2 relief | alternative suppliers, reserves, Red Sea vessels, maritime-security support |
| Kimchi bond / FX liquidity | Stage 2 FX-policy | stablecoin trading 57T KRW, KRW 1,347 to 1,353 anchors |
| $350B U.S. investment outflow | 4C-watch + relief | FX bond cap $3.5B to $5B, KRW -8%, retail U.S. holdings $160B |

## Green Gate 원칙

R11에서 Stage 3-Green은 “정책 뉴스가 크다”가 아니라 다음 연결이 있어야 한다.

예: `WGBI 편입`은 시장 구조 개선 신호지만, 실제 자금유입과 금리/환율/자금조달비용 개선, 그리고 특정 회사의 EPS/FCF 연결고리가 없으면 회사 Green이 아니다.

필수 조건:

- 정책이 실제 법안, 예산, index inclusion, 계약, capital inflow로 확정
- 회사 단위 revenue / EPS / FCF bridge 존재
- FX / 금리 / credit cost / energy cost 효과 확인
- 일회성 headline이 아니라 지속 효과 확인
- 정치·제도·규제 신뢰 훼손 부재

금지 패턴:

- 정책 발언만 있음
- 선거공약만 있음
- 세금/재분배 surprise
- martial-law 또는 제도 신뢰 훼손
- 지정학 headline만 있음
- WGBI/MSCI 기대만 있음
- FX 정책 발표만 있고 실제 flow 없음
- energy-security headline만 있고 비용/마진 안정 없음

## 산출 파일

- `data/e2r_case_library/cases_r11_loop10_round241.jsonl`
- `data/sector_taxonomy/round241_r11_loop10_policy_geopolitical_event_price_validation_audit.json`
- `output/e2r_round241_r11_loop10_policy_geopolitical_event_price_validation/round241_r11_loop10_price_validation_summary.md`
- `output/e2r_round241_r11_loop10_policy_geopolitical_event_price_validation/round241_r11_loop10_case_matrix.csv`
- `output/e2r_round241_r11_loop10_policy_geopolitical_event_price_validation/round241_r11_loop10_shadow_weights.csv`
- `output/e2r_round241_r11_loop10_policy_geopolitical_event_price_validation/round241_r11_loop10_stage4b_4c_review.md`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m py_compile src/e2r/sector/archetypes.py src/e2r/sector/round241_r11_loop10_policy_geopolitical_event_price_validation.py src/e2r/cli/build_round241_r11_loop10_report.py tests/test_round241_r11_loop10_policy_geopolitical_event_price_validation.py
PYTHONPATH=src python -m unittest tests.test_round241_r11_loop10_policy_geopolitical_event_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round241_r11_loop10_report
```

후속 전체 테스트는 커밋 전 최종 검증 단계에서 수행한다.

## 다음 작업

- R11은 policy/event가 가격을 먼저 움직이는 영역이므로 Stage 3-Green은 계속 보수적으로 유지한다.
- `Hormuz/Iran energy shock`은 R11 macro hard 4C 기준 케이스로 유지한다.
- WGBI, short-selling, FX liquidity는 Stage 2 구조 개선/relief로 두고, 실제 flow와 회사 EPS/FCF 연결이 생길 때만 후속 scoring 설계에 반영한다.
