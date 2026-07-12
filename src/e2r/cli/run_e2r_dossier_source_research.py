"""Run bounded LLM-planned source acquisition for one E2R dossier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.dossier import DossierTarget, run_dossier_source_research


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dossier-root", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--company-name", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--canonical-archetype", required=True)
    parser.add_argument("--force-web-family", action="append", default=[])
    parser.add_argument("--question-family", action="append", default=[])
    parser.add_argument("--adequacy-route-category", action="append", default=[])
    args = parser.parse_args(argv)
    task_path = Path(args.dossier_root) / "question_source_tasks.jsonl"
    tasks = tuple(
        json.loads(line) for line in task_path.read_text().splitlines() if line.strip()
    )
    result = run_dossier_source_research(
        target=DossierTarget(args.target_id, args.company_name),
        as_of_date=args.as_of_date,
        archetype_id=args.canonical_archetype,
        dossier_question_tasks=tasks,
        output_root=args.output_root,
        force_web_family_ids=args.force_web_family,
        question_family_ids=args.question_family,
        adequacy_route_categories=args.adequacy_route_category,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "DOSSIER_SOURCE_RESEARCH_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
