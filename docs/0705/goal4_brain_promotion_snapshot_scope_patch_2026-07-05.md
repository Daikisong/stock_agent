# Goal4 Brain Promotion Snapshot Scope Patch - 2026-07-05

## 결론

최신 0705 runtime attempt에서 `brain_stage_promotion_unsafe_promoted_count=1`로 남아 있던 blocker는 promoted row 자체의 source 문제가 아니었다.

실제 promoted row:

```text
symbol: 005930
stagecourt_trace_id: SCT-BRAIN-1e999f3308d1bc0f3d6b
stage_scope: FULL_THESIS
score_scale: FULL_E2R_100
accepted claims:
  CLM-fd7a6609a992dd420e3d -> CompanyGuide
  CLM-f6e8334905f141c3ce64 -> OpenDART
```

snapshot 문서 2개는 다음 unpromoted 후보 쪽에 있었다.

```text
snapshot://issuer_official/hd_hyundai_electric_report.txt
snapshot://issuer_official/hyosung_heavy_report.txt
```

따라서 기존 audit은 다음처럼 과잉 판정했다.

```text
brain_docs 전체에 snapshot이 있음
→ promoted 삼성전자 row도 unsafe라고 판정
```

올바른 판정은 다음이다.

```text
promoted row가 참조한 accepted claim의 evidence document가 snapshot인가?
→ 아니면 unsafe promotion 아님
```

쉬운 예:

```text
삼성전자 답안지는 DART/CompanyGuide 서류를 첨부했다.
다른 후보 파일함에 snapshot 서류가 남아 있다.
그 snapshot 때문에 삼성전자 답안지를 무효 처리하면 안 된다.
```

## 코드 패치

`_brain_stage_promotion_audit`에서 snapshot blocker 범위를 바꿨다.

변경 전:

```text
brain evidence documents include snapshot:// URLs
```

변경 후:

```text
promoted brain evidence documents include snapshot:// URLs
```

추가 metric:

```text
brain_snapshot_document_count
brain_promoted_snapshot_document_count
```

`_brain_web_readiness_gate_audit`도 같은 기준으로 맞췄다.

```text
snapshot_document_count: 전체 Brain attempt의 snapshot 문서 수
promoted_snapshot_document_count: promoted row가 실제로 참조한 snapshot 문서 수
```

전체 snapshot은 diagnostic으로 남긴다.
하지만 readiness blocker는 promoted snapshot이 있을 때만 건다.

## 최신 재계산 결과

```text
brain_stage_promotion_audit:
  verdict: PROMOTION_APPLIED
  unsafe_promoted_stage_row_count: 0
  brain_snapshot_document_count: 2
  brain_promoted_snapshot_document_count: 0
  blockers: []

brain_web_readiness_gate_audit:
  verdict: BLOCKED
  brain_web_evidence_pass_allowed: false
  snapshot_document_count: 2
  promoted_snapshot_document_count: 0
  blockers:
    - web/LLM accepted claim count is zero
    - Brain/Web source task budget caps were exceeded: 2
    - Brain/Web operational minimum web/LLM accepted claims not met: 0/3

leaf_artifact_audit:
  verdict: PASS
  critical_count: 0
```

## Goal4 상태

이번 패치는 Goal4 완료가 아니다.

해결된 것:

```text
1. promoted row와 무관한 snapshot 문서 때문에 unsafe promotion으로 막히던 과잉 blocker 제거
2. leaf artifact audit critical count 1 -> 0
3. score recompute audit과 promotion source audit의 의미 분리
```

아직 남은 것:

```text
1. Brain/Web accepted claim 중 web/LLM source-backed claim이 0개
2. source task budget cap exceeded 2개
3. required positive primitive 부족
4. C05/C06 외 전체 아키타입 full-thesis parity 미증명
5. 하이닉스 controlled smoke와 production row 분리 상태
```

최신 readiness 표현도 다음처럼 정정됐다.

```text
brain_stagecourt_path_produced: true
brain_web_promoted_stagecourt_path: false
remaining gap:
  Brain/Web StageCourt path is promoted but evidence readiness gate is still blocked
```

즉 이제 상태는:

```text
가짜/오귀속 promotion 위험은 제거됨.
하지만 meaningful runtime parity는 아직 아님.
다음 작업은 web/LLM accepted claim 0개와 source task budget cap 초과 원인을 줄이는 것.
```
