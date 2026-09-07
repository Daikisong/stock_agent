# Scheduler

timezone은 고정 `Asia/Seoul`, 기본 창은 새벽 `05:30`과 저녁 `18:30`이다.

각 창은 SQLite의 `(as_of_date, scan_window)` unique key로 한 번만 claim된다. 프로세스가 05:30에 꺼져 있다가 06:00에 켜져도 morning 창을 catch-up으로 한 번 실행하고, 재시작해도 다시 만들지 않는다.

cheap scan의 `DEEP_RESEARCH` production candidate만 Pro queue로 간다. test-injected candidate와 `EVENT_SEARCH` 후보는 직접 승격되지 않는다. 자연 후보가 없을 때 live 검증용 종목을 넣으면 반드시 `FORCED_VALIDATION_CANARY`로 표시해 production selection처럼 보이게 하지 않는다.
