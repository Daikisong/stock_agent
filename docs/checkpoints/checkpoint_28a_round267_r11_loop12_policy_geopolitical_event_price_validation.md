# Checkpoint 28A Round 267 R11 Loop 12 Policy Geopolitical Disaster Event Price Validation

## 반영 범위

- 원문: `docs/round/round_267.md`
- analyst_round_id: `round_195`
- analyst_large_sector: `POLICY_GEOPOLITICAL_DISASTER_EVENT`
- canonical_large_sector: `POLICY_GEOPOLITICAL_EVENT`
- production scoring 변경: 없음
- candidate generation input 변경: 없음
- shadow weight only: true
- price validation: `partial_with_reported_price_anchors`
- full adjusted OHLC complete: false

이번 라운드는 정책·지정학·재난·이벤트가 가격을 크게 움직일 때, 그것을 바로 Stage 3-Green으로 보지 않고 `relief`, `event premium`, `4B-watch`, `4C-watch`, `hard 4C`로 나누기 위한 calibration pack이다.

쉬운 예시:

- `추경 26.2조원`은 정책 relief다.
- 하지만 특정 기업의 `매출, 마진, EPS/FCF`로 연결되는 증거가 없으면 Green 근거가 아니다.
- `현대차 새만금 10조 CAPEX 보도 + 주가 +10.5%`도 CAPEX-to-ROI가 닫히기 전까지는 event premium / 4B-watch다.

## 추가한 코드와 산출물

- `src/e2r/sector/round267_r11_loop12_policy_geopolitical_event_price_validation.py`
- `src/e2r/cli/build_round267_r11_loop12_report.py`
- `tests/test_round267_r11_loop12_policy_geopolitical_event_price_validation.py`
- `data/e2r_case_library/cases_r11_loop12_round267.jsonl`
- `data/sector_taxonomy/round267_r11_loop12_policy_geopolitical_event_price_validation_audit.json`
- `output/e2r_round267_r11_loop12_policy_geopolitical_event_price_validation/`

## 추가한 canonical archetype

- `LABOR_DISRUPTION_SYSTEMIC_POLICY_4C`
- `GEOPOLITICAL_ENERGY_MACRO_HARD_4C`
- `FISCAL_POLICY_RELIEF_NOT_GREEN`
- `AI_CAPITAL_MARKET_CONFIDENCE_EVENT`
- `STABLECOIN_FX_POLICY_OVERHEAT`
- `RARE_EARTH_END_USE_RESTRICTION_4C`
- `REGIONAL_POLICY_CAPEX_EVENT_PREMIUM`

기존 `CRITICAL_MINERALS_POLICY_RELIEF`는 그대로 사용했다.

## 케이스 요약

| case | 판정 | 핵심 가격/정책 anchor |
|---|---|---|
| Samsung strike | 4C-watch | 삼성전자 -9.3%, 18일 파업 계획, 5만명 이상, 하루 손실 최대 1조원 추정 |
| Middle East / Iran | hard 4C | KOSPI -12.06%, 원화 1,505.8/USD, 시총 817.6조원 감소 |
| Energy-saving / oil budget | policy relief | LNG 절감 14,000톤/일, 추경 26.2조원, 정유 지원 5조원 |
| KOSPI 7,000 | event premium + 4B-watch | KOSPI +6.45%, 삼성 +14.4%, 증권주 +13.5%, 외국인 3.1조원 순매수 |
| AI fiscal room | policy relief | AI/반도체 세수 여력, 추가 국채 없이 26.2조원 추경 |
| Stablecoin / FX | overheat + 4C-watch | Kakao Pay 2배 이상, LG CNS +70%, Aton +80%, ME2ON 3배 |
| Rare-earth / critical minerals | 4C-watch + relief | 중국 희토류 end-use 제한, 17개 광물 모니터링, 2,500억원 해외광산 지원 |
| Hyundai Saemangeum | event premium | 10조원 CAPEX 보도, 현대차 +10.5%, 기아 +15% |

## Green gate 보강 메모

R11 계열 Stage 3-Green은 다음을 통과해야 한다.

- 정책이 법, 예산, 계약, 자금유입 중 하나로 확정
- 기업 revenue / EPS / FCF bridge 확인
- FX, 금리, 에너지 cost 안정 확인
- 공급망 restriction 없음
- labor / safety / geopolitical hard gate 없음
- regulated revenue 또는 offtake 확인
- policy funding 지속가능
- 가격경로가 evidence 이후 따라옴

금지 패턴:

- policy headline only
- CAPEX report only
- stablecoin theme only
- index milestone only
- fiscal spending only
- supply-chain relief only
- labor strike unresolved
- energy shock unresolved

## 4B / 4C 보정

4B-watch 예시:

- 정책·재정·CAPEX 보도만으로 +10% 이상 급등
- stablecoin/digital policy로 2~3배 상승
- KOSPI sidecar-level 급등
- 증권주가 거래대금/실적 bridge 전에 +10% 이상 상승
- 희토류·critical minerals policy로 basket 급등

Hard 4C 예시:

- geopolitical energy chokepoint disruption
- KOSPI historic crash
- KRW disorderly depreciation
- strategic supply-chain sanction
- labor strike affecting national exports
- stablecoin-driven capital outflow

이번 라운드의 hard 4C는 `Middle East / Iran energy shock`만 확정했다. Samsung strike, stablecoin FX, rare-earth restriction은 hard 4C가 아니라 강한 4C-watch로 남겼다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round267_r11_loop12_policy_geopolitical_event_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round267_r11_loop12_report
```

라운드 전용 테스트는 통과했다. 전체 테스트는 커밋 전 검증 단계에서 다시 실행한다.

## 다음 단계

- 이 팩은 calibration/evaluation material이다.
- production scoring에는 아직 적용하지 않는다.
- 이후 R11 정책 이벤트 계열 shadow scoring에서 `relief`, `event premium`, `4B-watch`, `4C-watch`, `hard 4C` 분리를 먼저 검증한다.
