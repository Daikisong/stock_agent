# Checkpoint 28A Round 129 R10 Loop 7

## 목적

`docs/round/round_129.md`의 R10 건설/부동산/건자재 Loop 7 내용을 calibration 자료로 반영했다.

이번 라운드의 핵심은 “부동산/데이터센터/건자재 테마”를 실제 현금흐름으로 검증하는 것이다. 예를 들어 데이터센터 수요가 강해도, 임차인 계약과 NOI/AFFO, 전력/물/허가가 없으면 Stage 3 근거가 아니라 Stage 1~2 관찰 신호로 남긴다.

## 반영 파일

- `src/e2r/sector/round129_r10_loop7_construction_real_estate_materials.py`
- `src/e2r/cli/build_round129_r10_loop7_report.py`
- `tests/test_round129_r10_loop7_construction_real_estate_materials.py`
- `data/e2r_case_library/cases_r10_loop7_round129.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round129_r10_loop7_v7.csv`
- `output/e2r_round129_r10_loop7_construction_real_estate_materials/`

## 핵심 반영

- R10 Loop 7 대상 archetype 28개를 별도 round129 팩으로 분리했다.
- 케이스 후보 25개를 유지하면서 Equinix, BXDC, Heidelberg, Holcim-Xella, Korea PF, BXMT, Fermi, Lineage 같은 성공/반례 축을 보존했다.
- `Round129BaseScoreAxis`를 추가해 R10 v7 기본 점수축 7개를 명시했다.
- 새 기본 점수축은 총 100점이다.
  - EPS/FCF/AFFO/NOI conversion: 24
  - asset/tenant/contract/PF visibility: 20
  - power/water/permitting/local acceptance: 16
  - cost ratio/price/volume/M&A synergy: 14
  - market mispricing/rerating gap: 8
  - valuation room/4B margin: 6
  - leverage/CAPEX/AFFO integrity/disclosure: 12
- 이 점수축은 production scoring 변경이 아니라, 다음 shadow scoring 설계를 위한 calibration 표다.

## Guardrails

- case record는 candidate-generation input으로 쓰지 않는다.
- StageClassifier, FeatureEngineering, RedTeam, E2R_STANDARD flow는 round129 팩을 import하지 않는다.
- PF 지원, AI 데이터센터 수요, 높은 배당수익률, 건자재 가격 인상, 재건 정책만으로 Stage 3-Green을 만들지 않는다.
- REIT/데이터센터는 AFFO per share, NOI, 배당 커버리지, 임차인 계약, 전력/물/허가, CAPEX integrity를 확인해야 한다.

## 생성 리포트

- `round129_r10_loop7_construction_real_estate_materials_summary.md`
- `round129_r10_loop7_case_matrix.csv`
- `round129_r10_loop7_stage_date_plan.csv`
- `round129_r10_loop7_green_guardrails.md`
- `round129_r10_loop7_risk_overlays.md`
- `round129_r10_loop7_price_validation_plan.md`
- `round129_r10_loop7_price_fields.csv`
- `round129_r10_loop7_base_score_axes.csv`

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round129_r10_loop7_construction_real_estate_materials.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round129_r10_loop7_report`

전체 테스트는 커밋 전 최종 검증에서 다시 수행한다.
