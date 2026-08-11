from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.cli.compile_e2r_v6_cross_archetype_canaries import main as canary_cli_main
from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_FAIL,
    CANARY_COMPILATION_PASS,
    CANARY_COMPILATION_PENDING,
    CANARY_RECEIPT_NAME,
    CANARY_RESULT_NAME,
    CANARY_RESULT_PASS,
    CANARY_RESULT_SCHEMA,
    CANARY_REVIEW_NAMES,
    CANARY_REVIEWS_DIRECTORY,
    build_full_researcher_mode_canary_receipt,
    build_independent_canary_review,
    compile_cross_archetype_canary_directory,
    compile_cross_archetype_canary_results,
    seal_cross_archetype_canary_summary,
    validate_cross_archetype_canary_summary,
)
from e2r.production.v6_canary_selection import (
    NATURAL_SELECTION,
    REQUIRED_ARCHETYPES,
    SELECTION_PASS,
    SELECTION_RECEIPT_SCHEMA,
    SELECTION_SCHEMA,
    seal_cross_archetype_canary_selection,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER


AS_OF_DATE = "2026-07-12"


def _selection() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for index, archetype_id in enumerate(REQUIRED_ARCHETYPES, start=1):
        target_id = f"{index:06d}"
        pre_deep = hashlib.sha256(f"{archetype_id}:{target_id}".encode()).hexdigest()
        rows.append(
            {
                "schema_version": SELECTION_RECEIPT_SCHEMA,
                "selection_id": "SELREC-" + pre_deep[:24],
                "archetype_id": archetype_id,
                "target_id": target_id,
                "company_name": f"회사{index}",
                "selection_mode": NATURAL_SELECTION,
                "selection_as_of_date": AS_OF_DATE,
                "pre_deep_input_hash": pre_deep,
                "krx_effective_date": AS_OF_DATE,
                "krx_source_url": "https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info",
                "krx_source_hash": hashlib.sha256(f"krx:{index}".encode()).hexdigest(),
                "krx_request_id": f"KRXREQ-{index:024x}",
                "candidate_event_hash": hashlib.sha256(f"event:{index}".encode()).hexdigest(),
                "depth_decision_hash": hashlib.sha256(f"depth:{index}".encode()).hexdigest(),
                "planner_run_id": f"LIVEPLAN-{index:024x}",
                "blind_input_id": f"BLIND-{index:024x}",
                "plan_hash": hashlib.sha256(f"plan:{index}".encode()).hexdigest(),
                "issuer_profile_hash": hashlib.sha256(f"issuer:{index}".encode()).hexdigest(),
                "business_profile_hash": hashlib.sha256(f"business:{index}".encode()).hexdigest(),
                "direct_current_supporting_fact_ids": [f"FACT-{index}"],
                "recipe_ids": [f"RECIPE-{index}"],
                "trigger_event_ids": [f"TRIG-{index}"],
                "available_source_families": ["OPENDART"],
                "selection_rationale": "natural validation fixture",
                "final_score_visible_at_selection": False,
                "final_stage_visible_at_selection": False,
                "production_daily_candidate": True,
                "score_or_stage_authority": False,
            }
        )
    return {
        "schema_version": SELECTION_SCHEMA,
        "status": SELECTION_PASS,
        "selection_as_of_date": AS_OF_DATE,
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "selections": rows,
        "selection_count": len(rows),
        "critical_counts": {
            "required_archetype_missing_count": 0,
            "invalid_candidate_lineage_count": 0,
            "post_score_target_selection_count": 0,
            "target_specific_code_branch_count": 0,
            "forced_canary_mislabeled_natural_count": 0,
            "duplicate_target_count": 0,
        },
        "critical_count_sum": 0,
        "failures": [],
        "score_or_stage_authority": False,
        "selection_roster_hash": stable_hash(rows),
    }


def _result(selection: dict[str, object], row: dict[str, object]) -> dict[str, object]:
    vector = dict(
        zip(CANONICAL_COMPONENT_ORDER, (10.0, 10.0, 10.0, 8.0, 8.0, 2.0, 2.0))
    )
    body: dict[str, object] = {
        "schema_version": CANARY_RESULT_SCHEMA,
        "status": CANARY_RESULT_PASS,
        "run_id": "RESEARCHRUN-" + str(row["target_id"]),
        "selection_id": row["selection_id"],
        "selection_roster_hash": selection["selection_roster_hash"],
        "archetype_id": row["archetype_id"],
        "target_id": row["target_id"],
        "as_of_date": AS_OF_DATE,
        "production_research_status": "COMPLETE",
        "fact_extraction_status": "COMPLETE",
        "structured_materialization_status": "COMPLETE",
        "business_model_status": "COMPLETE",
        "component_research_status": "COMPLETE",
        "judge_status": "COMPLETE",
        "red_team_status": "COMPLETE",
        "synthesis_status": "COMPLETE",
        "supervisor_status": "COMPLETE",
        "semantic_saturation_status": "COMPLETE",
        "score_status": "COMPLETE",
        "stagecourt_status": "FINAL",
        "full_researcher_mode_complete": True,
        "component_score_vector": vector,
        "total_score": 50.0,
        "canonical_stage": "2",
        "score_valid": True,
        "stage_final": True,
        "component_count": 7,
        "judge_decision_count": 21,
        "query_count": 3,
        "document_count": 8,
        "fact_count": 13,
        "counterfact_count": 2,
        "material_gap_count": 0,
        "source_count": 7,
        "output_tree_hash": hashlib.sha256(
            f"output:{row['target_id']}".encode()
        ).hexdigest(),
        "provider_call_counts": {"COLLABORATION_CODEX": 4},
        "provider_error_count": 0,
        "unauthorized_provider_call_count": 0,
        "local_provider_call_count": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    return {**body, "result_id": "CANARYRUN-" + stable_hash(body)[:24]}


def _bundle(
    selection: dict[str, object], row: dict[str, object]
) -> dict[str, object]:
    result = _result(selection, row)
    receipt = build_full_researcher_mode_canary_receipt(
        result, selection=selection, selection_row=row
    )
    reviews = []
    for reviewer in ("A", "B"):
        seed = f"{row['target_id']}:{reviewer}"
        reviews.append(
            build_independent_canary_review(
                reviewer_id=f"/root/reviewer_{reviewer.lower()}",
                provider_call_id=f"COLLABCALL-{row['target_id']}-{reviewer}",
                prompt_hash=hashlib.sha256(f"prompt:{seed}".encode()).hexdigest(),
                response_hash=hashlib.sha256(f"response:{seed}".encode()).hexdigest(),
                result=result,
                receipt=receipt,
            )
        )
    return {"result": result, "receipt": receipt, "reviews": reviews}


def _bundles(selection: dict[str, object]) -> dict[str, dict[str, object]]:
    rows = selection["selections"]
    assert isinstance(rows, list)
    return {
        str(row["archetype_id"]): _bundle(selection, row)
        for row in rows
        if isinstance(row, dict)
    }


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_live_tree(
    root: Path,
    selection: dict[str, object],
    bundles: dict[str, dict[str, object]],
) -> None:
    rows = selection["selections"]
    assert isinstance(rows, list)
    for row in rows:
        assert isinstance(row, dict)
        archetype_id = str(row["archetype_id"])
        directory = root / f"{archetype_id}_{row['target_id']}"
        bundle = bundles[archetype_id]
        _write_json(directory / CANARY_RESULT_NAME, bundle["result"])
        _write_json(directory / CANARY_RECEIPT_NAME, bundle["receipt"])
        reviews = bundle["reviews"]
        assert isinstance(reviews, list)
        for name, review in zip(CANARY_REVIEW_NAMES, reviews):
            _write_json(directory / CANARY_REVIEWS_DIRECTORY / name, review)


class E2RV6CanaryResultsTests(unittest.TestCase):
    def test_exact_five_results_and_ten_independent_reviews_compile(self) -> None:
        selection = _selection()
        result = compile_cross_archetype_canary_results(
            selection=selection,
            bundles_by_archetype=_bundles(selection),
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_PASS)
        self.assertEqual(result["complete_canary_count"], 5)
        self.assertEqual(result["independent_review_count"], 10)
        summary = result["summary"]
        assert isinstance(summary, dict)
        validate_cross_archetype_canary_summary(summary, selection=selection)
        self.assertEqual(len(summary["canaries"]), 5)

    def test_missing_result_or_one_reviewer_is_pending_and_has_no_summary(self) -> None:
        selection = _selection()
        bundles = _bundles(selection)
        bundles.pop(REQUIRED_ARCHETYPES[-1])
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_PENDING)
        self.assertIsNone(result["summary"])

        bundles = _bundles(selection)
        reviews = bundles[REQUIRED_ARCHETYPES[0]]["reviews"]
        assert isinstance(reviews, list)
        reviews.pop()
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)
        self.assertIsNone(result["summary"])

    def test_duplicate_reviewer_and_cross_canary_swap_fail_closed(self) -> None:
        selection = _selection()
        bundles = _bundles(selection)
        first = bundles[REQUIRED_ARCHETYPES[0]]
        reviews = first["reviews"]
        assert isinstance(reviews, list)
        reviews[1] = dict(reviews[0])
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)

        bundles = _bundles(selection)
        first_reviews = bundles[REQUIRED_ARCHETYPES[0]]["reviews"]
        second_reviews = bundles[REQUIRED_ARCHETYPES[1]]["reviews"]
        assert isinstance(first_reviews, list)
        assert isinstance(second_reviews, list)
        second_result = bundles[REQUIRED_ARCHETYPES[1]]["result"]
        second_receipt = bundles[REQUIRED_ARCHETYPES[1]]["receipt"]
        assert isinstance(second_result, dict)
        assert isinstance(second_receipt, dict)
        second_reviews[0] = build_independent_canary_review(
            reviewer_id="/root/reviewer_a",
            provider_call_id=str(first_reviews[0]["provider_call_id"]),
            prompt_hash=hashlib.sha256(b"new prompt").hexdigest(),
            response_hash=hashlib.sha256(b"new response").hexdigest(),
            result=second_result,
            receipt=second_receipt,
        )
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)

        bundles = _bundles(selection)
        bundles[REQUIRED_ARCHETYPES[0]]["receipt"] = bundles[
            REQUIRED_ARCHETYPES[1]
        ]["receipt"]
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)

    def test_score_stage_and_forbidden_provenance_tampering_fail(self) -> None:
        selection = _selection()
        bundles = _bundles(selection)
        result_payload = bundles[REQUIRED_ARCHETYPES[0]]["result"]
        assert isinstance(result_payload, dict)
        result_payload["total_score"] = 99.0
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)

        bundles = _bundles(selection)
        result_payload = bundles[REQUIRED_ARCHETYPES[0]]["result"]
        assert isinstance(result_payload, dict)
        result_payload["provider_call_counts"] = {"QWEN": 4}
        body = {key: value for key, value in result_payload.items() if key != "result_id"}
        result_payload["result_id"] = "CANARYRUN-" + stable_hash(body)[:24]
        result = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=bundles
        )
        self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)

    def test_directory_loader_rejects_extra_symlink_and_reports_absence_pending(self) -> None:
        selection = _selection()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "live"
            missing = compile_cross_archetype_canary_directory(
                selection=selection, live_root=root
            )
            self.assertEqual(missing["status"], CANARY_COMPILATION_PENDING)

            bundles = _bundles(selection)
            _write_live_tree(root, selection, bundles)
            complete = compile_cross_archetype_canary_directory(
                selection=selection, live_root=root
            )
            self.assertEqual(complete["status"], CANARY_COMPILATION_PASS)

            (root / "foreign").mkdir()
            invalid = compile_cross_archetype_canary_directory(
                selection=selection, live_root=root
            )
            self.assertEqual(invalid["status"], CANARY_COMPILATION_FAIL)
            (root / "foreign").rmdir()

            first_row = selection["selections"][0]
            assert isinstance(first_row, dict)
            canary_root = root / f"{first_row['archetype_id']}_{first_row['target_id']}"
            result_path = canary_root / CANARY_RESULT_NAME
            original = result_path.read_bytes()
            result_path.unlink()
            target = Path(temporary) / "outside.json"
            target.write_bytes(original)
            result_path.symlink_to(target)
            invalid = compile_cross_archetype_canary_directory(
                selection=selection, live_root=root
            )
            self.assertEqual(invalid["status"], CANARY_COMPILATION_FAIL)

    def test_summary_seal_is_immutable_and_parent_symlink_is_rejected(self) -> None:
        selection = _selection()
        compiled = compile_cross_archetype_canary_results(
            selection=selection, bundles_by_archetype=_bundles(selection)
        )
        summary = compiled["summary"]
        assert isinstance(summary, dict)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            live_root = root / "live"
            _write_live_tree(live_root, selection, _bundles(selection))
            destination = root / "trusted" / "summary.json"
            seal_cross_archetype_canary_summary(
                destination, summary, selection=selection, live_root=live_root
            )
            first_inode = destination.stat().st_ino
            seal_cross_archetype_canary_summary(
                destination, summary, selection=selection, live_root=live_root
            )
            self.assertEqual(destination.stat().st_ino, first_inode)

            changed = json.loads(json.dumps(summary))
            changed["canaries"][0]["canonical_stage"] = "1"
            body = {key: value for key, value in changed.items() if key != "summary_id"}
            changed["summary_id"] = "CANARYSUM-" + stable_hash(body)[:24]
            with self.assertRaises(ValueError):
                seal_cross_archetype_canary_summary(
                    destination,
                    changed,
                    selection=selection,
                    live_root=live_root,
                )

            outside = root / "outside"
            outside.mkdir()
            linked_parent = root / "linked"
            linked_parent.symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                seal_cross_archetype_canary_summary(
                    linked_parent / "summary.json",
                    summary,
                    selection=selection,
                    live_root=live_root,
                )

    def test_hardlinked_input_is_rejected(self) -> None:
        selection = _selection()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "live"
            _write_live_tree(root, selection, _bundles(selection))
            first_row = selection["selections"][0]
            assert isinstance(first_row, dict)
            canary_root = root / f"{first_row['archetype_id']}_{first_row['target_id']}"
            source = canary_root / CANARY_RESULT_NAME
            replacement = Path(temporary) / "hardlinked.json"
            source.rename(replacement)
            os.link(replacement, source)
            result = compile_cross_archetype_canary_directory(
                selection=selection, live_root=root
            )
            self.assertEqual(result["status"], CANARY_COMPILATION_FAIL)

    def test_cli_does_not_create_summary_while_actual_results_are_missing(self) -> None:
        selection = _selection()
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary).resolve()
            cutover = repo / "docs/operational/e2r_v6_operational_cutover"
            selection_path = cutover / "cross_archetype_canary_selection.json"
            seal_cross_archetype_canary_selection(selection_path, selection)
            summary_path = cutover / "cross_archetype_canary_summary.json"
            with patch(
                "e2r.cli.compile_e2r_v6_cross_archetype_canaries."
                "canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.cli.compile_e2r_v6_cross_archetype_canaries."
                "_repository_identity_is_trusted",
                return_value=True,
            ), redirect_stdout(io.StringIO()):
                exit_code = canary_cli_main(["--repo-root", str(repo)])
            self.assertEqual(exit_code, 2)
            self.assertFalse(summary_path.exists())

            _write_live_tree(
                cutover / "current_live_canaries",
                selection,
                _bundles(selection),
            )
            with patch(
                "e2r.cli.compile_e2r_v6_cross_archetype_canaries."
                "canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.cli.compile_e2r_v6_cross_archetype_canaries."
                "_repository_identity_is_trusted",
                return_value=True,
            ), redirect_stdout(io.StringIO()):
                exit_code = canary_cli_main(["--repo-root", str(repo)])
            self.assertEqual(exit_code, 0)
            self.assertTrue(summary_path.is_file())


if __name__ == "__main__":
    unittest.main()
