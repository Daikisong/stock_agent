# Round 9 Case Record Pack Audit

Round 9는 지금까지 말로 정리한 성공/반례 후보가 실제 agent-readable case record로 들어갔는지 확인하는 calibration 단계다.

쉬운 예시:

```text
HMM은 EPS와 주가가 크게 움직였을 수 있다.
하지만 운임 정상화로 꺾이는 구조라면 structural Green이 아니라 cycle_boom_bust 반례다.
```

## What Round 9 Confirms

- 10개 대섹터 관점이 문서화되어 있다.
- 실무 archetype view는 32개로 정리된다.
- `ONE_OFF_OR_THEME_RISK`는 보고용 alias이며, production enum은 `ONE_OFF_EVENT_DEMAND`와 `THEME_VALUATION_OVERHEAT`를 분리 유지한다.
- Round 1-8에서 나온 필수 case id가 `cases_v02.jsonl`에 존재하는지 감사한다.
- `notes` 필드는 calibration 설명용이며 production evidence가 아니다.

## What Not To Change

- production scoring에 case label을 넣지 않는다.
- `score_weight_hint`를 live scoring에 적용하지 않는다.
- stage date나 price를 추정으로 채우지 않는다.
- event premium, one-off, cycle boom-bust를 true rerating으로 부르지 않는다.
