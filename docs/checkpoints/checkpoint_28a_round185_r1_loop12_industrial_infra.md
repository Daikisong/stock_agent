# Checkpoint 28A Round 185 R1 Loop 12 Industrial Orders / Infrastructure

`docs/round/round_185.md`의 R1 Loop 12 내용을 calibration pack으로 반영했다.

이번 라운드는 기존 R1 대형 대표주 반복을 줄이고, 국장 중심 중소형 전력설비·전선·방산전자·우주발사체·건설기계·원전해체·조선기자재 후보를 다시 정리한다. 핵심은 “수주 뉴스가 있다”가 아니라 계약 detail, OP/EPS/FCF 전환, 가격경로, 자본규율, 지배구조, 공시 신뢰도를 같이 보는 것이다.

## 반영 파일

- `src/e2r/sector/round185_r1_loop12_industrial_infra.py`
- `src/e2r/cli/build_round185_r1_loop12_report.py`
- `tests/test_round185_r1_loop12_industrial_infra.py`
- `data/e2r_case_library/cases_r1_loop12_round185.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round185_r1_loop12_v12.csv`
- `output/e2r_round185_r1_loop12_industrial_infra/`

## 추가 Archetype

- `GRID_TRANSFORMER_MIDCAP_KOREA`
- `POWER_CABLE_GRID_BACKLOG_KOREA`
- `DEFENSE_ELECTRONICS_KF21_RADAR`
- `SPACE_LAUNCH_PROGRAM_OF_RECORD`
- `DEFENSE_CAPITAL_RAISE_DILUTION`
- `CONSTRUCTION_EQUIPMENT_CYCLE_KOREA`
- `CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY`
- `NUCLEAR_DECOMMISSIONING_KOREA`
- `NUCLEAR_POLICY_STAGE1_2_NOT_GREEN`
- `SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA`
- `SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK`

## Stage 기준

Stage 3 조기 포착은 8개 조건 중 5개 이상을 요구한다.

- 고객명·계약금액·납품기간 확정
- 수주잔고 증가와 장기 납품 visibility
- OP/EPS 상향 또는 분기 OP beat
- OPM 또는 FCF 개선
- Stage 2 이후 60D MFE +20% 이상
- KOSPI/KOSDAQ 대비 상대강도 우위
- 증자·CB·지배구조 hard issue 없음
- valuation 과열 전

예를 들어 일진전기나 조선기자재 basket은 후보가 될 수 있지만, 고객명·계약금액·납품기간·OPM이 비어 있으면 Stage 3가 아니라 Stage 2 또는 4B-watch로 남는다.

## RedTeam

- 한화에어로스페이스: KSLV-III와 방산 program은 Stage 2 strong이지만, 대규모 증자·금감원 정정 요구·희석은 Green 차단 요소다.
- 두산밥캣: cash flow가 좋아도 지배구조와 소수주주 가치 훼손 우려가 있으면 governance cap이다.
- 한화시스템: KF-21 radar는 Stage 2 evidence지만, Eutelsat/OneWeb 투자손실은 별도 자본배분 4C-watch다.
- 원전 정책: 국가 에너지 계획은 research routing evidence일 뿐 개별 종목 Stage 3 근거가 아니다.

## 안전장치

- production scoring은 변경하지 않았다.
- case library는 candidate-generation input이 아니다.
- 정책, MOU/LOI, media-only, OpenDART list-only, price-only rotation은 Stage 3-Green을 만들 수 없다.
- 가격, 계약금액, 마진, MFE/MAE, 고객명, 납품기간은 backfill 대상으로 남겼고 임의로 채우지 않았다.

## 다음 작업

R1 Loop 12 산출물은 가격경로와 공시 detail backfill 우선순위를 만든다. 다음에는 전력설비·전선·조선기자재 후보의 실제 KRX 가격경로, OpenDART detail, OP/EPS revision을 채워서 Stage 2와 Stage 3의 경계를 검증해야 한다.
