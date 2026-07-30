"""Validate and import one Codex collaboration-subagent provider response."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    import_collaboration_response,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--journal-root", required=True)
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--response-path", required=True)
    parser.add_argument("--agent-id", required=True)
    parser.add_argument("--canonical-task-name", required=True)
    parser.add_argument("--agent-model", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    response_path = Path(args.response_path)
    try:
        payload = json.loads(response_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            "collaboration response path must contain exactly one JSON object"
        ) from exc
    if not isinstance(payload, dict):
        raise ValueError(
            "collaboration response path must contain exactly one JSON object"
        )
    envelope = import_collaboration_response(
        journal_root=args.journal_root,
        request_id=args.request_id,
        response_payload=payload,
        agent_id=args.agent_id,
        canonical_task_name=args.canonical_task_name,
        agent_model=args.agent_model,
    )
    print(
        json.dumps(
            {
                "status": "COLLABORATION_RESPONSE_IMPORTED",
                "request_id": envelope["request_id"],
                "response_id": envelope["response_id"],
                "payload_hash": envelope["payload_hash"],
                "provenance": envelope["provenance"],
                "score_or_stage_authority": False,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
