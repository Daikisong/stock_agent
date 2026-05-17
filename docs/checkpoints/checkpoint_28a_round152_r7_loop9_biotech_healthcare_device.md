# Checkpoint 28A Round 152 R7 Loop 9 Biotech / Healthcare / Medical Device

## 목적

`docs/round/round_152.md`의 R7 Loop 9 내용을 별도 calibration pack으로 반영했다.

R7은 CDMO, CRO, 바이오시밀러, GLP-1, 유전자치료제, 의료AI, 원격의료, 의료기기, 수술로봇, 보톡스·미용시술 안전 게이트를 다룬다. 이번 라운드의 핵심은 “허가·임상·논문·TAM”과 “상업화·반복매출·FCF”를 분리하는 것이다.

쉬운 예시는 다음과 같다.

- `FDA 승인`은 Stage 2 근거가 될 수 있지만, 처방량·보험·gross-to-net·OP/EPS가 없으면 Stage 3-Green 근거가 아니다.
- `CDMO 미국 생산거점`은 전략적 visibility지만, 고객계약·가동률·tech transfer·OPM/FCF가 확인되기 전에는 Stage 3가 아니다.
- `의료AI AUC 0.91`은 좋은 논문 근거지만, 병원 도입·수가·반복매출·subgroup 성능이 확인되어야 상업화 근거가 된다.
- `수술로봇 설치대수`는 출발점이고, procedure growth와 instruments/accessories 반복매출이 붙어야 구조적 후보가 된다.
- `GLP-1 TAM`이 커도 가격전쟁, copycat, compounded drug 규제, 보험 압박이 켜지면 4B/4C 감시가 먼저다.

## 반영 파일

- `src/e2r/sector/round152_r7_loop9_biotech_healthcare_device.py`
- `src/e2r/cli/build_round152_r7_loop9_report.py`
- `tests/test_round152_r7_loop9_biotech_healthcare_device.py`
- `data/e2r_case_library/cases_r7_loop9_round152.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round152_r7_loop9_v9.csv`
- `output/e2r_round152_r7_loop9_biotech_healthcare_device/`

## v9 기본 점수축

| component | weight | 해석 |
| --- | ---: | --- |
| eps_fcf_commercialization_conversion | 24 | 승인·임상·논문이 처방, 매출, OPM, FCF, cash runway로 전환되는지 확인 |
| prescription_reimbursement_recurring_visibility | 22 | scripts, PBM/보험, 수가, procedure growth, 반복소모품, CDMO 가동률 |
| barrier_recurring_bottleneck | 14 | installed base, 장기계약, regulatory barrier, switching cost, 반복성 |
| cash_runway_capital_discipline | 10 | cash runway, 희석, take-private, CAPEX 부담, funding cycle |
| market_mispricing_rerating_gap | 8 | 승인/TAM/capacity old-frame이 상업화 증거 뒤에도 남아 있는지 확인 |
| valuation_room_4b_runway | 6 | GLP-1, 수술로봇, CDMO, 의료AI narrative가 이미 crowded인지 확인 |
| safety_regulatory_disclosure_confidence | 16 | FDA/DOJ, 특허소송, reimbursement, subgroup, counterfeit, safety, disclosure detail 강화 |

## 케이스 방향

- Stage 2 후보: `Samsung Biologics Rockville facility`, `Lilly Foundayo approval`, `Humira biosimilar PBM/access`, `Lunit DBT external validation`
- Stage 2→3 후보: `Intuitive Surgical procedure growth + instruments/accessories`
- 4B→4C / RedTeam: `Novo GLP-1 price pressure`, `Hims GLP-1 telehealth pivot`, `Bluebird cash crunch`, `Charles River CRO funding crunch`, `Teladoc impairment`, `Amgen-Samsung Bioepis patent litigation`, `Botox counterfeit safety`

## Guardrail

- production scoring은 변경하지 않았다.
- case record는 candidate-generation input이 아니다.
- FDA 승인, 임상 성공, AI AUC, CDMO capacity, GLP-1 TAM만으로 Green을 만들지 않는다.
- Stage 3는 처방량, 보험·PBM·수가, commercial revenue, 반복시술·소모품, 가동률, OPM/FCF, cash runway, safety/regulatory gate, 실제 가격경로 동행을 요구한다.
- 승인 후 uptake 실패, reimbursement failure, cash crunch, funding crunch, compounded GLP-1 crackdown, patent litigation, subgroup AI failure, device safety/counterfeit는 RedTeam overlay로 유지한다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round152_r7_loop9_biotech_healthcare_device.py -v
PYTHONPATH=src python -m e2r.cli.build_round152_r7_loop9_report
```

결과:

- Round 152 전용 테스트 14개 통과
- v9 score profile 생성
- case JSONL 생성
- summary, guardrail, risk overlay, price validation, stage cap, score-stage-price alignment 리포트 생성
