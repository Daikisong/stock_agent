from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.research_quality import (
    audit_search_adequacy,
    compile_dossier_search_adequacy,
)
from e2r.research_brain.scoring.question_impact_contract import (
    load_question_impact_contracts,
)


def _jsonl(path: Path):
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _preferred_jsonl(root: Path, primary: str, fallback: str):
    rows = _jsonl(root / primary)
    return rows if rows else _jsonl(root / fallback)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", action="append", required=True)
    parser.add_argument("--write-back", action="store_true")
    parser.add_argument(
        "--leaf-output",
        default="docs/operational/e2r_evidence_search_adequacy.jsonl",
    )
    parser.add_argument(
        "--audit-output",
        default="docs/operational/e2r_evidence_search_adequacy_audit.json",
    )
    args = parser.parse_args()
    all_rows = []
    for input_root in args.input_root:
        root = Path(input_root)
        rows = compile_dossier_search_adequacy(
            question_tasks=_jsonl(root / "question_source_tasks.jsonl"),
            executed_tasks=_jsonl(root / "executed_question_source_tasks.jsonl"),
            provider_requests=_preferred_jsonl(
                root,
                "research_provider_requests.jsonl",
                "provider_requests.jsonl",
            ),
            provider_fetch_results=_preferred_jsonl(
                root,
                "research_provider_fetch_results.jsonl",
                "provider_fetch_results.jsonl",
            ),
            web_search_tasks=_preferred_jsonl(
                root,
                "research_web_search_tasks.jsonl",
                "web_search_tasks.jsonl",
            ),
            documents=(
                *_jsonl(root / "evidence_documents.jsonl"),
                *_jsonl(root / "research_web_fetched_documents.jsonl"),
            ),
            claims=_jsonl(root / "accepted_current_claims.jsonl"),
            primitive_mappings=_jsonl(root / "primitive_mappings.jsonl"),
            question_closures=_jsonl(root / "question_closure_v2.jsonl")
            or _jsonl(root / "question_closure.jsonl"),
            question_contracts=load_question_impact_contracts(),
            claim_eligibility_decisions=_jsonl(
                root / "claim_eligibility_decisions.jsonl"
            ),
            proposed_impacts=_jsonl(root / "claim_impacts_proposed.jsonl"),
            validated_impacts=_jsonl(root / "claim_impacts_validated.jsonl"),
            material_fact_comparisons=_jsonl(
                root / "material_fact_comparison.jsonl"
            ),
        )
        if not rows:
            raise ValueError(f"no search adequacy rows compiled from {root}")
        all_rows.extend(rows)
        if args.write_back:
            write_jsonl(
                root / "evidence_search_adequacy.jsonl",
                (row.to_dict() for row in rows),
            )
            write_json(
                root / "evidence_search_adequacy_audit.json",
                audit_search_adequacy(rows),
            )
    audit = audit_search_adequacy(tuple(all_rows))
    write_jsonl(
        Path(args.leaf_output),
        (row.to_dict() for row in all_rows),
    )
    write_json(Path(args.audit_output), audit)
    print(
        f"{audit['status']} questions={audit['question_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
