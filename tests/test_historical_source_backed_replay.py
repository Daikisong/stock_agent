from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from e2r.cli.run_e2r_historical_replay import main as historical_cli_main
from e2r.research_brain.replay import (
    HistoricalHttpResponse,
    compile_historical_source_backed_replay,
    load_historical_source_backed_snapshot,
    write_historical_source_backed_replay,
)


CANARIES = (
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
)


class _FakeTransport:
    def __init__(self, bodies: dict[str, bytes]) -> None:
        self.bodies = bodies
        self.calls: list[str] = []

    def fetch(self, *, url: str, timeout_seconds: int) -> HistoricalHttpResponse:
        self.calls.append(url)
        body = self.bodies.get(url)
        if body is None:
            return HistoricalHttpResponse(
                url=url,
                status_code=503,
                content_type="text/html",
                body=b"",
                error="fixture provider unavailable",
            )
        return HistoricalHttpResponse(
            url=url,
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=body,
        )


class HistoricalSourceBackedReplayTests(unittest.TestCase):
    def test_all_canaries_use_full_fetched_anchor_and_guard_replay(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry_path, bodies = self._write_inputs(root)
            transport = _FakeTransport(bodies)
            result = compile_historical_source_backed_replay(
                registry_path=registry_path,
                repo_root=root,
                transport=transport,
            )
            paths = write_historical_source_backed_replay(
                result,
                output_root=root / "output",
            )

            self.assertEqual(result.manifest["critical_count_sum"], 0)
            self.assertEqual(result.manifest["positive_replay_ready_count"], 6)
            self.assertEqual(result.manifest["guard_replay_ready_count"], 6)
            self.assertEqual(result.manifest["wrong_subject_probe_count"], 1)
            self.assertEqual(result.manifest["registry_source_repair_count"], 3)
            self.assertTrue(
                all(row["anchor_verified"] for row in result.replay_rows)
            )
            self.assertTrue(
                all(row["url_string_only"] is False for row in result.replay_rows)
            )
            self.assertTrue(
                all(row["historical_score_credit"] == 0 for row in result.repair_rows)
            )
            self.assertEqual(
                {row["observed_decision"] for row in result.replay_rows if row["source_role"] == "WRONG_SUBJECT"},
                {"REJECT_SCORE"},
            )
            self.assertTrue(paths["source_backed_replay"].is_file())
            self.assertTrue(paths["source_repair_queue"].is_file())
            self.assertTrue(paths["replay_provenance"].is_file())

            frozen = load_historical_source_backed_snapshot(root / "output")
            self.assertEqual(
                frozen.manifest["source_corpus_hash"],
                result.manifest["source_corpus_hash"],
            )
            self.assertEqual(
                frozen.manifest["replay_leaf_hash"],
                result.manifest["replay_leaf_hash"],
            )

    def test_same_frozen_fetch_has_zero_replay_variance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry_path, bodies = self._write_inputs(root)
            first = compile_historical_source_backed_replay(
                registry_path=registry_path,
                repo_root=root,
                transport=_FakeTransport(bodies),
            )
            second = compile_historical_source_backed_replay(
                registry_path=registry_path,
                repo_root=root,
                transport=_FakeTransport(bodies),
            )
            self.assertEqual(
                first.manifest["source_corpus_hash"],
                second.manifest["source_corpus_hash"],
            )
            self.assertEqual(
                first.manifest["replay_leaf_hash"],
                second.manifest["replay_leaf_hash"],
            )

    def test_future_source_and_fetch_failure_cannot_be_replay_ready(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry_path, bodies = self._write_inputs(root)
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
            registry["cases"][0]["available_date"] = "2024-01-03"
            registry["cases"][0]["as_of_date"] = "2024-01-02"
            registry_path.write_text(json.dumps(registry), encoding="utf-8")
            bodies.pop(registry["cases"][2]["url"])
            result = compile_historical_source_backed_replay(
                registry_path=registry_path,
                repo_root=root,
                transport=_FakeTransport(bodies),
            )
            self.assertGreater(result.manifest["critical_count_sum"], 0)
            self.assertGreater(
                result.manifest["hard_acceptance_counts"][
                    "curated_case_not_replay_ready_count"
                ],
                0,
            )

    def test_cli_requires_explicit_live_source_authorization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(io.StringIO()):
            code = historical_cli_main(
                [
                    "--output-root",
                    tmp,
                    "--source-backed",
                    "true",
                    "--live-source-fetch-authorized",
                    "false",
                ]
            )
            error = json.loads(
                (Path(tmp) / "historical_replay_command_error.json").read_text(
                    encoding="utf-8"
                )
            )
        self.assertEqual(code, 2)
        self.assertEqual(
            error["blocker"],
            "HISTORICAL_LIVE_SOURCE_FETCH_AUTHORIZATION_MISMATCH",
        )

    def test_tampered_frozen_document_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry_path, bodies = self._write_inputs(root)
            result = compile_historical_source_backed_replay(
                registry_path=registry_path,
                repo_root=root,
                transport=_FakeTransport(bodies),
            )
            output = root / "output"
            write_historical_source_backed_replay(result, output_root=output)
            provenance = [
                json.loads(line)
                for line in (output / "historical_replay_provenance.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            document_path = output / provenance[0]["frozen_text_path"]
            document_path.write_text("tampered source\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "text hash mismatch"):
                load_historical_source_backed_snapshot(output)

    @staticmethod
    def _write_inputs(root: Path) -> tuple[Path, dict[str, bytes]]:
        cases: list[dict[str, object]] = []
        bodies: dict[str, bytes] = {}
        for index, archetype_id in enumerate(CANARIES):
            for role in ("POSITIVE", "GUARD"):
                url = f"https://source.test/{index}/{role.lower()}"
                marker = f"Target-{index}"
                quote = f"exact {role.lower()} evidence {index}"
                bodies[url] = (
                    f"<html><body><h1>{marker}</h1><p>{quote}</p>"
                    f"<p>{'full source body ' * 20}</p></body></html>"
                ).encode()
                cases.append(
                    {
                        "case_id": f"CASE-{index}-{role}",
                        "archetype_id": archetype_id,
                        "primitive_id": f"primitive_{index}",
                        "source_role": role,
                        "url": url,
                        "source_type": "OTHER",
                        "source_name": "Fixture full source",
                        "target_entity_id": f"ENTITY-{index}",
                        "target_name": marker,
                        "target_markers": [marker],
                        "published_date": "2024-01-01",
                        "available_date": "2024-01-01",
                        "as_of_date": "2024-01-02",
                        "quote_contains": quote,
                        "predicate": f"predicate {index} {role}",
                        "expected_directness": "DIRECT",
                        "expected_decision": (
                            "ACCEPT_REPLAY_EVIDENCE"
                            if role == "POSITIVE"
                            else "REJECT_SCORE"
                        ),
                    }
                )
        wrong_url = "https://source.test/wrong-subject"
        bodies[wrong_url] = (
            "<html><body><h1>Different Company</h1>"
            "<p>exact wrong subject evidence</p>"
            f"<p>{'full source body ' * 20}</p></body></html>"
        ).encode()
        cases.append(
            {
                "case_id": "CASE-WRONG-SUBJECT",
                "archetype_id": CANARIES[0],
                "primitive_id": "primitive_wrong_subject",
                "source_role": "WRONG_SUBJECT",
                "url": wrong_url,
                "source_type": "OTHER",
                "source_name": "Fixture wrong subject",
                "target_entity_id": "ENTITY-TARGET",
                "target_name": "Missing Target",
                "target_markers": ["Missing Target"],
                "published_date": "2024-01-01",
                "available_date": "2024-01-01",
                "as_of_date": "2024-01-02",
                "quote_contains": "exact wrong subject evidence",
                "predicate": "wrong subject cannot score",
                "expected_directness": "NOT_TARGET_SCOPED",
                "expected_decision": "REJECT_SCORE",
            }
        )
        inventory = {
            "records": [
                {
                    "research_case_id": "INV-PROXY",
                    "canonical_archetype_id": CANARIES[0],
                    "source_urls": ["https://inventory.test/proxy"],
                    "source_proxy_only": True,
                    "evidence_url_pending": False,
                },
                {
                    "research_case_id": "INV-PENDING",
                    "canonical_archetype_id": CANARIES[1],
                    "source_urls": ["https://inventory.test/pending"],
                    "source_proxy_only": False,
                    "evidence_url_pending": True,
                },
                {
                    "research_case_id": "INV-URL-ONLY",
                    "canonical_archetype_id": CANARIES[2],
                    "source_urls": ["https://inventory.test/url-only"],
                    "source_proxy_only": False,
                    "evidence_url_pending": False,
                },
            ]
        }
        inventory_path = root / "inventory.json"
        inventory_path.write_text(json.dumps(inventory), encoding="utf-8")
        registry = {
            "schema_version": "e2r_historical_source_backed_replay_registry_v1",
            "registry_id": "fixture-registry",
            "snapshot_acquired_date": "2026-07-11",
            "inventory_path": str(inventory_path),
            "max_fetch_attempts_per_case": 2,
            "request_timeout_seconds": 5,
            "canary_archetype_ids": list(CANARIES),
            "cases": cases,
        }
        registry_path = root / "registry.json"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        return registry_path, bodies


if __name__ == "__main__":
    unittest.main()
