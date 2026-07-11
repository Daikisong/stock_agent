"""Compile one leaf-backed mandatory-target E2R acceptance report."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.dossier import compile_target_full_thesis_acceptance


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--company-name", required=True)
    parser.add_argument("--success-label", required=True)
    parser.add_argument("--dossier-root", required=True)
    parser.add_argument("--source-research-root", action="append", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    result = compile_target_full_thesis_acceptance(
        target_id=args.target_id,
        company_name=args.company_name,
        success_label=args.success_label,
        dossier_root=args.dossier_root,
        source_research_roots=args.source_research_root,
        output_path=args.output,
    )
    print(json.dumps({"status":result["status"],"critical_count_sum":result["critical_count_sum"]},ensure_ascii=False,sort_keys=True))
    return 0 if result["status"] == args.success_label else 2


if __name__ == "__main__": raise SystemExit(main())
