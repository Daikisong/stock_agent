# Checkpoint 28A Round 155 R10 Loop 9

## 목적

`docs/round/round_155.md`의 R10 건설/부동산/건자재 Loop 9 내용을 calibration 자료로 반영했다.

이번 라운드의 핵심은 “부동산/데이터센터/건자재 테마”를 실제 현금흐름으로 검증하는 것이다. 예를 들어 데이터센터 수요가 강해도, 임차인 계약과 NOI/AFFO, 전력/물/허가가 없으면 Stage 3 근거가 아니라 Stage 1~2 관찰 신호로 남긴다.

## 반영 파일

- `src/e2r/sector/round155_r10_loop9_construction_real_estate_materials.py`
- `src/e2r/cli/build_round155_r10_loop9_report.py`
- `tests/test_round155_r10_loop9_construction_real_estate_materials.py`
- `data/e2r_case_library/cases_r10_loop9_round155.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round155_r10_loop9_v9.csv`
- `output/e2r_round155_r10_loop9_construction_real_estate_materials/`

## 핵심 반영

- R10 Loop 9 대상 archetype 28개를 별도 round155 팩으로 분리했다.
- 케이스 후보 25개를 유지하면서 Equinix, BXDC, Heidelberg, Holcim-Xella, Korea PF, BXMT, Fermi, Lineage 같은 성공/반례 축을 보존했다.
- `DATA_CENTER_LOCAL_OPPOSITION_OVERLAY`를 반영해 moratorium보다 넓은 지역 반발, zoning, 소음, 주민 수용성 gate를 명시했다.
- `Round155BaseScoreAxis`를 추가해 R10 v9 기본 점수축 7개를 명시했다.
- 새 기본 점수축은 총 100점이다.
  - EPS/FCF/AFFO/NOI conversion: 24
  - asset/tenant/contract/PF visibility: 20
  - power/water/permitting/local acceptance: 16
  - cost/price/volume/M&A synergy: 14
  - leverage/CAPEX/AFFO integrity/disclosure: 12
  - market mispricing/rerating gap: 8
  - valuation room/4B margin: 6
- 이 점수축은 production scoring 변경이 아니라, 다음 shadow scoring 설계를 위한 calibration 표다.
- Stage cap도 별도 CSV로 만들었다.
  - Stage 1 headline cap: PF 지원, 금리 인하 기대, AI 데이터센터 이름표, 재건 정책, 고배당만 있으면 최대 45점 관찰 신호다.
  - Stage 2 cash-flow visibility cap: 자산/임차인/NOI/AFFO/PF refinancing/M&A 주장만 있고 교차증거가 약하면 최대 70점이다.
  - Stage 3 cross-evidence gate: 70점을 넘더라도 현금흐름, 독립 증거, 가격경로, RedTeam clean이 필요하다.

## Guardrails

- case record는 candidate-generation input으로 쓰지 않는다.
- StageClassifier, FeatureEngineering, RedTeam, E2R_STANDARD flow는 round155 팩을 import하지 않는다.
- PF 지원, AI 데이터센터 수요, 높은 배당수익률, 건자재 가격 인상, 재건 정책만으로 Stage 3-Green을 만들지 않는다.
- REIT/데이터센터는 AFFO per share, NOI, 배당 커버리지, 임차인 계약, 전력/물/허가, CAPEX integrity를 확인해야 한다.
- 쉬운 예: 데이터센터 REIT IPO가 있어도 아직 자산을 사지 않았고 임차인 계약도 없으면 Stage 1~2 관찰 신호다. `NOI/AFFO`, `tenant lease`, `power/water secured`가 확인되기 전에는 Green 근거가 아니다.

## 생성 리포트

- `round155_r10_loop9_construction_real_estate_materials_summary.md`
- `round155_r10_loop9_case_matrix.csv`
- `round155_r10_loop9_stage_date_plan.csv`
- `round155_r10_loop9_green_guardrails.md`
- `round155_r10_loop9_risk_overlays.md`
- `round155_r10_loop9_price_validation_plan.md`
- `round155_r10_loop9_price_fields.csv`
- `round155_r10_loop9_base_score_axes.csv`
- `round155_r10_loop9_stage_caps.csv`

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round155_r10_loop9_construction_real_estate_materials.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round155_r10_loop9_report`
- `PYTHONPATH=src python -m compileall -q src tests`
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- `git diff --check`

결과:

- Round 155 전용 테스트 13개 통과
- 전체 unittest 1,997개 통과
- compileall 통과
- git diff whitespace check 통과
- case JSONL, v9 score profile, stage cap, summary/risk/guardrail/price validation 리포트 생성
