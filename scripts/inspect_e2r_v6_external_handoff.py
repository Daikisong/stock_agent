"""2026-07-12 C06 외부 검토 snapshot을 읽기 전용으로 요약한다."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path("output/researcher_mode/c06/2026-07-12-clean-v8")


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise TypeError(f"JSON object가 아닙니다: {path}")
    return value


def _status(path: Path) -> str:
    if not path.is_file():
        return "MISSING"
    return str(_read_json(path).get("status") or "STATUS_MISSING")


def _target_summary(root: Path, target_id: str) -> None:
    target = root / target_id
    print(f"\n[{target_id}]")
    print("fact_extraction:", _status(target / "fact_extraction_result.json"))
    print("source_graph:", _status(target / "source_graph_checkpoint.json"))
    print("component_memos:", _status(target / "component_scoring_memo_run.json"))
    print("saturation:", _status(target / "semantic_saturation_certificate.json"))


def _print_000660_details(root: Path) -> None:
    target = root / "000660"
    source = _read_json(target / "source_graph_checkpoint.json")
    journal = target / "collaboration_codex_subagent_provider"
    requests = tuple((journal / "requests").glob("COLLABREQ-*.json"))
    response_names = {
        path.name for path in (journal / "responses").glob("COLLABREQ-*.json")
    }

    print("\n[000660 Source Graph 세부]")
    print("epoch:", source.get("epoch"))
    for key in (
        "generated_queries",
        "executed_queries",
        "search_candidates",
        "evidence_documents",
        "query_failures",
        "query_generation_history",
        "query_generation_supervisor_handoffs",
    ):
        print(f"{key}:", len(source.get(key) or ()))
    print("pending_reasons:")
    for reason in source.get("pending_reasons") or ():
        print(" -", reason)

    print("\n[000660 Collaboration journal]")
    print("requests:", len(requests))
    print("responses:", len(response_names))
    print("unanswered:")
    for request in sorted(requests):
        if request.name in response_names:
            continue
        row = _read_json(request)
        print(
            " -",
            request.name,
            row.get("pass_name"),
            row.get("schema_name"),
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    root = args.root
    if not root.is_dir():
        parser.error(f"snapshot root가 없습니다: {root}")

    print("snapshot_root:", root)
    print("as_of_date: 2026-07-12")
    for target_id in ("005930", "000660"):
        _target_summary(root, target_id)
    _print_000660_details(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
