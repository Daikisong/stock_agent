# Round-7 Case Validation Framework

Source round: `docs/round/round_07.md`

이 문서는 calibration 전용이다. production scoring과 StageClassifier threshold를 바꾸지 않는다.

## 핵심

Round 7은 성공 사례와 반례를 점수-주가-EPS/FCF 정합성으로 다시 나눈다.

쉬운 예시:

`주가 +100%`라도 EPS/FCF 상향이 없으면 구조적 E2R 성공이 아니라 테마/이벤트 반례다.

## Green 허용도

| posture | archetype_count | interpretation |
|---|---:|---|
| GREEN_ELIGIBLE_AFTER_VALIDATION | 13 | 성공/반례와 가격 경로가 채워지면 향후 Green shadow scoring 후보 |
| WATCH_YELLOW_DEFAULT | 12 | 기본은 Stage 3-Watch/Yellow, Green은 강한 반복성/FCF 증거 필요 |
| REDTEAM_GUARDRAIL | 10 | RedTeam과 4B/4C 방어가 우선 |

## Guardrails
- 케이스 라이브러리를 candidate generation input으로 쓰지 않는다.
- Stage 3-Green threshold를 낮추지 않는다.
- event premium, one-off demand, credit relief rally를 true rerating으로 부르지 않는다.
- 가격 경로가 없는 케이스는 score weight 변경 근거로 쓰지 않는다.
