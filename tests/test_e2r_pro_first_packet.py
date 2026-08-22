from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.packet import (
    DeltaResearchContext,
    PacketBuildInput,
    ResearchPacketBuilder,
    write_packet_bundle,
)
from e2r.pro_first.prompt_contract import ProResearchPromptContract
from e2r.research_brain.researcher_mode.schemas import (
    ComponentAnchor,
    HistoricalResearchJudgment,
)


class ProFirstPacketTest(unittest.TestCase):
    def setUp(self) -> None:
        self.builder = ResearchPacketBuilder()
        self.base = PacketBuildInput(
            job_id="PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa",
            run_id="PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb",
            symbol="123456",
            company_name="검증기업",
            aliases=("검증 기업", "VERIFY CORP"),
            as_of_date="2026-08-22",
            latest_trading_snapshot_date="2026-08-21",
            research_mode="FULL_RESEARCH",
            trigger_summary=(
                {
                    "trigger_id": "TRIGGER-1",
                    "event_date": "2026-08-22",
                    "reason": "official disclosure",
                },
            ),
            candidate_archetypes=("C06",),
            business_snapshot={"segments": ["A", "B"], "snapshot_date": "2026-08-22"},
            structured_financial_snapshot={"fcf": 100.0, "as_of_date": "2026-08-22"},
            revision_valuation_snapshot={"revision": "UP", "source_date": "2026-08-21"},
            known_positive_facts=(
                {
                    "fact_id": "FACT-1",
                    "statement": "공식 계약이 확인됨",
                    "publication_date": "2026-08-22",
                    "url": "https://example.invalid/official/1",
                },
            ),
            known_counterfacts=(),
            research_objectives=("FCF와 계약 질을 독립 검증",),
            source_preferences=("issuer official", "customer official"),
            forbidden_inferences=("미확인을 ABSENT로 단정",),
        )

    def test_packet_schema_valid(self) -> None:
        packet = self.builder.build(self.base)
        self.assertEqual(packet.payload["schema_version"], "e2r_pro_research_packet_v1")
        self.assertEqual(len(packet.packet_hash), 64)
        with TemporaryDirectory() as directory:
            receipt = write_packet_bundle(
                packet,
                directory,
                commit_sha="deadbeef",
                config_hash="c" * 64,
            )
            self.assertEqual(
                json.loads(receipt.research_packet_json.read_text(encoding="utf-8")),
                packet.payload,
            )
            manifest = json.loads(receipt.packet_manifest.read_text(encoding="utf-8"))
            self.assertEqual(manifest["packet_hash"], packet.packet_hash)
            self.assertIn("score_authority: `false`", receipt.research_packet_markdown.read_text(encoding="utf-8"))

    def test_packet_has_no_expected_score(self) -> None:
        packet = self.builder.build(self.base)
        encoded = json.dumps(packet.payload, ensure_ascii=False, sort_keys=True).lower()
        self.assertNotIn("expected_score", encoded)
        self.assertNotIn("expected_final_score", encoded)
        self.assertFalse(packet.payload["score_authority"])

    def test_packet_has_no_expected_stage(self) -> None:
        packet = self.builder.build(self.base)
        encoded = json.dumps(packet.payload, ensure_ascii=False, sort_keys=True).lower()
        self.assertNotIn("expected_stage", encoded)
        self.assertNotIn("expected_final_stage", encoded)
        self.assertFalse(packet.payload["stage_authority"])

    def test_packet_blocks_future_source(self) -> None:
        future = replace(
            self.base,
            known_positive_facts=(
                {
                    "fact_id": "FUTURE",
                    "statement": "미래 공시",
                    "publication_date": "2026-08-23",
                },
            ),
        )
        with self.assertRaisesRegex(ValueError, "future source date"):
            self.builder.build(future)

    def test_anchor_digest_is_blind_safe(self) -> None:
        judgment = HistoricalResearchJudgment(
            judgment_id="HJ-1",
            research_case_id="CASE-1",
            archetype_id="C06",
            as_of_date="2025-01-01",
            source_quality="PRIMARY",
            fact_signatures=("FACT-A", "FACT-B", "FACT-C", "FACT-D"),
            counter_fact_signatures=("RISK-A",),
            score_schema_type="DIRECT_COMPONENT_POINTS",
            normalized_component_vector={"growth_quality": 8.0},
            component_max_points={"growth_quality": 10.0},
            reported_total_proxy=88.0,
            reported_stage="3-Green",
            future_outcome_ref="future winner",
            usable_as_exact_anchor=True,
            usable_as_ordinal_anchor=True,
            anchor_confidence="HIGH",
            company_name="과거기업",
            symbol="999999",
            source_file="historical.md",
            source_row_ids=("ROW-1",),
            score_source_row_ids=("SCORE-1",),
            score_mapping_confidence="HIGH",
        )
        proxy = self._component_anchor(
            "ANCHOR-PROXY",
            proxy=True,
            exact=False,
            patterns=("proxy pattern",),
        )
        anchors = (proxy,) + tuple(
            self._component_anchor(f"ANCHOR-{index}", patterns=(f"pattern-{index}",))
            for index in range(1, 4)
        )
        packet = self.builder.build(
            replace(
                self.base,
                historical_judgments=(judgment,),
                component_anchors=anchors,
            )
        )
        digest = packet.payload["historical_anchor_digest"]
        historical = next(row for row in digest if row["digest_kind"] == "HISTORICAL_JUDGMENT")
        encoded = json.dumps(historical, ensure_ascii=False, sort_keys=True)
        self.assertNotIn("reported_stage", encoded)
        self.assertNotIn("reported_total_proxy", encoded)
        self.assertNotIn("normalized_component_vector", encoded)
        self.assertNotIn("future winner", encoded)
        self.assertNotIn("과거기업", encoded)
        self.assertEqual(len(historical["fact_signatures"]), 3)
        component_rows = [row for row in digest if row["digest_kind"] == "COMPONENT_ANCHOR"]
        self.assertEqual(len(component_rows), 3)
        guard = next(row for row in component_rows if row["anchor_id"] == "ANCHOR-PROXY")
        self.assertTrue(guard["guard_only"])
        self.assertFalse(guard["usable_as_exact_anchor"])
        self.assertNotIn("points_mid", guard)

    def test_delta_packet_contains_only_delta_context(self) -> None:
        delta = DeltaResearchContext(
            prior_receipt={
                "receipt_as_of_date": "2026-08-20",
                "score": 70.0,
                "stage": "2",
            },
            new_events=(
                {
                    "event_id": "EVENT-NEW",
                    "event_date": "2026-08-22",
                    "statement": "새 공시",
                },
            ),
            new_or_superseding_facts=(
                {
                    "fact_id": "FACT-NEW",
                    "publication_date": "2026-08-22",
                    "supersedes": "FACT-OLD",
                },
            ),
            components_to_revisit=("growth_quality", "contract_quality"),
        )
        packet = self.builder.build(
            replace(
                self.base,
                research_mode="DELTA_RESEARCH",
                existing_thesis_digest={"thesis_id": "THESIS-1", "as_of_date": "2026-08-20"},
                delta_context=delta,
            )
        )
        self.assertEqual(packet.payload["business_snapshot"], {})
        self.assertEqual(packet.payload["structured_financial_snapshot"], {})
        self.assertEqual(packet.payload["revision_valuation_snapshot"], {})
        self.assertEqual(packet.payload["historical_anchor_digest"], [])
        self.assertEqual(packet.payload["known_positive_facts"], [])
        self.assertEqual(packet.payload["known_counterfacts"], [])
        self.assertEqual(packet.payload["research_objectives"], [])
        self.assertEqual(packet.payload["trigger_summary"], list(delta.new_events))
        self.assertFalse(packet.payload["delta_context"]["prior_receipt_is_current_authority"])

    def test_packet_hash_stable(self) -> None:
        first = self.builder.build(self.base)
        second = self.builder.build(
            replace(self.base, aliases=tuple(reversed(self.base.aliases)))
        )
        self.assertEqual(first.packet_hash, second.packet_hash)
        self.assertEqual(first.to_json(), second.to_json())

    def test_prompt_contract_has_run_markers_and_no_score_authority(self) -> None:
        rendered = ProResearchPromptContract().render(
            job_id=self.base.job_id,
            run_id=self.base.run_id,
            symbol=self.base.symbol,
            as_of_date=self.base.as_of_date,
        )
        self.assertIn(f"[[E2R_PRO_RUN_ID:{self.base.run_id}]]", rendered.text)
        self.assertIn(f"[[E2R_PRO_JOB_ID:{self.base.job_id}]]", rendered.text)
        self.assertIn("E2R_RESEARCH_DOSSIER_JSON_BEGIN", rendered.text)
        self.assertIn("최종 score와 Stage를 결정하거나 제안하지", rendered.text)
        self.assertEqual(
            rendered.output_filename,
            f"E2R_PRO_{self.base.job_id}_{self.base.symbol}_{self.base.as_of_date}.md",
        )
        self.assertEqual(len(rendered.prompt_hash), 64)

    def test_packet_manifest_is_recorded_atomically_and_idempotently(self) -> None:
        with TemporaryDirectory() as directory:
            store = ProFirstJobStore(
                Path(directory) / "packet.sqlite3",
                now=lambda: datetime(2026, 8, 22, tzinfo=timezone.utc),
            )
            candidate = store.create_candidate(
                symbol="123456",
                company_name="검증기업",
                as_of_date="2026-08-22",
                scan_window=ScanWindow.MORNING,
                trigger_fingerprint="trigger-packet",
                research_mode=ResearchMode.FULL_RESEARCH,
                selection_receipt={"blind": True},
            )
            job = store.create_job(candidate.candidate_id)
            job = store.transition(
                job.job_id,
                expected_version=job.state_version,
                to_status=JobStatus.PACKET_BUILDING,
                actor="packet-worker",
                idempotency_key="packet-building",
            )
            packet = self.builder.build(replace(self.base, job_id=job.job_id))
            manifest = {
                "job_id": job.job_id,
                "packet_hash": packet.packet_hash,
                "commit_sha": "deadbeef",
            }
            first = store.record_packet(
                job.job_id,
                expected_version=job.state_version,
                packet_id="PACKET-1",
                packet_hash=packet.packet_hash,
                manifest=manifest,
                actor="packet-worker",
                idempotency_key="packet-ready-once",
            )
            second = store.record_packet(
                job.job_id,
                expected_version=job.state_version,
                packet_id="PACKET-1",
                packet_hash=packet.packet_hash,
                manifest=manifest,
                actor="packet-worker",
                idempotency_key="packet-ready-once",
            )
            self.assertEqual(first.status, JobStatus.PACKET_READY.value)
            self.assertEqual(first.state_version, second.state_version)
            self.assertEqual(first.packet_hash, packet.packet_hash)
            with store._connect() as connection:
                packet_count = connection.execute(
                    "SELECT COUNT(*) FROM pro_packets WHERE job_id=?", (job.job_id,)
                ).fetchone()[0]
            self.assertEqual(packet_count, 1)

    def test_target_conditioned_anchor_is_rejected(self) -> None:
        conditioned = dict(
            self._component_anchor("ANCHOR-CONDITIONED", patterns=("pattern",)).to_dict()
        )
        conditioned["target_symbol_conditioned"] = True
        with self.assertRaisesRegex(ValueError, "target-conditioned"):
            self.builder.build(replace(self.base, component_anchors=(conditioned,)))

    @staticmethod
    def _component_anchor(
        anchor_id: str,
        *,
        proxy: bool = False,
        exact: bool = True,
        patterns: tuple[str, ...],
    ) -> ComponentAnchor:
        return ComponentAnchor(
            anchor_id=anchor_id,
            archetype_id="C06",
            component_id="growth_quality",
            economic_fact_patterns=patterns,
            role="POSITIVE",
            score_band="HIGH",
            points_lower=7.0,
            points_mid=8.0,
            points_upper=9.0,
            max_points=10.0,
            source_backed_case_ids=() if proxy else ("CASE-1",),
            source_proxy_guard_case_ids=("PROXY-1",) if proxy else (),
            source_score_anchor_ids=() if proxy else ("HJ-1",),
            confidence="HIGH",
            usable_as_exact_anchor=exact,
            usable_as_ordinal_anchor=True,
        )


if __name__ == "__main__":
    unittest.main()
