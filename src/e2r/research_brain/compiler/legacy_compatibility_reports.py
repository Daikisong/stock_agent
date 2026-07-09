"""Write legacy-shaped reports from the canonical Research Brain namespace."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from e2r.research_brain.compiler.legacy_case_inventory import extract_research_cases
from e2r.research_brain.compiler.legacy_pattern_aggregator import (
    build_archetype_coverage_matrix,
    build_source_quality_matrix,
)
from e2r.research_brain.retrieval.legacy_runtime_memory import (
    build_memory_card_matrix,
    build_runtime_memory_cards,
)


def _contract_ids(repo_root: Path) -> list[str]:
    payload = json.loads(
        (repo_root / "configs" / "e2r_archetype_evidence_contracts_v12.json").read_text(encoding="utf-8")
    )
    return [row["canonical_archetype_id"] for row in payload["contracts"]]


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_research_reverse_bundle(*, repo_root: str | Path = ".") -> dict[str, Any]:
    root = Path(repo_root)
    cases = [record.to_dict() for record in extract_research_cases(repo_root=root)]
    contract_ids = _contract_ids(root)
    coverage = build_archetype_coverage_matrix(cases, contract_ids)
    quality = build_source_quality_matrix(cases)
    cards = build_runtime_memory_cards(repo_root=root, records=cases)
    card_matrix = build_memory_card_matrix(cards)
    inventory = {
        "schema_version": "e2r_research_reverse_case_inventory_v1",
        "record_count": len(cases),
        "documented_corpus_size": len({case["source_file"] for case in cases}),
        "source_quality_counts": dict(sorted(Counter(case["source_quality"] for case in cases).items())),
        "archetype_count": len(contract_ids),
        "records": cases,
    }
    return {
        "inventory": inventory,
        "coverage": coverage,
        "quality": quality,
        "cards": cards,
        "card_matrix": card_matrix,
    }


def write_research_reverse_bundle(
    *,
    repo_root: str | Path = ".",
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    root = Path(repo_root)
    docs = Path(docs_dir)
    docs = docs if docs.is_absolute() else root / docs
    bundle = build_research_reverse_bundle(repo_root=root)
    paths = {
        "inventory_path": docs / "research_reverse_case_inventory.json",
        "coverage_path": docs / "research_reverse_archetype_coverage_matrix.json",
        "quality_path": docs / "research_reverse_source_quality_matrix.json",
        "cards_path": docs / "research_runtime_memory_cards_v2.json",
        "card_matrix_path": docs / "research_runtime_memory_card_matrix_v2.json",
    }
    _write_json(paths["inventory_path"], bundle["inventory"])
    _write_json(paths["coverage_path"], bundle["coverage"])
    _write_json(paths["quality_path"], bundle["quality"])
    _write_json(paths["cards_path"], bundle["cards"])
    _write_json(paths["card_matrix_path"], bundle["card_matrix"])
    return {**bundle, **paths}


__all__ = ["build_research_reverse_bundle", "write_research_reverse_bundle"]
