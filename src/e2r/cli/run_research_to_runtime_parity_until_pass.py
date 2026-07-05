"""Generate the research-to-runtime parity audit for Census V4 artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from e2r.census.research_to_runtime_parity import write_research_to_runtime_parity_artifacts


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    text = value.strip().lower()
    if text in {"1", "true", "yes", "y"}:
        return True
    if text in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"invalid boolean value: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--docs-dir", default="docs/operational")
    parser.add_argument("--output-root", default=None)
    parser.add_argument("--as-of-date", default=None)
    parser.add_argument("--mode", default="full_thesis_balanced")
    parser.add_argument("--mandatory-archetypes", default="C06,C08,C15,C17,C24,C28")
    parser.add_argument("--max-iterations", type=int, default=1)
    parser.add_argument("--fail-on-c05-monoculture", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-unknown-target-promoted", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-required-positive-missing-over-threshold", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-research-proxy-score", type=_parse_bool, default=False)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    mandatory = tuple(part.strip() for part in args.mandatory_archetypes.split(",") if part.strip())
    paths = write_research_to_runtime_parity_artifacts(
        repo_root=Path(args.repo_root),
        output_root=args.output_root,
        docs_dir=Path(args.docs_dir),
        as_of_date=args.as_of_date,
        mandatory_archetype_prefixes=mandatory,
    )
    audit = paths["audit"]
    result = {
        "mode": args.mode,
        "max_iterations_requested": args.max_iterations,
        "final_status": audit["final_status"],
        "completion_labels": audit["completion_labels"],
        "blockers": audit["blockers"],
        "matrix_path": str(paths["matrix_path"]),
        "summary_path": str(paths["summary_path"]),
        "root_cause_path": str(paths["root_cause_path"]),
        "v2_audit_path": str(paths["v2_audit_path"]),
        "candidate_selection_status": paths["candidate_selection_audit"]["status"],
        "planner_bias_status": paths["planner_bias_audit"]["status"],
        "research_case_count": paths["research_reverse_bundle"]["inventory"]["record_count"],
        "research_memory_card_count": paths["research_reverse_bundle"]["cards"]["card_count"],
        "source_route_pattern_count": paths["source_route_reports"]["source_route_matrix"]["pattern_count"],
        "research_memory_followup_task_count": paths["followup_audit"]["task_count"],
        "mandatory_replay_accepted_claim_count": paths["replay_reports"]["replay_matrix"]["accepted_claim_replay_count"],
        "mandatory_replay_source_proxy_repair_task_count": paths["replay_reports"]["replay_matrix"][
            "source_proxy_repair_task_count"
        ],
        "meaningful_acceptance_status": paths["meaningful_acceptance"]["meaningful_status"],
        "acceptance_report_path": str(paths["acceptance_report_path"]),
        "readiness_verdict_path": str(paths["readiness_verdict_path"]),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))

    failure_reasons: list[str] = []
    if args.fail_on_c05_monoculture and "C05_FULL_THESIS_MONOCULTURE" in audit["blockers"]:
        failure_reasons.append("C05_FULL_THESIS_MONOCULTURE")
    if args.fail_on_unknown_target_promoted and "TARGET_ARCHETYPE_UNKNOWN_PROMOTED" in audit["blockers"]:
        failure_reasons.append("TARGET_ARCHETYPE_UNKNOWN_PROMOTED")
    if (
        args.fail_on_required_positive_missing_over_threshold
        and "REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS" in audit["blockers"]
    ):
        failure_reasons.append("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS")
    if args.fail_on_research_proxy_score:
        proxy_score_rows = [
            row
            for row in audit["rows"]
            if row["source_proxy_leak_count"] > 0 and row["runtime_full_thesis_row_count"] > 0
        ]
        if proxy_score_rows:
            failure_reasons.append("RESEARCH_PROXY_SCORE_LEAK")

    if failure_reasons:
        print(json.dumps({"failed_on": sorted(set(failure_reasons))}, ensure_ascii=False, sort_keys=True))
        return 2
    return 0 if audit["meaningful_full_thesis_evidence_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
