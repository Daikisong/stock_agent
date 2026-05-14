# Round-7 Success and Counterexample Rules

## Success Case

성공 사례는 점수만 높으면 안 된다. Stage 2/3 근거 이후 가격과 EPS/FCF가 함께 움직여야 한다.

- `evidence_score_high`
- `stage2_or_stage3_signal`
- `price_rerating_after_signal`
- `eps_op_fcf_revision_confirmed`
- `no_fast_4c`

## Counterexample

- `price_up_without_eps_fcf`
- `score_high_but_price_no_rerating`
- `eps_spike_one_off`
- `fast_4c_after_stage2`
- `event_premium_only`

## Price Validation Fields

- `stage1_price`
- `stage2_price`
- `stage3_price`
- `stage4b_price`
- `stage4c_price`
- `peak_price`
- `mfe_90d`
- `mfe_180d`
- `mfe_1y`
- `mae_90d`
- `mae_180d`
- `mae_1y`
- `drawdown_after_peak`
- `below_stage3_price_flag`

## 쉬운 예시

- 플랫폼: MAU가 늘어도 ARPU/OPM/FCF가 없으면 Stage 3-Green 근거가 아니다.
- 건설: 수주가 늘어도 PF와 유동성 문제가 남아 있으면 credit relief rally일 수 있다.
- CDMO: 바이오 임상 뉴스가 아니라 장기 생산계약, 가동률, FCF가 핵심이다.
