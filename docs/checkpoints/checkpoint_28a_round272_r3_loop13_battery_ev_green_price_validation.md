# Checkpoint 28A Round 272 R3 Loop 13 Battery EV Green Price Validation

## 반영 요약

`docs/round/round_272.md`의 R3 Loop 13 내용을 케이스 라이브러리용 구조화 자료로 반영했다. 이번 라운드는 2차전지·EV·친환경 대섹터에서 `Tesla`, `ESS`, `LFP`, `IRA`, `FEOC`, `배터리 소재` 같은 단어만으로 Stage 3-Green을 만들면 안 된다는 가격검증 팩이다.

예를 들면 L&F/Tesla 4680 양극재 계약은 처음에는 큰 계약처럼 보였지만, 실제 계약가치가 `$2.9B`에서 `$7,386`으로 줄었다. 이 경우 핵심은 고객명이나 최초 계약금액이 아니라 실제 call-off, 납품량, 가동률, 마진이다.

## 추가한 항목

- 신규 R3 Loop 13 canonical archetype 8개
- 라운드 272 전용 케이스 팩 모듈
- 라운드 272 리포트 생성 CLI
- 케이스 JSONL, taxonomy audit JSON, output 리포트 CSV/MD
- 단위 테스트 7개

## 케이스 요약

| case | 판정 |
|---|---|
| L&F / Tesla 4680 cathode | hard 4C. 계약가치가 사실상 붕괴 |
| LGES / Tesla LFP ESS | Stage 2. GWh, shipment, margin, ex-subsidy OP 전 Green 금지 |
| LGES Q2 2025 IRA quality | headline OP는 좋지만 ex-IRA OP 품질 게이트 실패 |
| LG Chem / LGES stake sale | capital recycling Stage 2. ROIC와 부채감축 확인 필요 |
| Samsung SDI / Tesla ESS report | 회사 미확정 보도이므로 event premium |
| EcoPro Materials precursor | IPO/수직계열화 story만으로 부족한 failed rerating |
| Aricell / S-Connect | battery safety hard reference |
| FEOC / graphite policy | sector relief. 회사별 계약·인증·마진 전 Green 금지 |

## 산출물

- `src/e2r/sector/round272_r3_loop13_battery_ev_green_price_validation.py`
- `src/e2r/cli/build_round272_r3_loop13_report.py`
- `tests/test_round272_r3_loop13_battery_ev_green_price_validation.py`
- `data/e2r_case_library/cases_r3_loop13_round272.jsonl`
- `data/sector_taxonomy/round272_r3_loop13_battery_ev_green_price_validation_audit.json`
- `output/e2r_round272_r3_loop13_battery_ev_green_price_validation/`

## Green Gate

R3 Stage 3-Green은 다음 증거가 닫혀야 가능하다.

- signed contract + actual call-off
- GWh 또는 소재 물량
- 납품 시작 또는 매출 인식
- utilization 개선
- 보조금 제외 OP 품질
- margin / FCF 개선
- 고객 EV/ESS 프로그램 건강도
- safety / quality risk 해소
- FEOC 관련 탈중국 공급·인증
- 증거 이후 따라온 가격 경로

금지 패턴도 명시했다.

- 고객명 headline only
- contract value without call-off
- 회사 확인 없는 reported deal
- IRA subsidy-driven OP only
- policy support only
- IPO vertical-integration story only
- battery safety incident unresolved

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round272_r3_loop13_battery_ev_green_price_validation -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round272_r3_loop13_report
```

결과:

- 라운드 272 단위 테스트 7개 통과
- compileall 통과
- 리포트 생성 CLI 정상 실행

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation input 변경 없음
- StageClassifier threshold 변경 없음
- case library를 scoring input으로 사용하지 않음
- full OHLC가 없는 항목은 임의 MFE/MAE를 만들지 않음

## 다음 작업

R3는 이제 고객명/정책/보조금/headline을 더 엄격히 분리한다. 다음 R3 scoring shadow 실험을 할 때는 `actual_calloff`, `GWh_volume_disclosed`, `ex_subsidy_OP_quality`, `battery_safety_quality`, `non_China_sourcing_certification` 축을 별도 진단 점수로만 먼저 비교해야 한다.
