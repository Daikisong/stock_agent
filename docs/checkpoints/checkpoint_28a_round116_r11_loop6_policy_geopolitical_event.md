# Checkpoint 28A Round 116 R11 Loop 6 Policy / Geopolitical / Disaster / Event

## Purpose

Round 116 반영은 R11 정책·지정학·재난·이벤트 라운드의 Loop 6 데이터팩이다.

핵심 기준은 단순하다.

- 큰 뉴스는 Stage 1 라우팅 증거가 될 수 있다.
- Stage 2 이상은 실제 계약, 정부 주문, 예산, financing, 착공, 매출, EPS/FCF 전환이 필요하다.
- Stage 3-Green은 이번 라운드에서도 완화하지 않는다.

쉬운 예시:

- 엠폭스 뉴스만 있으면 `EVENT_DISEASE_PEST_DEMAND`이고 Event/Red 성격이다.
- Bavarian Nordic처럼 정부 stockpile 계약과 매출·EBITDA 가이던스 상향이 같이 있으면 `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE` Stage 2 후보가 된다.
- 희토류 수출통제는 macro bottleneck 증거지만, 개별 기업은 생산능력, offtake, price floor, 매출, FCF가 확인되기 전까지 Green 후보가 아니다.

## Added Or Extended Archetypes

- `STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT`
- `EXPORT_CONTROL_TO_OFFTAKE_ESCALATION`
- `TOURISM_POLICY_EVENT`
- `AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK`

## Generated Data

- `src/e2r/sector/round116_r11_loop6_policy_geopolitical_event.py`
- `src/e2r/cli/build_round116_r11_loop6_report.py`
- `tests/test_round116_r11_loop6_policy_geopolitical_event.py`
- `data/e2r_case_library/cases_r11_loop6_round116.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round116_r11_loop6_v6.csv`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_policy_geopolitical_event_summary.md`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_case_matrix.csv`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_stage_date_plan.csv`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_green_guardrails.md`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_event_false_positive_caps.md`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_price_validation_plan.md`
- `output/e2r_round116_r11_loop6_policy_geopolitical_event/round116_r11_loop6_price_fields.csv`

## Summary Counts

- target_count: 24
- case_candidate_count: 18
- success_candidate_count: 7
- event_premium_count: 5
- stage4b_case_count: 3
- stage4c_case_count: 5
- watch_yellow_first_count: 12
- redteam_first_count: 12
- gate_only_target_count: 4
- price_fields: 153

## Guardrails

- Case records are calibration/evaluation only.
- Production scoring, staging, RedTeam, and E2R_STANDARD flow do not import the Round 116 pack.
- No API keys or secrets are stored.
- No stage price is invented.
- No contract, budget, order, financing, guidance, or revenue field is invented.
- Stage 3-Green thresholds are not changed.

## Validation

Commands run:

```bash
find src tests -type d -name __pycache__ -prune -exec rm -rf {} +
PYTHONPATH=src python -m unittest tests.test_round116_r11_loop6_policy_geopolitical_event -v
PYTHONPATH=src python -m e2r.cli.build_round116_r11_loop6_report
```

Round-specific tests passed:

- 10 tests OK

Full-suite validation is recorded in the final round response after the repository-wide test run.

## Production Impact

No production scoring change was applied.

Round 116 only expands the case library and score-weight draft material. The main scoring engine should later consume this only through an explicit shadow/scoring-calibration checkpoint, not through hidden imports.
