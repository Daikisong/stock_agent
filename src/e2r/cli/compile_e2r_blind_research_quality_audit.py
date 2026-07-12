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
    parser.add_argument(
        "--dossier-output",
        action="append",
        default=[],
        metavar="TARGET_ID=PATH",
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
    if args.dossier_output:
        dossier_roots = {}
        for value in args.dossier_output:
            target_id, separator, path = value.partition("=")
            if not separator or not target_id or not path:
                parser.error("--dossier-output must be TARGET_ID=PATH")
            if target_id in dossier_roots:
                parser.error(f"duplicate --dossier-output target: {target_id}")
            dossier_roots[target_id] = path
        benchmark.write_dossier_leaves(
            result=result,
            gold_root=args.gold_root,
            production_root=args.production_root,
            dossier_roots=dossier_roots,
        )
    print(
        f"{result.status} gold={result.audit['gold_fact_count']} "
        f"recall={result.audit['noncritical_fact_recall']:.3f} "
        f"critical={result.audit['critical_count_sum']}"
    )
    return 0 if result.audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
