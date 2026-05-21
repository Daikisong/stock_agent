# Checkpoint 28A Round 330 R9 Loop 17 Mobility / Transport / Leisure

## 반영 범위

- 입력 문서: `docs/round/round_330.md`
- analyst round id: `round_258`
- 대섹터: `MOBILITY_TRANSPORT_LEISURE`
- 방법: `trigger_level_backtest_v1_after_redteam`
- production scoring 변경: `false`
- shadow weight only: `true`
- full adjusted OHLC 완료: `false`

이번 패치는 모빌리티, 항공, 관광, 해양 애프터마켓, 조선/운송 인프라의 trigger-level calibration을 케이스 라이브러리로 옮긴 것이다. 예를 들어 현대차 하이브리드/value-up은 `Stage2-Actionable`이지만, 관세와 현지화 마진이 닫히지 않으면 Stage 3-Green으로 올리지 않는다.

## 추가된 canonical archetype

- `AUTO_TARIFF_LOCALIZATION_4B`
- `MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT`
- `AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE`
- `LCC_SAFETY_TRUST_HARD_4C`
- `CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE`
- `MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE`
- `SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE`

기존 `AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE`도 이번 라운드 target으로 사용했다.

## 생성된 산출물

- `data/e2r_case_library/cases_r9_loop17_round258.jsonl`
- `data/e2r_trigger_calibration/triggers_r9_loop17_round258.jsonl`
- `data/sector_taxonomy/round330_r9_loop17_mobility_transport_leisure_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round258_r9_loop17_v1.csv`
- `output/e2r_round330_r9_loop17_mobility_transport_leisure_trigger_validation/round330_summary.md`
- `output/e2r_round330_r9_loop17_mobility_transport_leisure_trigger_validation/trigger_grid.md`
- `output/e2r_round330_r9_loop17_mobility_transport_leisure_trigger_validation/stage_rules.md`
- `output/e2r_round330_r9_loop17_mobility_transport_leisure_trigger_validation/stage4b_4c_review.md`
- `output/e2r_round330_r9_loop17_mobility_transport_leisure_trigger_validation/price_validation_plan.md`

## 케이스 요약

- Hyundai Motor hybrid + value-up: `Stage2-Actionable`
- Hyundai/Kia U.S. auto tariff: `4B-watch`
- Hyundai/Kia robotics / AI factory: `Stage2 overheat / Yellow candidate`
- Korean Air / Asiana consolidation: `Stage2 no-price`
- Jeju Air fatal crash: `hard 4C`
- China visa-free tourism leisure basket: `Stage2-Actionable`
- HD Hyundai Marine Solution IPO: `Stage2-Actionable`
- HD Hyundai Heavy / Hyundai Mipo MASGA merger: `Stage2-Actionable`

## Green 차단 원칙

- 자동차 성장은 관세 조정 후 마진이 확인돼야 한다.
- 로보틱스/AI factory는 매출, 생산성, capex ROI가 없으면 Green이 아니다.
- 항공 합병은 yield, load factor, cost synergy가 필요하다.
- 관광 정책은 방문객 수보다 basket size와 OP conversion이 중요하다.
- 해양 IPO와 조선 합병은 cycle, overhang, 실제 contract/execution gate가 남아 있다.
- fatal safety event는 hard 4C로 분리한다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round330_r9_loop17_mobility_transport_leisure_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round330_r9_loop17_report
```

결과:

- 라운드 330 전용 테스트 통과.
- 케이스 JSONL, 트리거 JSONL, audit JSON, shadow weight CSV, markdown 리포트 생성 완료.
- MFE/MAE/peak/drawdown은 full adjusted OHLC가 없으므로 생성하지 않았다.

## 다음 작업

R10 Loop 17에서는 건설, 부동산, 건자재 쪽에서 같은 방식으로 trigger-level price validation을 추가한다. 특히 수주/분양/PF/원가율을 구분해야 하며, 단순 수주 뉴스가 cash-flow 개선으로 이어졌는지를 별도로 검증해야 한다.
