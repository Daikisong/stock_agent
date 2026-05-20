# Checkpoint 28A Round 280 R11 Loop 13 정책·지정학·재난 이벤트 검증팩

## 요약

- 원문: `docs/round/round_280.md`
- analyst round id: `round_208`
- 대섹터: `POLICY_GEOPOLITICS_DISASTER_EVENT`
- 케이스 수: 8
- production scoring 변경: false
- candidate generation input: false
- shadow weight only: true
- 가격 검증 상태: `partial_with_reported_price_anchors`
- full adjusted OHLC: false

이번 라운드는 정책, 지정학, 환율, 에너지, 노동, 관세, 수출통제, 재난 이벤트가 회사의 Stage 3-Green 증거처럼 오인되는 것을 막기 위한 보정 팩이다.

쉬운 예로, 자동차 관세가 25%에서 15%로 낮아졌다는 뉴스는 relief다. 그러나 기업별 gross margin, 가격 전가, 현지 생산 economics, FCF bridge가 확인되지 않으면 Stage 3-Green 증거가 아니다.

## 추가된 canonical archetype

- `POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE`
- `MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C`
- `AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT`
- `SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION`
- `US_KOREA_TARIFF_POLICY_4C_WATCH`
- `CHINA_FAB_EXPORT_LICENSE_RELIEF`
- `CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE`

기존 `RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C`와 함께 라운드 280 타깃 8개 archetype을 구성한다.

## 케이스 반영

| case | 판정 |
|---|---|
| martial law / Korea discount | 정치 충격 hard 4C reference |
| Iran / Middle East energy-FX shock | macro hard 4C |
| AI windfall / citizen dividend discussion | event premium / 4B-watch |
| Samsung strike / emergency arbitration | systemic labor supply-chain 4C-watch |
| China rare-earth export controls | supply-chain license 4C-watch |
| U.S.-Korea tariff policy | tariff margin bridge 4C-watch + policy relief |
| Samsung/SK Hynix China fab tool license | annual license Stage 2 relief candidate |
| 2025 South Korea wildfires | disaster loss hard reference |

## Green 필수 확인

- 법안, 예산, 시행 확인
- 기업별 EPS/FCF bridge
- 관세 gross margin bridge
- 가격 전가와 현지 생산 economics
- FX/energy hedge
- 실제 supply-chain license, 재고, 대체조달
- 노동 생산연속성
- 재난 피해 산정과 복구계약 margin
- sovereign credit / FX 안정
- 증거 이후 가격경로

## 금지 패턴

- 정책 headline만으로 Green 처리
- 실행 없는 relief package
- margin bridge 없는 tariff cut
- 실제 license 없는 rare-earth truce
- 해결되지 않은 strike risk
- 법안 없는 AI tax/bonus comment
- 피해 산정 없는 disaster rebuild story
- 지정학 리스크 무시
- annual license를 multiyear visibility로 취급

## 산출물

- `data/e2r_case_library/cases_r11_loop13_round280.jsonl`
- `data/sector_taxonomy/round280_r11_loop13_policy_geopolitical_disaster_event_price_validation_audit.json`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_price_validation_summary.md`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_case_matrix.csv`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_target_aliases.csv`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_score_adjustments.csv`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_shadow_weights.csv`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_deep_sub_archetypes.csv`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_price_validation_fields.csv`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_green_gate_review.md`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_price_validation_plan.md`
- `output/e2r_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation/round280_r11_loop13_stage4b_4c_review.md`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round280_r11_loop13_policy_geopolitical_disaster_event_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round280_r11_loop13_report
PYTHONPATH=src python -m compileall -q src tests
git diff --check
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

- 라운드 280 전용 단위 테스트 6개 통과
- CLI 산출물 생성 완료
- compileall 통과
- `git diff --check` 통과
- 전체 unittest 3,214개 통과

테스트 후 생성된 `__pycache__`는 커밋 전 정리했다.
