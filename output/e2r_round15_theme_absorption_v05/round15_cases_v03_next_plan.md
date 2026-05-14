# Round-15 cases_v03 Next Plan

1. Convert the Round-15 success/counterexample plan into `cases_v03.jsonl` candidates.
2. Add stage date candidates only when the source text supports them.
3. Backfill stage2/stage3 price, MFE/MAE, peak price, and drawdown.
4. Run score-price alignment before any shadow scoring.
5. Keep production StageClassifier and Stage 3-Green thresholds unchanged.

## What Not To Change
- Do not use theme tags as production evidence.
- Do not use Round-15 targets as candidate-generation labels.
- Do not treat one-off EPS spikes, cheap commodity rebounds, or policy headlines as structural E2R without repeat FCF evidence.
