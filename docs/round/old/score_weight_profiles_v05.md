# Score Weight Profiles v0.5

Round 18 adds score-weight profiles for research and shadow validation only.
They are not wired into production `features.py` or `staging.py`.

The profiles describe which evidence dimensions matter more by archetype:

- `eps_fcf`
- `structural_visibility`
- `bottleneck_pricing`
- `market_mispricing`
- `valuation_rerating`
- `capital_allocation`
- `information_confidence`
- `risk_penalty`

Example:

- `MEMORY_HBM_CAPACITY` gives high weight to EPS/FCF, memory/HBM visibility, and pricing/capacity bottlenecks.
- That does not mean every HBM tag is Green.
- It means HBM cases should be researched for HBM demand, pricing, supply discipline, and medium-term revisions.

Counterexample:

- `CHEMICAL_SPREAD` can have strong EPS rebound.
- But oversupply risk, especially China/Middle-East capacity, keeps structural visibility low.
- This remains RedTeam-first until spread durability and capacity discipline are proven.

## Files

- `data/sector_taxonomy/score_weight_profiles_v05.yml`
- `output/e2r_case_library_v03/score_weight_profiles_v05_summary.md`
- `output/e2r_case_library_v03/shadow_score_profile_report.md`

## Production Rule

Do not apply these profiles to production scoring yet.

Before production use, each archetype needs:

- enough success and counterexample cases
- price-path validation
- score-price alignment review
- 4B/4C lifecycle checks
