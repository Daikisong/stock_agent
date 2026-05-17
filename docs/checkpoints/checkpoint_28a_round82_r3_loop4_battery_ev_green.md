# Checkpoint 28A Round82 R3 Loop4 Battery / EV / Green-Energy

## 목적

`docs/round/round_82.md`의 R3 Loop 4 리서치 기준을 case-library와 score-profile 설계 자료로 반영했다.

이 작업은 생산 scoring 변경이 아니다. 예를 들어 `ESS`라는 단어가 나왔다고 Stage 3-Green을 주는 것이 아니라, 계약금액·계약기간·고객·GWh·OPM·FCF가 실제로 확인되는지 검증하기 위한 calibration 자료다.

## 반영 내용

- R3 Loop 4 canonical target 18개를 추가/정리했다.
- `ESS_AI_DATA_CENTER_STORAGE`, `EV_TO_ESS_CAPACITY_REDEPLOYMENT`, `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE`, `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`, `EV_FIRE_BESS_SAFETY_OVERLAY`, `RENEWABLE_ENERGY_PROJECT_ECONOMICS`, `LITHIUM_ESS_DEMAND_CYCLE`, `SPECULATIVE_BATTERY_TECH` archetype을 추가했다.
- R3 Loop 4 case candidate 16개를 `data/e2r_case_library/cases_r3_loop4_round82.jsonl`로 생성했다.
- R3 Loop 4 score profile을 `data/sector_taxonomy/score_weight_profiles_round82_r3_loop4_v4.csv`로 생성했다.
- 리포트 산출물을 `output/e2r_round82_r3_loop4_battery_ev_green/` 아래에 생성했다.

## 핵심 해석

- Green 가능 축은 여전히 제한적이다: `ESS_LFP_GRID_STORAGE`, `WASTE_RECYCLING_ENVIRONMENT`.
- `LGES $4.3B LFP 계약`은 금액과 기간은 강하지만 고객·용도 미공개라 `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` cap을 건다.
- `GM-LG Ultium Ohio idle`은 EV CAPA thesis 4C와 ESS 전환 Watch가 동시에 붙는 사례로 분리했다.
- `Ford Energy`는 AI 데이터센터 storage 후보지만, 정확한 source date, 고객계약, margin, FCF가 확인되기 전에는 Green 근거가 아니다.
- `Moss Landing BESS fire`와 한국 EV 배터리 인증 이슈는 positive storage evidence가 아니라 RedTeam safety/permitting overlay다.
- `전고체/신소재`는 상용화·고객·양산·FCF 확인 전까지 `SPECULATIVE_BATTERY_TECH` Watch/Red다.

## 산출물 요약

- target_count: 18
- case_candidate_count: 16
- structural_success_count: 1
- success_candidate_count: 5
- cyclical_success_count: 1
- failed_rerating_count: 1
- overheat_count: 1
- stage4b_case_count: 2
- stage4c_case_count: 7
- green_possible_count: 2
- redteam_first_count: 7
- gate_only_target_count: 3

## 검증

실행한 핵심 검증:

```bash
PYTHONPATH=src python -m unittest tests.test_round82_r3_loop4_battery_ev_green -v
PYTHONPATH=src python -m e2r.cli.build_round82_r3_loop4_report
```

## 변경하지 않은 것

- 생산 StageClassifier threshold를 바꾸지 않았다.
- 생산 scoring에 R3 Loop 4 weight를 적용하지 않았다.
- case record를 candidate-generation input으로 쓰지 않았다.
- 고객명·용도·마진·가동률·stage price가 없는 값은 만들지 않았다.

## 다음 단계

R3는 false-positive가 큰 대섹터다. 다음 단계는 price path backfill과 실제 공시/리포트 기반 검증이다. 예를 들어 `ESS 계약`은 좋은 출발점이지만, 고객·GWh·OPM·FCF가 이어지지 않으면 Stage 3-Green으로 올리지 않는다.
