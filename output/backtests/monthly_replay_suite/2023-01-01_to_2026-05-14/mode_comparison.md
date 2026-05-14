# Mode Comparison

| mode | candidates | Green | Yellow | Red | missed winners | false positives | 4B unknown | evidence_missing | report/news unavailable | official evidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| case_fixture | 234 | 101 | 23 | 42 | 0 | 0 | 0 | 25 | 127 | 443 |
| official_only | 234 | 0 | 0 | 0 | 8 | 0 | 0 | 508 | 378 | 443 |
| hybrid | 234 | 101 | 23 | 42 | 0 | 0 | 0 | 25 | 127 | 443 |

## Interpretation

- official_only is intentionally weaker when the historical winner was report/news-driven because those snapshots are excluded.
- case_fixture is strong for regression testing, but curated fixtures do not prove live discovery.
- hybrid is the closest practical approximation when report/news fixtures exist alongside official evidence.
