"""Run the generic bounded E2R full-thesis dossier workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.dossier import (
    DossierRunConfig,
    DossierTarget,
    FullThesisDossierOrchestrator,
    load_question_family_catalog,
    run_organic_claim_closure,
)


def _bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--symbol")
    parser.add_argument("--company")
    parser.add_argument("--symbols")
    parser.add_argument("--companies")
    parser.add_argument("--canonical-archetype", required=True)
    parser.add_argument("--materialize-live-input", type=_bool, default=False)
    parser.add_argument("--live-materialization-authorized", type=_bool, default=False)
    parser.add_argument("--max-research-iterations", type=int, default=12)
    parser.add_argument("--max-code-repair-iterations", type=int, default=10)
    parser.add_argument("--require-organic-claim", type=_bool, default=True)
    parser.add_argument(
        "--require-calibrated-component-score", type=_bool, default=True
    )
    parser.add_argument("--require-full-score-valid", type=_bool, default=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument(
        "--question-family-config",
        default="configs/e2r_full_thesis_question_families_v1.json",
    )
    parser.add_argument("--resume-source-root")
    args = parser.parse_args(argv)
    targets = _targets(args)
    config = DossierRunConfig(
        as_of_date=args.as_of_date,
        canonical_archetype=args.canonical_archetype,
        output_root=args.output_root,
        max_research_iterations=args.max_research_iterations,
        max_code_repair_iterations=args.max_code_repair_iterations,
        materialize_live_input=args.materialize_live_input,
        live_materialization_authorized=args.live_materialization_authorized,
        require_organic_claim=args.require_organic_claim,
        require_calibrated_component_score=args.require_calibrated_component_score,
        require_full_score_valid=args.require_full_score_valid,
    )
    catalog = load_question_family_catalog(args.question_family_config)
    result = FullThesisDossierOrchestrator(
        question_family_catalog=catalog
    ).initialize(config, targets=targets)
    closure_results = ()
    if args.resume_source_root:
        closure_results = tuple(
            run_organic_claim_closure(
                target=target,
                as_of_date=args.as_of_date,
                archetype_id=args.canonical_archetype,
                source_root=args.resume_source_root,
                output_root=Path(result.target_results[index]["output_root"]),
            )
            for index, target in enumerate(targets)
        )
    organic_claim_count = sum(row.organic_claim_count for row in closure_results)
    print(
        json.dumps(
            {
                "status": result.status,
                "target_results": result.target_results,
                "critical_count_sum": result.audit["critical_count_sum"],
                "research_complete": False,
                "organic_claim_count": organic_claim_count,
                "organic_closure_statuses": [row.status for row in closure_results],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


def _targets(args: argparse.Namespace) -> tuple[DossierTarget, ...]:
    if args.symbol or args.company:
        if not args.symbol or not args.company or args.symbols or args.companies:
            raise ValueError("use --symbol and --company together, without plural inputs")
        return (DossierTarget(args.symbol, args.company),)
    symbols = tuple(value.strip() for value in str(args.symbols or "").split(",") if value.strip())
    companies = tuple(value.strip() for value in str(args.companies or "").split(",") if value.strip())
    if not symbols or len(symbols) != len(companies):
        raise ValueError("plural symbol and company lists must be non-empty and aligned")
    return tuple(DossierTarget(symbol, company) for symbol, company in zip(symbols, companies))


if __name__ == "__main__":
    raise SystemExit(main())
