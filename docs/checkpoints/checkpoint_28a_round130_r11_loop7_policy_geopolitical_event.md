# Checkpoint 28A Round 130 R11 Loop 7

## 목적

`docs/round/round_130.md`의 R11 정책/지정학/재난/이벤트 Loop 7 내용을 calibration 자료로 반영했다.

이번 라운드의 핵심은 “뉴스가 크다”와 “돈이 실제로 묶였다”를 분리하는 것이다. 예를 들어 전염병 뉴스는 Stage 1 라우팅 신호가 될 수 있지만, 정부 stockpile 계약, 계약금액, 매출 가이던스 상향, EBITDA margin 상향이 붙어야 Stage 2 후보가 된다.

## 반영 파일

- `src/e2r/sector/round130_r11_loop7_policy_geopolitical_event.py`
- `src/e2r/cli/build_round130_r11_loop7_report.py`
- `tests/test_round130_r11_loop7_policy_geopolitical_event.py`
- `data/e2r_case_library/cases_r11_loop7_round130.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round130_r11_loop7_v7.csv`
- `output/e2r_round130_r11_loop7_policy_geopolitical_event/`

## 핵심 반영

- R11 Loop 7 대상 canonical archetype 24개를 별도 round130 팩으로 분리했다.
- 케이스 후보 18개를 유지했다.
  - Stage 2 후보: Bavarian Nordic stockpile, Ukraine critical infra financing, China rare-earth export control, climate-to-grid infrastructure.
  - Event premium: China group visa tourism policy, disaster rebuild material, local policy theme.
  - RedTeam/4C: Moderna BARDA cancellation, North Korea Kumgang dismantling, LK-99 replication failure, Abbott diagnostics normalization.
  - 4B-watch: AI citizen dividend policy shock.
- `Round130BaseScoreAxis`를 추가해 R11 v7 기본 점수축 7개를 명시했다.
- 새 기본 점수축은 총 100점이다.
  - actual contract / budget / order / financing visibility: 28
  - EPS/FCF / revenue guidance conversion: 20
  - recurrence / durability: 14
  - bottleneck / policy intensity / geopolitical reality: 12
  - market mispricing / rerating gap: 8
  - valuation room / 4B margin: 6
  - RedTeam / disclosure confidence: 12

## Guardrails

- case record는 candidate-generation input으로 쓰지 않는다.
- StageClassifier, FeatureEngineering, RedTeam, E2R_STANDARD flow는 round130 팩을 import하지 않는다.
- 정책 발표, 재건회의, 수출통제 headline, 관광정책, 논문/preprint만으로 Stage 3-Green을 만들지 않는다.
- 정부계약 취소, funding withdrawal, 수요 정상화, 재현 실패, 시설 철거, 정책 shock은 RedTeam/4C 성격으로 유지한다.
- OpenDART/news detail에서 계약금액, 예산, 정부주문, financing, 공사착수, 매출 인식이 확인되지 않으면 Stage 3를 cap한다.

## 생성 리포트

- `round130_r11_loop7_policy_geopolitical_event_summary.md`
- `round130_r11_loop7_case_matrix.csv`
- `round130_r11_loop7_stage_date_plan.csv`
- `round130_r11_loop7_green_guardrails.md`
- `round130_r11_loop7_event_false_positive_caps.md`
- `round130_r11_loop7_price_validation_plan.md`
- `round130_r11_loop7_price_fields.csv`
- `round130_r11_loop7_base_score_axes.csv`

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round130_r11_loop7_policy_geopolitical_event.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round130_r11_loop7_report`

전체 테스트는 커밋 전 최종 검증에서 다시 수행한다.
