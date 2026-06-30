# Census Mode v1/v2 Reclassification

- Census v1은 CENSUS_SKELETON_PASS이며 FULL_UNIVERSE_STAGE_MAP_PASS가 아니다.
- v1의 Unknown 3391 / ProviderPending 3391 / accepted_claim 0 / score_contribution 0은 안전한 빈 지도다.
- Census v2는 source 숫자를 만들었지만 leaf artifact에서 stage row의 claim/score/StageCourt 연결을 독립 재계산하지 못했다.
- root cause: src/e2r/census/census_runner.py::_baseline_inputs_for_config, src/e2r/census/census_runner_v2.py::_build_stage_rows, src/e2r/cli/audit_e2r_census_v2.py::main.
- v3부터 FULL_UNIVERSE_STAGE_MAP_PASS는 leaf artifact auditor와 reviewer A/B/C가 모두 PASS일 때만 허용한다.
