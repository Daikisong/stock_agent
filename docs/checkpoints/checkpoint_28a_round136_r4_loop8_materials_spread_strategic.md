# Checkpoint 28A Round 136 R4 Loop 8 Materials / Spread / Strategic Resources

## 목적

`docs/round/round_136.md`의 R4 Loop 8 내용을 별도 calibration pack으로 반영했다.

R4는 원자재 가격, 스프레드, 전략자원 뉴스가 EPS를 크게 흔들 수 있지만, 대부분 cycle risk가 크다. 그래서 이번 라운드는 “가격이 올랐다”와 “EPS/FCF 체급 변화가 고정됐다”를 강하게 분리한다.

쉬운 예시는 다음과 같다.

- `구리 가격 record high`는 Stage 1~2 macro evidence가 될 수 있다.
- 하지만 개별 구리·비철금속 기업이 Stage 3-Green이 되려면 생산량, cash cost, FCF, 자본환원, 처리 input cost가 같이 확인돼야 한다.
- `Korea Zinc 공개매수 상승`은 전략금속 구조 성공이 아니라 event premium이다.
- `MP Materials DoD/Apple 계약`은 Stage 2 구조 후보지만, YTD 급등 뒤 증자가 붙으면 4B/dilution watch도 같이 봐야 한다.

## 반영 파일

- `src/e2r/sector/round136_r4_loop8_materials_spread_strategic.py`
- `src/e2r/cli/build_round136_r4_loop8_report.py`
- `tests/test_round136_r4_loop8_materials_spread_strategic.py`
- `data/e2r_case_library/cases_r4_loop8_round136.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round136_r4_loop8_v8.csv`
- `output/e2r_round136_r4_loop8_materials_spread_strategic/`

## v8 기본 점수축

| component | weight | 해석 |
| --- | ---: | --- |
| eps_fcf_transition | 22 | 원자재 가격만으로는 cap. OP/EPS/FCF와 비용통제가 Stage 3의 핵심 |
| contract_offtake_price_floor_visibility | 20 | price floor, offtake, 정부투자, 고객계약, 생산계획 확인 |
| bottleneck_pricing_power | 18 | 희토류 scarcity, 구리 AI-grid, 금 realized price, spread 개선 |
| market_mispricing_rerating_gap | 10 | 구조적 mispricing과 공개매수/event premium을 분리 |
| valuation_room_4b_runway | 8 | scarcity narrative가 이미 가격에 반영됐으면 runway 축소 |
| capital_discipline_dilution_risk | 12 | 증자, 희석, CAPEX 부담, 배당삭감, buyback 품질 강화 |
| information_confidence_disclosure_detail | 10 | 계약조건, price floor, 기간, AISC, 생산량, FCF detail 필요 |

## 케이스 방향

- Stage 2 후보: `MP Materials DoD/Apple price floor/offtake`, `Copper AI-grid record high`, `Barrick realized gold price/AISC/buyback`, `Equinox-Orla jurisdiction M&A`
- Event premium 분리: `Korea Zinc tender offer`
- 4C/RedTeam 후보: `Korea Zinc share issuance/probe`, `LG Chem/Lotte Chemical oversupply`, `Lithium -86%`, `Indonesia HPAL sulfur input-cost squeeze`
- Speculative cap: graphene, MXene, superconductor, paper/preprint/SNS-only science themes

## Guardrail

- production scoring은 변경하지 않았다.
- case record는 candidate-generation input이 아니다.
- 희토류 수출통제, 구리 가격 상승, 금 가격 상승, 화학 spread 반등, 공개매수, 과학테마만으로 Green을 만들지 않는다.
- price floor, offtake, 생산 ramp-up, realized price, AISC, cash cost, FCF, 자본환원, dilution, governance event, processing input cost를 실제 field로 확인해야 한다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round136_r4_loop8_materials_spread_strategic.py -v
PYTHONPATH=src python -m e2r.cli.build_round136_r4_loop8_report
```

결과:

- Round 136 전용 테스트 12개 통과
- v8 score profile 생성
- case JSONL 생성
- summary, guardrail, risk overlay, price validation, stage cap, score-stage-price alignment 리포트 생성

