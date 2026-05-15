# Checkpoint 28A Round 20: Score-Weight v0.6 Research Matrix

## 목적

Round 20은 production scoring 적용이 아니라, 얇았던 sub-archetype의 점수비중 가설을 더 정리하는 단계다.

쉬운 예시:

- `액침냉각`이라는 테마명이 있다고 점수가 올라가면 안 된다.
- 실제 고객, 수주, 납품 시점, 매출 인식, 마진 근거가 있어야 AI 데이터센터 냉각 후보로 볼 수 있다.
- 즉, 테마명은 검색 라벨이고 점수는 증거에서만 나온다.

## 반영 파일

추가한 코드:

- `src/e2r/sector/round20_score_weight_v06.py`
- `src/e2r/cli/build_round20_score_weight_report.py`
- `tests/test_round20_score_weight_v06.py`

생성한 데이터/리포트:

- `data/sector_taxonomy/score_weight_profiles_round20_v06.csv`
- `data/sector_taxonomy/theme_tag_map_round20_v06.csv`
- `output/e2r_round20_score_weight_v06/round20_score_weight_v06_summary.md`
- `output/e2r_round20_score_weight_v06/round20_score_weight_targets.csv`
- `output/e2r_round20_score_weight_v06/round20_theme_policy_v06.md`
- `output/e2r_round20_score_weight_v06/round20_case_candidate_plan.md`
- `output/e2r_round20_score_weight_v06/round20_shadow_scoring_next_plan.md`

## 대상

이번 v0.6 대상은 10개다.

- `RAIL_INFRASTRUCTURE`
- `AI_DATA_CENTER_COOLING`
- `WASTE_RECYCLING_ENVIRONMENT`
- `SECURITY_IDENTITY_DEEPFAKE`
- `CLOUD_AI_SOFTWARE_INFRA`
- `EDUCATION_SPECIALTY_SERVICES`
- `APPAREL_BRAND_OEM`
- `BUILDING_MATERIALS_CYCLE`
- `REIT_DEVELOPMENT_TRUST`
- `CRO_CLINICAL_SERVICE`

## 정책 요약

Green 가능으로 분류한 research profile:

- `AI_DATA_CENTER_COOLING`
- `WASTE_RECYCLING_ENVIRONMENT`
- `CLOUD_AI_SOFTWARE_INFRA`

Watch/Yellow 우선:

- `RAIL_INFRASTRUCTURE`
- `SECURITY_IDENTITY_DEEPFAKE`
- `EDUCATION_SPECIALTY_SERVICES`
- `APPAREL_BRAND_OEM`
- `BUILDING_MATERIALS_CYCLE`
- `REIT_DEVELOPMENT_TRUST`
- `CRO_CLINICAL_SERVICE`

주의:

- 이 Green 가능은 production Stage 3-Green 허용이 아니다.
- 가격 경로 검증, 성공/반례 case, MFE/MAE, drawdown 검증 전까지는 shadow 연구용이다.

## 바꾸지 않은 것

- `features.py` 변경 없음
- `staging.py` 변경 없음
- `red_team.py` 변경 없음
- `pipeline/e2r_standard_flow.py` 변경 없음
- production `StageClassifier` threshold 변경 없음

## 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round20_score_weight_report \
  --output-directory output/e2r_round20_score_weight_v06 \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round20_v06.csv \
  --theme-map data/sector_taxonomy/theme_tag_map_round20_v06.csv
```

테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_round20_score_weight_v06 -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 다음 작업

1. v0.6 targets를 case record 후보로 확장한다.
2. stage date와 price path를 채운다.
3. shadow score와 실제 MFE/MAE를 비교한다.
4. 충분한 성공/반례 coverage가 생긴 archetype만 production scoring 후보로 올린다.

핵심 원칙:

> 분류표가 좋아졌다고 점수표가 검증된 것은 아니다.
> 점수표는 실제 증거와 주가 경로로 검증된 뒤에만 운영에 반영한다.
