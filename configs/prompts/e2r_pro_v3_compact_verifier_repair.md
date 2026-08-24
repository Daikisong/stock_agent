아래 candidate들은 Local Evidence Preflight와 source representation resolver로 해결되지 않았고,
deterministic verifier가 실제 initial-output 또는 의미/source support 문제로 반려했다.

전체 dossier를 다시 쓰지 마라. 아래 repair group과 candidate만 보고 각 candidate에 허용된
action 하나를 선택한 `e2r_pro_repair_delta_v3` JSON 하나만 반환하라.

허용:

- `CORRECT`: exact excerpt와 일치하도록 명백한 필드 오류만 수정
- `REPLACE`: 더 적합한 공식 source document와 atomic fact로 대체
- `NARROW`: statement를 excerpt가 직접 지지하는 범위로 축소
- `WITHDRAW`: 공개 source로 지지할 수 없어 철회

금지:

- 없는 quote 생성
- 같은 잘못된 URL을 문장만 바꿔 재제출
- 여러 source를 하나의 replacement fact에 합성
- score/Stage를 높이기 위한 fact 창작
- 기존 accepted fact 삭제·수정
- packet 밖 candidate·question 추가
- 전체 `ResearchDossierV3` 재출력

replacement fact는 Initial V3 atomic evidence contract와 `verifier_preflight`를 그대로 만족해야
한다. replacement fact 한 개는 source document 한 개만 참조한다. 같은 source group의
`fetched_source_text`는 group에 한 번만 제공되므로 candidate별로 전체 원문을 반복하지 마라.

응답 형식:

응답 맨 앞에 compiled context에 제시된 `E2R_PRO_RUN_ID`, `E2R_PRO_JOB_ID`,
`E2R_PRO_PASS_ID`, `E2R_PRO_PARENT_PASS_ID` marker를 각각 정확히 한 번 출력한다.

E2R_REPAIR_DELTA_JSON_BEGIN
```json
{...e2r_pro_repair_delta_v3...}
```
E2R_REPAIR_DELTA_JSON_END

`score_authority=false`, `stage_authority=false`를 유지한다.

{{COMPILED_CONTEXT}}
