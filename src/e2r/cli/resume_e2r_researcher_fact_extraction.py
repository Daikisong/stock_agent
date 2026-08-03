"""Resume only pending production fact leaves through Codex collaboration."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexResearcherProvider,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    load_current_research_target_registry,
    load_current_research_targets,
    resume_current_fact_extraction_checkpoint,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--symbols", required=True)
    parser.add_argument("--archetype", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument(
        "--target-registry",
        default="configs/e2r_targeted_live_smoke_v1.json",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    symbols = tuple(
        dict.fromkeys(
            value.strip()
            for value in args.symbols.split(",")
            if value.strip()
        )
    )
    if not symbols:
        raise ValueError("--symbols must contain at least one symbol")
    registry_rows = load_current_research_target_registry(
        args.target_registry
    )
    targets = load_current_research_targets(
        symbols=symbols,
        registry_path=args.target_registry,
        as_of_date=args.as_of_date,
        registry_rows=registry_rows,
    )
    config = CurrentResearcherModeConfig(
        as_of_date=args.as_of_date,
        archetype_id=args.archetype,
        output_root=args.output_root,
        live_materialization_authorized=True,
        checkpoint_resume=True,
        gold_lane_isolated=True,
        require_researcher_parity=True,
    )
    provider = CollaborationCodexResearcherProvider.default()
    rows = []
    for target in targets:
        result = resume_current_fact_extraction_checkpoint(
            config=config,
            target=target,
            provider=provider,
        )
        rows.append(
            {
                "target_id": target.target_id,
                "status": result.status,
                "fact_count": len(result.facts),
                "material_claim_count": len(result.material_claims),
                "provider_call_count": len(result.provider_calls),
                "pending_reasons": list(result.pending_reasons),
                "production_score_authority": False,
                "provider_route": "COLLABORATION_CODEX_SUBAGENT",
            }
        )
    complete = bool(
        rows
        and all(row["status"] == "FACT_EXTRACTION_COMPLETE" for row in rows)
    )
    print(
        json.dumps(
            {
                "status": (
                    "FACT_EXTRACTION_RECOVERY_COMPLETE"
                    if complete
                    else "FACT_EXTRACTION_RECOVERY_PENDING"
                ),
                "as_of_date": args.as_of_date,
                "archetype_id": args.archetype,
                "target_results": rows,
                "score_or_stage_authority": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if complete else 2


if __name__ == "__main__":
    raise SystemExit(main())
