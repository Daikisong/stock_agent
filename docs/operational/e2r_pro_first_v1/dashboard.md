# Dashboard

기본 주소는 `http://127.0.0.1:8765`다. 외부 interface에는 bind할 수 없다.

읽기 API는 scan/candidate/job/artifact/result를 보여준다. 상태 변경 API는 같은 loopback origin과 24자 이상 local token을 요구한다.

승인은 두 단계다.

```text
issue → 15분 만료 single-use nonce 발급
consume → 현재 packet_hash + prompt_hash + browser_session_id와 원자 대조
```

두 번 consume하거나 prompt를 바꾸면 409로 거절된다. Dashboard는 score나 Stage를 편집하는 기능을 제공하지 않는다.
