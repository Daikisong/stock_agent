# Checkpoint 28A Round 245 R2 Loop 11 AI Semiconductor Price Validation

## 목적

`docs/round/round_245.md`를 R2 Loop 11 AI·반도체·전자부품 가격경로 검증 팩으로 구조화했다. 이번 작업은 케이스 라이브러리와 shadow calibration 산출물만 추가하며, 생산 scoring, StageClassifier, candidate generation은 바꾸지 않는다.

쉬운 예시:

- SK하이닉스는 HBM/EUV/advanced packaging 증거가 맞물린 구조적 성공 사례지만, 큰 가격 재평가 이후에는 신규 Green보다 `4B-watch` 관리가 중요하다.
- 한미반도체의 SK하이닉스 확정 계약은 Stage 2 증거다. 반대로 Micron 미확정 보도로 장중 +22% 움직인 부분은 Green 증거가 아니라 `4B-watch`다.
- 삼성전자의 foundry 계약과 AMD MoU는 Stage 2 후보 증거지만, HBM/foundry volume shipment, margin, EPS/FCF 전환과 labor/export/IP RedTeam을 통과하기 전에는 Green이 아니다.

## 반영 파일

- `src/e2r/sector/archetypes.py`
- `src/e2r/sector/round245_r2_loop11_ai_semiconductor_price_validation.py`
- `src/e2r/cli/build_round245_r2_loop11_report.py`
- `tests/test_round245_r2_loop11_ai_semiconductor_price_validation.py`
- `data/e2r_case_library/cases_r2_loop11_round245.jsonl`
- `data/sector_taxonomy/round245_r2_loop11_ai_semiconductor_price_validation_audit.json`
- `output/e2r_round245_r2_loop11_ai_semiconductor_price_validation/`

## 추가한 아키타입

Round 245가 요구한 R2 세부 archetype을 canonical enum으로 보존했다.

- `MEMORY_HBM_CAPACITY_LEADER`
- `HBM_EUV_ADVANCED_PACKAGING_CAPEX`
- `FOUNDRY_TURNAROUND_CONTRACT`
- `HBM_BONDER_EQUIPMENT`
- `CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF`
- `SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY`
- `SEMICONDUCTOR_IP_LEAK_REDTEAM`

기존 enum이던 다음 항목은 이번 라운드 기준에 맞게 정의를 보강했다.

- `HBM_CATCHUP_EXECUTION`
- `SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER`
- `POLICY_FOUNDRY_EVENT`
- `GEOPOLITICAL_EXPORT_CONTROL_OVERLAY`

## 케이스 요약

총 8개 케이스를 추가했다.

| case | 해석 |
|---|---|
| SK Hynix | HBM/EUV/advanced packaging 구조적 성공 benchmark, 현재는 4B-watch |
| Samsung Electronics | foundry/HBM catch-up Stage 2 후보, strike/export/IP 4C-watch |
| Hanmi Semiconductor | 확정 SK Hynix order는 Stage 2, 미확정 Micron rumor +22%는 4B-watch |
| Jusung / Mirae | CXMT entity-list 제외 relief event, China customer concentration과 export-control watch |
| Gaonchips | Preferred Networks design win Stage 2, 양산·매출·마진 전 Green 금지 |
| DB HiTek policy foundry | 정부 foundry 정책 Stage 1~2, 회사 단위 order/utilization 전 Green 금지 |
| Hanwha Precision spin-off | HBM 장비 optionality지만 corporate action event premium |
| Export-control/IP-leak basket | Samsung/SK Hynix/Hana Micron/Hanmi 4C-watch overlay |

## Green Gate

R2 Stage 3-Green은 다음을 요구한다.

- company-level customer evidence
- product-specific exposure
- order / shipment / contract / revenue path
- gross margin 또는 OPM 개선
- EPS/FCF revision
- capacity bottleneck 또는 supply allocation
- customer diversification
- export-control / China fab / labor / IP leakage / accounting trust 통과
- evidence 이후 가격경로 확인

반대로 다음은 Green 금지 패턴이다.

- AI keyword만 있음
- HBM rumor만 있음
- 미확정 고객 보도
- design win without revenue
- policy foundry without order
- spin-off / corporate action only
- China customer concentration only
- labor/export-control/IP risk ignored
- price rally before confirmation

## 산출물

생성한 산출물:

- `round245_r2_loop11_price_validation_summary.md`
- `round245_r2_loop11_case_matrix.csv`
- `round245_r2_loop11_target_aliases.csv`
- `round245_r2_loop11_score_adjustments.csv`
- `round245_r2_loop11_shadow_weights.csv`
- `round245_r2_loop11_deep_sub_archetypes.csv`
- `round245_r2_loop11_price_validation_fields.csv`
- `round245_r2_loop11_green_gate_review.md`
- `round245_r2_loop11_price_validation_plan.md`
- `round245_r2_loop11_stage4b_4c_review.md`

## 검증

실행한 핵심 검증:

```bash
PYTHONPATH=src python -m py_compile \
  src/e2r/sector/archetypes.py \
  src/e2r/sector/round245_r2_loop11_ai_semiconductor_price_validation.py \
  src/e2r/cli/build_round245_r2_loop11_report.py \
  tests/test_round245_r2_loop11_ai_semiconductor_price_validation.py

PYTHONPATH=src python -m unittest tests.test_round245_r2_loop11_ai_semiconductor_price_validation -v

PYTHONPATH=src python -m e2r.cli.build_round245_r2_loop11_report
```

최종 전체 테스트와 `git diff --check`는 커밋 전 검증 단계에서 수행한다.

## 변경하지 않은 것

- 생산 scoring threshold 변경 없음
- StageClassifier threshold 변경 없음
- case library를 candidate generation 입력으로 사용하지 않음
- 종목명을 scoring/staging/red-team 로직 조건으로 사용하지 않음
- full OHLC가 없는 MFE/MAE를 조작하지 않음
- 4C-watch를 hard 4C로 억지 확정하지 않음
