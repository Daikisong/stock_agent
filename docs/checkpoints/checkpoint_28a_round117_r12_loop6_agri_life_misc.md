# Checkpoint 28A Round 117 R12 Loop 6 농업·생활서비스·기타 반영

## 목적

`docs/round/round_117.md`의 R12 Loop 6 내용을 case library와 calibration 리포트에 반영했다. 이번 라운드는 농업·생활서비스·규제 소비재 서사를 더 잘게 나눠, 겉으로는 필수재·방어주처럼 보여도 반복매출, 단위경제, 규제 범위, FCF가 확인되지 않으면 Stage 3-Green으로 가지 않도록 막는 것이 핵심이다.

쉬운 예시는 이렇다. 계란 가격이 조류독감으로 급등하면 이익은 강하게 보일 수 있다. 하지만 가격 정상화, DOJ 조사, 소비자 반발 가능성이 있으면 구조적 체급 변화가 아니라 `LIVESTOCK_DISEASE_PRICE_REGULATORY` 게이트로 분리해야 한다.

## 반영 내용

- `src/e2r/sector/archetypes.py`에 라운드 117 신규 archetype을 추가했다.
  - `RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION`
  - `FERTILIZER_STRATEGIC_PHOSPHATE_OPTION`
  - `LIVESTOCK_DISEASE_PRICE_REGULATORY`
  - `EDTECH_AI_SEARCH_DISINTERMEDIATION`
  - `CANNABIS_PARTIAL_RESCHEDULING_LIMIT`
- `src/e2r/sector/round117_r12_loop6_agri_life_misc.py`를 추가·정리했다.
  - target_count: 33
  - case_candidate_count: 23
  - gate_only_target_count: 10
  - green_possible_count: 0
- 새 케이스를 추가하거나 라운드 117 명명으로 정렬했다.
  - `deere_construction_right_to_repair_case`
  - `cnh_weak_farm_equipment_demand_case`
  - `bayer_soy_seed_license_crop_science_case`
  - `nutrien_potash_phosphate_option_case`
  - `calmaine_egg_price_regulatory_case`
  - `chegg_ai_search_disintermediation_case`
  - `cannabis_schedule3_limited_case`
- production scoring은 변경하지 않았다.
  - 이 팩은 calibration/evaluation 자료다.
  - `features.py`, `staging.py`, `red_team.py`, `e2r_standard_flow.py`는 round117 팩을 import하지 않는다.

## 산출물

- `data/e2r_case_library/cases_r12_loop6_round117.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round117_r12_loop6_v6.csv`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_agri_life_misc_summary.md`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_case_matrix.csv`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_stage_date_plan.csv`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_green_guardrails.md`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_unit_economics_caps.md`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_price_validation_plan.md`
- `output/e2r_round117_r12_loop6_agri_life_misc/round117_r12_loop6_price_fields.csv`

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round117_r12_loop6_agri_life_misc -v`
- `PYTHONPATH=src python -m e2r.cli.build_round117_r12_loop6_report`

전체 테스트와 `compileall`, `git diff --check`는 커밋 전 검증 단계에서 실행했다.

## 다음 작업

라운드 117도 아직 생산 점수 변경 단계가 아니다. 다음 라운드에서는 가격 경로와 case coverage를 더 채워서, 어떤 R12 서사가 단순 이벤트인지 구조적 FCF 변화인지 더 명확히 나누는 것이 우선이다.
