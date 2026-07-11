from __future__ import annotations

import argparse
from pathlib import Path

from e2r.research_brain.research_quality import BlindResearchQualityBenchmark


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold-root", required=True)
    parser.add_argument("--production-root", required=True)
    parser.add_argument(
        "--comparison-output",
        default="docs/operational/e2r_material_fact_comparison.jsonl",
    )
    parser.add_argument(
        "--audit-output",
        default="docs/operational/e2r_research_quality_gold_audit.json",
    )
    args = parser.parse_args()
    benchmark = BlindResearchQualityBenchmark()
    result = benchmark.compare(
        gold_root=args.gold_root,
        production_root=args.production_root,
    )
    benchmark.write(
        result=result,
        comparison_path=Path(args.comparison_output),
        audit_path=Path(args.audit_output),
    )
    print(
        f"{result.status} gold={result.audit['gold_fact_count']} "
        f"recall={result.audit['noncritical_fact_recall']:.3f} "
        f"critical={result.audit['critical_count_sum']}"
    )
    return 0 if result.audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
