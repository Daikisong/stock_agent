from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from e2r.cli.compile_e2r_v6_artifact_lifecycle import (
    _write_json_atomic,
    main as lifecycle_cli_main,
)
from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    CANARY_RECEIPT_NAME,
    CANARY_RESULT_NAME,
    CANARY_RESULT_PASS,
    CANARY_RESULT_SCHEMA,
    CANARY_REVIEW_NAMES,
    CANARY_REVIEWS_DIRECTORY,
    build_full_researcher_mode_canary_receipt,
    build_independent_canary_review,
    compile_cross_archetype_canary_results,
)
from e2r.production.v6_canary_selection import (
    NATURAL_SELECTION,
    REQUIRED_ARCHETYPES,
    SELECTION_PASS,
    SELECTION_RECEIPT_SCHEMA,
    SELECTION_SCHEMA,
    summarize_cross_archetype_canary_selection,
)
from e2r.production.v6_production_static_audit import (
    PRODUCTION_STATIC_AUDIT_LEAF,
    compile_production_static_audit,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    ARTIFACT_LIFECYCLE_FAIL,
    ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA,
    ARTIFACT_LIFECYCLE_PASS,
    CANARY_RECEIPT_DATE,
    CANARY_TARGET_IDS,
    CANONICAL_MANIFEST_NAME,
    CLEAN_CLONE_REPRODUCTION_PASS,
    CLEAN_CLONE_REPRODUCTION_SCHEMA,
    CLEAN_CLONE_TEST_PASS,
    CLEAN_CLONE_TEST_SCHEMA,
    CURRENT_AUTHORITY,
    FINAL_ROOT_RELATIVE,
    FINAL_STATUS_PROJECTION,
    HISTORICAL_SNAPSHOT,
    PRE_GOLD_PENDING_STATUS,
    PROVIDER_RUNTIME_AUDIT_PASS,
    PROVIDER_RUNTIME_AUDIT_SCHEMA,
    SUPERSEDED,
    compile_artifact_lifecycle,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER


def _run_git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=repo, text=True, stderr=subprocess.DEVNULL
    ).strip()


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


_STATIC_AUDIT_FIXTURE: dict[str, object] | None = None


def _static_audit_fixture() -> dict[str, object]:
    global _STATIC_AUDIT_FIXTURE
    if _STATIC_AUDIT_FIXTURE is None:
        _STATIC_AUDIT_FIXTURE = dict(
            compile_production_static_audit(repo_root=Path.cwd())
        )
    return json.loads(json.dumps(_STATIC_AUDIT_FIXTURE))


def _phase106_bundle(
    selection: dict[str, object],
    row: dict[str, object],
) -> dict[str, object]:
    vector = dict(
        zip(CANONICAL_COMPONENT_ORDER, (10.0, 10.0, 10.0, 8.0, 8.0, 2.0, 2.0))
    )
    result_body: dict[str, object] = {
        "schema_version": CANARY_RESULT_SCHEMA,
        "status": CANARY_RESULT_PASS,
        "run_id": "RESEARCHRUN-" + str(row["target_id"]),
        "selection_id": row["selection_id"],
        "selection_roster_hash": selection["selection_roster_hash"],
        "archetype_id": row["archetype_id"],
        "target_id": row["target_id"],
        "as_of_date": CANARY_RECEIPT_DATE,
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
            f"phase106:{row['target_id']}".encode()
        ).hexdigest(),
        "provider_call_counts": {"COLLABORATION_CODEX": 4},
        "provider_error_count": 0,
        "unauthorized_provider_call_count": 0,
        "local_provider_call_count": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    result = {
        **result_body,
        "result_id": "CANARYRUN-" + stable_hash(result_body)[:24],
    }
    receipt = build_full_researcher_mode_canary_receipt(
        result,
        selection=selection,
        selection_row=row,
    )
    reviews = [
        build_independent_canary_review(
            reviewer_id=f"/root/phase106_{reviewer.lower()}",
            provider_call_id=f"COLLABCALL-{row['target_id']}-{reviewer}",
            prompt_hash=hashlib.sha256(
                f"prompt:{row['target_id']}:{reviewer}".encode()
            ).hexdigest(),
            response_hash=hashlib.sha256(
                f"response:{row['target_id']}:{reviewer}".encode()
            ).hexdigest(),
            result=result,
            receipt=receipt,
        )
        for reviewer in ("A", "B")
    ]
    return {"result": result, "receipt": receipt, "reviews": reviews}


class _TrackedDossierFixture:
    def __init__(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.base = Path(self._temporary.name)
        self.repo = self.base / "repo"
        self.repo.mkdir()
        _run_git(self.repo, "init", "-q")
        _run_git(self.repo, "config", "user.email", "phase104@example.invalid")
        _run_git(self.repo, "config", "user.name", "Phase 104 Test")
        self.final = self.repo / FINAL_ROOT_RELATIVE
        self._create_final_tree()
        self.commit("initial tracked dossier")
        self._manifest_payload = self._build_manifest()
        _write_json(
            self.final / CANONICAL_MANIFEST_NAME,
            self._manifest_payload,
        )
        self.commit("track canonical lifecycle manifest")

    def close(self) -> None:
        self._temporary.cleanup()

    def __enter__(self) -> "_TrackedDossierFixture":
        return self

    def __exit__(self, *_args: object) -> None:
        self.close()

    def _create_final_tree(self) -> None:
        self.final.mkdir(parents=True)
        (self.final / "README.md").write_text("# E2R v6 dossier\n", encoding="utf-8")
        _write_json(self.final / "starting_state.json", {"snapshot": "START"})
        for name in (
            "current_krx_census_summary.json",
            "operational_acceptance_reviewer_gate.json",
        ):
            _write_json(self.final / name, {"artifact": name, "complete": True})
        selection_receipts: list[dict[str, object]] = []
        for index, archetype_id in enumerate(REQUIRED_ARCHETYPES, start=1):
            target_id = f"{index:06d}"
            pre_deep_hash = hashlib.sha256(
                f"{archetype_id}:{target_id}".encode("utf-8")
            ).hexdigest()
            selection_receipts.append(
                {
                    "schema_version": SELECTION_RECEIPT_SCHEMA,
                    "selection_id": "SELREC-" + pre_deep_hash[:24],
                    "archetype_id": archetype_id,
                    "target_id": target_id,
                    "company_name": f"회사{index}",
                    "selection_mode": NATURAL_SELECTION,
                    "selection_as_of_date": CANARY_RECEIPT_DATE,
                    "pre_deep_input_hash": pre_deep_hash,
                    "krx_effective_date": CANARY_RECEIPT_DATE,
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
        selection = {
            "schema_version": SELECTION_SCHEMA,
            "status": SELECTION_PASS,
            "selection_as_of_date": CANARY_RECEIPT_DATE,
            "required_archetypes": list(REQUIRED_ARCHETYPES),
            "selections": selection_receipts,
            "selection_count": len(REQUIRED_ARCHETYPES),
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
            "selection_roster_hash": stable_hash(selection_receipts),
        }
        _write_json(self.final / "cross_archetype_canary_selection.json", selection)
        bundles: dict[str, dict[str, object]] = {}
        live_root = self.final / "current_live_canaries"
        for row in selection_receipts:
            archetype_id = str(row["archetype_id"])
            bundle = _phase106_bundle(selection, row)
            bundles[archetype_id] = bundle
            target_root = live_root / f"{archetype_id}_{row['target_id']}"
            _write_json(target_root / CANARY_RESULT_NAME, bundle["result"])
            _write_json(target_root / CANARY_RECEIPT_NAME, bundle["receipt"])
            reviews = bundle["reviews"]
            assert isinstance(reviews, list)
            for name, review in zip(CANARY_REVIEW_NAMES, reviews):
                _write_json(target_root / CANARY_REVIEWS_DIRECTORY / name, review)
        compiled = compile_cross_archetype_canary_results(
            selection=selection,
            bundles_by_archetype=bundles,
        )
        assert compiled["status"] == CANARY_COMPILATION_PASS
        _write_json(
            self.final / "cross_archetype_canary_summary.json",
            compiled["summary"],
        )
        (self.final / "current_krx_stage_map_compact.jsonl").write_text(
            '{"target_id":"TEST","canonical_stage":"2"}\n',
            encoding="utf-8",
        )
        (self.final / "operational_cutover_final.md").write_text(
            "\n".join(
                (
                    "# Final",
                    "production_research_status=COMPLETE",
                    "gold_evaluation_status=PASS",
                    "score_status=COMPLETE",
                    "stagecourt_status=FINAL",
                    "score_valid=true",
                    "stage_final=true",
                    "",
                )
            ),
            encoding="utf-8",
        )
        for target_id in CANARY_TARGET_IDS:
            target_root = (
                self.final
                / "canary_receipts"
                / CANARY_RECEIPT_DATE
                / target_id
            )
            target_root.mkdir(parents=True)
            vector = {"eps_fcf_explosion": 10.0, "earnings_visibility": 8.0}
            score = {
                "schema_version": "e2r_v6_score_receipt_v1",
                "receipt_id": f"SCORE-{target_id}",
                "target_id": target_id,
                "component_score_vector": vector,
                "total_score": 18.0,
                "canonical_stage": "2",
                "score_valid": True,
                **dict(FINAL_STATUS_PROJECTION),
            }
            stage = {
                "schema_version": "e2r_v6_stagecourt_receipt_v1",
                "target_id": target_id,
                "score_receipt_id": score["receipt_id"],
                "component_score_vector_hash": stable_hash(vector),
                "total_score": 18.0,
                "canonical_stage": "2",
                "decision_status": "FINAL",
                "score_valid": True,
            }
            _write_json(target_root / "score_receipt.json", score)
            _write_json(target_root / "stagecourt_receipt.json", stage)
            _write_json(target_root / "receipt_manifest.json", {"target_id": target_id})
            for name in (
                "component_decisions.jsonl",
                "scoring_facts.jsonl",
                "judge_decisions.jsonl",
                "source_manifest.jsonl",
                "anchor_manifest.jsonl",
                "provider_calls.jsonl",
            ):
                (target_root / name).write_text(
                    json.dumps({"target_id": target_id, "kind": name}) + "\n",
                    encoding="utf-8",
                )
        clone_root = self.final / "clean_clone"
        receipt_result = {
            "schema_version": "e2r_v6_receipt_only_verification_v1",
            "status": "E2R_V6_RECEIPT_ONLY_REPRODUCTION_PASS",
            "offline": True,
            "critical_count_sum": 0,
            "target_count": 2,
            "target_ids": list(CANARY_TARGET_IDS),
        }
        readiness_result = {
            "schema_version": "e2r_v6_tracked_readiness_v1",
            "status": "E2R_V6_TRACKED_READINESS_PASS",
            "ready": True,
            "offline": True,
            "production_readiness_authority": False,
            "critical_count": 0,
            "same_receipt_replay_variance": 0,
            "target_ids": list(CANARY_TARGET_IDS),
        }
        test_result = {
            "schema_version": CLEAN_CLONE_TEST_SCHEMA,
            "status": CLEAN_CLONE_TEST_PASS,
            "executed_test_count": 100,
            "failed_test_count": 0,
            "error_test_count": 0,
            "critical_count_sum": 0,
            "production_readiness_authority": False,
        }
        _write_json(clone_root / "receipt_recompute_result.json", receipt_result)
        _write_json(clone_root / "tracked_readiness_result.json", readiness_result)
        _write_json(clone_root / "test_result.json", test_result)
        _write_json(
            self.final / "clean_clone_reproduction.json",
            {
                "schema_version": CLEAN_CLONE_REPRODUCTION_SCHEMA,
                "status": CLEAN_CLONE_REPRODUCTION_PASS,
                "as_of_date": CANARY_RECEIPT_DATE,
                "receipt_recompute_result_hash": hashlib.sha256(
                    (clone_root / "receipt_recompute_result.json").read_bytes()
                ).hexdigest(),
                "tracked_readiness_result_hash": hashlib.sha256(
                    (clone_root / "tracked_readiness_result.json").read_bytes()
                ).hexdigest(),
                "test_result_hash": hashlib.sha256(
                    (clone_root / "test_result.json").read_bytes()
                ).hexdigest(),
                "critical_count_sum": 0,
                "production_readiness_authority": False,
            },
        )
        _write_json(
            self.final / "provider_runtime_audit.json",
            {
                "schema_version": PROVIDER_RUNTIME_AUDIT_SCHEMA,
                "status": PROVIDER_RUNTIME_AUDIT_PASS,
                "as_of_date": CANARY_RECEIPT_DATE,
                "provider_call_counts": {"COLLABORATION_CODEX": 1},
                "scored_fact_provider_lineage_counts": {"COLLABORATION_CODEX": 1},
                "provider_error_count": 0,
                "unauthorized_provider_call_count": 0,
                "local_provider_call_count": 0,
                "qwen_call_count": 0,
                "ollama_call_count": 0,
                "inherited_qwen_scored_fact_count": 0,
                "inherited_ollama_scored_fact_count": 0,
                "critical_count_sum": 0,
                "production_readiness_authority": False,
            },
        )
        _write_json(
            self.final / PRODUCTION_STATIC_AUDIT_LEAF,
            _static_audit_fixture(),
        )

    def commit(self, message: str) -> str:
        _run_git(self.repo, "add", "-A")
        _run_git(self.repo, "commit", "-qm", message)
        return _run_git(self.repo, "rev-parse", "HEAD")

    def _build_manifest(self) -> dict[str, object]:
        head = _run_git(self.repo, "rev-parse", "HEAD")
        audit_path = self.final / "artifact_lifecycle_audit.json"
        artifacts: list[dict[str, object]] = []
        for path in sorted(item for item in self.final.rglob("*") if item.is_file()):
            if path in {audit_path, self.final / CANONICAL_MANIFEST_NAME}:
                continue
            relative = path.relative_to(self.repo).as_posix()
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            artifact_id = "ART-" + hashlib.sha256(relative.encode()).hexdigest()[:20]
            historical = path == self.final / "starting_state.json"
            artifacts.append(
                {
                    "artifact_id": artifact_id,
                    "artifact_path": relative,
                    "artifact_role": (
                        HISTORICAL_SNAPSHOT if historical else CURRENT_AUTHORITY
                    ),
                    "authority_scope": relative,
                    "as_of_date": "2026-07-12",
                    "generated_at": "2026-08-09T01:02:03+09:00",
                    "commit_sha": head,
                    "content_hash": digest,
                    "supersedes": [],
                    "superseded_by": None,
                    "production_readiness_authority": not historical,
                }
            )
        return {
            "schema_version": ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA,
            "artifacts": artifacts,
            "status_projection": dict(FINAL_STATUS_PROJECTION),
        }

    def manifest(self) -> dict[str, object]:
        return json.loads(json.dumps(self._manifest_payload))

    def install_manifest(self, manifest: dict[str, object], message: str) -> None:
        _write_json(self.final / CANONICAL_MANIFEST_NAME, manifest)
        self.commit(message)
        self._manifest_payload = json.loads(json.dumps(manifest))

    def replace_artifact_and_reseal(
        self,
        relative: str,
        payload: object,
        message: str,
    ) -> None:
        _write_json(self.final / relative, payload)
        self.commit(f"{message} payload")
        self.install_manifest(self._build_manifest(), f"{message} manifest")

    def compile(self, manifest: dict[str, object] | None = None) -> dict[str, object]:
        return dict(
            compile_artifact_lifecycle(
                manifest or self.manifest(),
                repo_root=self.repo,
                prospective_audit_path=self.final / "artifact_lifecycle_audit.json",
            )
        )

    @staticmethod
    def row_for(manifest: dict[str, object], suffix: str) -> dict[str, object]:
        rows = manifest["artifacts"]
        assert isinstance(rows, list)
        return next(
            row
            for row in rows
            if isinstance(row, dict) and str(row["artifact_path"]).endswith(suffix)
        )


class E2RV6ArtifactLifecycleTests(unittest.TestCase):
    def setUp(self) -> None:
        trust = patch(
            "e2r.research_brain.researcher_mode.artifact_lifecycle."
            "_repository_identity_is_trusted",
            return_value=True,
        )
        trust.start()
        self.addCleanup(trust.stop)

    def test_untrusted_repository_cannot_publish_current_authority(self) -> None:
        with _TrackedDossierFixture() as fixture, patch(
            "e2r.research_brain.researcher_mode.artifact_lifecycle."
            "_repository_identity_is_trusted",
            return_value=False,
        ):
            result = fixture.compile()
        self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
        self.assertEqual(
            result["critical_counts"]["repository_identity_untrusted_count"], 1
        )
        self.assertFalse(result["criteria"]["repository_identity_trusted"])

    def test_complete_tracked_dossier_passes_without_synthesizing_authority(self) -> None:
        with _TrackedDossierFixture() as fixture:
            result = fixture.compile()

            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_PASS)
            self.assertTrue(result["ready"])
            self.assertEqual(result["critical_count_sum"], 0)
            self.assertEqual(
                result["hard_acceptance_counts"],
                {
                    "current_authority_contradiction_count": 0,
                    "stale_snapshot_masquerading_current_count": 0,
                    "pending_status_after_gold_pass_count": 0,
                    "score_stage_receipt_mismatch_count": 0,
                },
            )
            self.assertTrue(result["authority_not_synthesized"])
            self.assertFalse(result["score_or_stage_authority"])
            self.assertFalse(
                (fixture.final / "artifact_lifecycle_audit.json").exists()
            )
            static_row = _TrackedDossierFixture.row_for(
                fixture.manifest(),
                PRODUCTION_STATIC_AUDIT_LEAF,
            )
            self.assertEqual(static_row["artifact_role"], CURRENT_AUTHORITY)
            self.assertTrue(static_row["production_readiness_authority"])
            self.assertEqual(result["required_current_authority_failures"], [])

    def test_phase104_does_not_require_phase109_terminal_publications(self) -> None:
        with _TrackedDossierFixture() as fixture:
            for name in (
                "operational_acceptance_reviewer_gate.json",
                "operational_cutover_final.md",
            ):
                (fixture.final / name).unlink()
            fixture.commit("remove phase109 terminal publications")
            manifest = fixture._build_manifest()
            fixture.install_manifest(
                manifest,
                "track lifecycle before phase109 publication",
            )

            result = fixture.compile(manifest)

            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_PASS)
            self.assertEqual(result["critical_count_sum"], 0)
            missing = "\n".join(result["missing_required_final_files"])
            self.assertNotIn("operational_acceptance_reviewer_gate.json", missing)
            self.assertNotIn("operational_cutover_final.md", missing)

    def test_canonical_manifest_and_semantic_pass_artifacts_are_not_self_attested(self) -> None:
        mutated_manifest_cases = (
            (
                "clean_clone_reproduction.json",
                {"complete": True},
                "CLEAN_CLONE_REPRODUCTION_CONTRACT_INVALID",
            ),
            (
                "clean_clone/test_result.json",
                {"status": "PASS"},
                "CLEAN_CLONE_TEST_RESULT_NOT_PASS",
            ),
            (
                "provider_runtime_audit.json",
                {"complete": True},
                "PROVIDER_RUNTIME_AUDIT_CONTRACT_INVALID",
            ),
            (
                PRODUCTION_STATIC_AUDIT_LEAF,
                {"complete": True, "critical_count_sum": 0},
                "PRODUCTION_STATIC_AUDIT_CONTRACT_INVALID",
            ),
            (
                "cross_archetype_canary_selection.json",
                {"complete": True},
                "CANARY_SELECTION_CONTRACT_INVALID",
            ),
            (
                "cross_archetype_canary_summary.json",
                {"complete": True},
                "CROSS_ARCHETYPE_CANARY_RESULT_SUMMARY_INVALID",
            ),
        )
        for relative, payload, expected_code in mutated_manifest_cases:
            with self.subTest(relative=relative), _TrackedDossierFixture() as fixture:
                fixture.replace_artifact_and_reseal(
                    relative, payload, f"replace {relative} with placeholder"
                )
                result = fixture.compile()
                self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
                self.assertIn(
                    expected_code,
                    {
                        row["code"]
                        for row in result["semantic_final_artifact_failures"]
                    },
                )
                self.assertGreater(
                    result["critical_counts"][
                        "semantic_final_artifact_contract_failure_count"
                    ],
                    0,
                )

        with _TrackedDossierFixture() as fixture:
            forged = fixture.manifest()
            forged["status_projection"]["score_valid"] = False
            result = fixture.compile(forged)
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                result["critical_counts"][
                    "canonical_lifecycle_manifest_unbound_count"
                ],
                1,
            )
            self.assertFalse(
                result["criteria"][
                    "canonical_lifecycle_manifest_is_tracked_and_exact"
                ]
            )

        with _TrackedDossierFixture() as fixture:
            selection = json.loads(
                (fixture.final / "cross_archetype_canary_selection.json").read_text(
                    encoding="utf-8"
                )
            )
            fixture.replace_artifact_and_reseal(
                "cross_archetype_canary_summary.json",
                summarize_cross_archetype_canary_selection(selection),
                "replace Phase106 result with Phase105 projection",
            )
            result = fixture.compile()
            self.assertIn(
                "CROSS_ARCHETYPE_CANARY_RESULT_SUMMARY_INVALID",
                {
                    row["code"]
                    for row in result["semantic_final_artifact_failures"]
                },
            )

        with _TrackedDossierFixture() as fixture:
            provider_path = fixture.final / "provider_runtime_audit.json"
            provider = json.loads(provider_path.read_text(encoding="utf-8"))
            provider["provider_call_counts"] = {"OLLAMA": 1}
            fixture.replace_artifact_and_reseal(
                "provider_runtime_audit.json",
                provider,
                "forge provider map while zeroing explicit local counts",
            )
            result = fixture.compile()
            self.assertIn(
                "PROVIDER_RUNTIME_AUDIT_CONTRACT_INVALID",
                {
                    row["code"]
                    for row in result["semantic_final_artifact_failures"]
                },
            )

    def test_git_content_binding_and_path_escape_fail_closed(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            (fixture.final / "README.md").write_text(
                "# changed after manifest\n", encoding="utf-8"
            )
            result = fixture.compile(manifest)
            readme = next(
                row
                for row in result["artifact_validations"]
                if str(row["artifact_path"]).endswith("README.md")
            )
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertIn(
                "GIT_BINDING:head_index_worktree_match", readme["errors"]
            )
            self.assertIn("GIT_BINDING:content_hash_matches", readme["errors"])

        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            row = _TrackedDossierFixture.row_for(manifest, "README.md")
            row["artifact_path"] = "../outside.json"
            result = fixture.compile(manifest)
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertIn(
                "ARTIFACT_PATH_INVALID_OR_OUTSIDE_FINAL_ROOT",
                result["invalid_artifact_rows"][0]["errors"],
            )

        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            row = _TrackedDossierFixture.row_for(manifest, "README.md")
            row["artifact_path"] = (
                f"{FINAL_ROOT_RELATIVE.as_posix()}/bad\nname.json"
            )
            result = fixture.compile(manifest)
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertIn(
                "ARTIFACT_PATH_INVALID_OR_OUTSIDE_FINAL_ROOT",
                result["invalid_artifact_rows"][0]["errors"],
            )

    def test_final_root_cannot_be_redirected_away_from_contract_path(self) -> None:
        with _TrackedDossierFixture() as fixture:
            result = compile_artifact_lifecycle(
                fixture.manifest(),
                repo_root=fixture.repo,
                final_root="docs/a-different-final-root",
                prospective_audit_path=(
                    fixture.repo
                    / "docs/a-different-final-root/artifact_lifecycle_audit.json"
                ),
            )
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                result["critical_counts"]["final_root_argument_invalid_count"], 1
            )

    def test_symlink_in_final_tree_is_rejected(self) -> None:
        with _TrackedDossierFixture() as fixture:
            link = fixture.final / "linked-outside.json"
            link.symlink_to(fixture.base / "outside.json")
            result = fixture.compile()
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(result["critical_counts"]["final_tree_symlink_count"], 1)
            self.assertIn(
                link.relative_to(fixture.repo).as_posix(), result["final_tree_symlinks"]
            )

    def test_current_authority_scope_is_unique(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            first = _TrackedDossierFixture.row_for(manifest, "README.md")
            second = _TrackedDossierFixture.row_for(
                manifest, "provider_runtime_audit.json"
            )
            second["authority_scope"] = first["authority_scope"]
            result = fixture.compile(manifest)
            self.assertEqual(
                result["hard_acceptance_counts"][
                    "current_authority_contradiction_count"
                ],
                1,
            )
            self.assertFalse(result["criteria"]["current_authority_scope_unique"])

    def test_supersession_must_be_bidirectional_and_acyclic(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            older = _TrackedDossierFixture.row_for(manifest, "starting_state.json")
            newer = _TrackedDossierFixture.row_for(
                manifest, "operational_cutover_final.md"
            )
            older["artifact_role"] = SUPERSEDED
            older["superseded_by"] = newer["artifact_id"]
            newer["supersedes"] = [older["artifact_id"]]
            fixture.install_manifest(manifest, "track valid supersession manifest")
            self.assertEqual(fixture.compile(manifest)["status"], ARTIFACT_LIFECYCLE_PASS)

            newer["supersedes"] = []
            broken = fixture.compile(manifest)
            self.assertEqual(broken["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                broken["critical_counts"][
                    "supersession_bidirectional_mismatch_count"
                ],
                1,
            )

        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            left = _TrackedDossierFixture.row_for(manifest, "starting_state.json")
            right = _TrackedDossierFixture.row_for(
                manifest, "clean_clone_reproduction.json"
            )
            for row, successor, older in (
                (left, right, right),
                (right, left, left),
            ):
                row["artifact_role"] = SUPERSEDED
                row["production_readiness_authority"] = False
                row["superseded_by"] = successor["artifact_id"]
                row["supersedes"] = [older["artifact_id"]]
            cyclic = fixture.compile(manifest)
            self.assertEqual(cyclic["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(cyclic["critical_counts"]["supersession_cycle_count"], 1)

    def test_four_hard_counts_reject_nested_or_receipt_contradictions(self) -> None:
        cases = (
            (
                "current_authority_contradiction_count",
                "provider_runtime_audit.json",
                {"nested": {"score_valid": False}},
            ),
            (
                "stale_snapshot_masquerading_current_count",
                "provider_runtime_audit.json",
                {"snapshot_status": "SUPERSEDED_PRE_FINAL"},
            ),
            (
                "pending_status_after_gold_pass_count",
                "clean_clone_reproduction.json",
                {
                    "nested": {
                        "production_research_status": PRE_GOLD_PENDING_STATUS
                    }
                },
            ),
        )
        for hard_count, suffix, payload in cases:
            with self.subTest(hard_count=hard_count):
                with _TrackedDossierFixture() as fixture:
                    path = next(
                        item
                        for item in fixture.final.rglob("*")
                        if item.is_file() and item.name == suffix
                    )
                    _write_json(path, payload)
                    fixture.commit(f"mutate {hard_count}")
                    result = fixture.compile()
                    self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
                    self.assertGreater(
                        result["hard_acceptance_counts"][hard_count], 0
                    )

        with _TrackedDossierFixture() as fixture:
            stage_path = (
                fixture.final
                / "canary_receipts"
                / CANARY_RECEIPT_DATE
                / CANARY_TARGET_IDS[0]
                / "stagecourt_receipt.json"
            )
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
            stage["total_score"] = 17.0
            _write_json(stage_path, stage)
            fixture.commit("make score and StageCourt disagree")
            result = fixture.compile()
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                result["hard_acceptance_counts"][
                    "score_stage_receipt_mismatch_count"
                ],
                1,
            )
            self.assertIn(
                "TOTAL_SCORE_MISMATCH",
                result["score_stage_receipt_mismatches"][0]["reasons"],
            )

    def test_missing_required_file_and_directory_never_create_authority(self) -> None:
        with _TrackedDossierFixture() as fixture:
            missing_file = fixture.final / "provider_runtime_audit.json"
            missing_file.unlink()
            missing_dir = next(
                path
                for path in (fixture.final / "current_live_canaries").iterdir()
                if path.name.startswith("C08_")
            )
            shutil.rmtree(missing_dir)
            result = fixture.compile()
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertGreater(
                result["critical_counts"]["missing_required_final_file_count"], 0
            )
            self.assertIn("C08_", result["missing_current_live_canary_prefixes"])
            self.assertTrue(result["authority_not_synthesized"])
            self.assertFalse(missing_file.exists())
            self.assertFalse(
                (fixture.final / "artifact_lifecycle_audit.json").exists()
            )

    def test_cli_writes_result_last_and_preserves_old_output_on_replace_failure(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest_path = fixture.final / CANONICAL_MANIFEST_NAME
            manifest = fixture.manifest()
            output = fixture.final / "artifact_lifecycle_audit.json"
            argv = [
                "compile_e2r_v6_artifact_lifecycle",
                "--manifest",
                str(manifest_path),
                "--repo-root",
                str(fixture.repo),
                "--output",
                str(output),
            ]
            with patch.object(sys, "argv", argv), redirect_stdout(io.StringIO()):
                exit_code = lifecycle_cli_main()
            self.assertEqual(exit_code, 0)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_PASS)
            self.assertFalse(list(output.parent.glob(f".{output.name}.*.tmp")))

            untracked_recheck = compile_artifact_lifecycle(
                manifest, repo_root=fixture.repo
            )
            self.assertEqual(untracked_recheck["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertFalse(
                untracked_recheck["criteria"][
                    "lifecycle_audit_output_contract_satisfied"
                ]
            )
            fixture.commit("track compiled lifecycle audit")
            tracked_recheck = compile_artifact_lifecycle(
                manifest, repo_root=fixture.repo
            )
            self.assertEqual(tracked_recheck["status"], ARTIFACT_LIFECYCLE_PASS)

            original = output.read_bytes()
            with patch("os.replace", side_effect=OSError("simulated crash")):
                with self.assertRaisesRegex(OSError, "simulated crash"):
                    _write_json_atomic(output, {"status": "replacement"})
            self.assertEqual(output.read_bytes(), original)
            self.assertFalse(list(output.parent.glob(f".{output.name}.*.tmp")))

            _write_json(output, {"not": "a lifecycle audit"})
            fixture.commit("track malformed lifecycle audit")
            invalid_existing = compile_artifact_lifecycle(
                manifest, repo_root=fixture.repo
            )
            self.assertEqual(invalid_existing["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertFalse(
                invalid_existing["criteria"][
                    "lifecycle_audit_output_contract_satisfied"
                ]
            )

    def test_atomic_writer_pins_parent_directory_inode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "output"
            parent.mkdir()
            displaced = root / "output-original"
            victim = root / "victim"
            victim.mkdir()
            output = parent / "audit.json"
            original_replace = __import__("os").replace
            attacked = False

            def replace_after_parent_swap(*args, **kwargs):
                nonlocal attacked
                if not attacked:
                    attacked = True
                    parent.rename(displaced)
                    parent.symlink_to(victim, target_is_directory=True)
                return original_replace(*args, **kwargs)

            with patch(
                "e2r.cli.compile_e2r_v6_artifact_lifecycle.os.replace",
                side_effect=replace_after_parent_swap,
            ):
                _write_json_atomic(output, {"status": "safe"})

            self.assertFalse((victim / output.name).exists())
            self.assertEqual(
                json.loads((displaced / output.name).read_text(encoding="utf-8")),
                {"status": "safe"},
            )

    def test_atomic_writer_never_creates_through_a_swapped_symlink_parent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            victim = root / "final-receipts"
            victim.mkdir()
            swapped_parent = root / "outside"
            swapped_parent.symlink_to(victim, target_is_directory=True)
            output = swapped_parent / "new-parent" / "audit.json"
            with self.assertRaises((OSError, ValueError)):
                _write_json_atomic(output, {"status": "forbidden"})
            self.assertFalse((victim / "new-parent").exists())


if __name__ == "__main__":
    unittest.main()
