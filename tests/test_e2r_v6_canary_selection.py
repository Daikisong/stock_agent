from __future__ import annotations

from contextlib import redirect_stdout
from copy import deepcopy
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import (
    FORCED_SELECTION,
    ISSUER_PROFILE_MANIFEST_NAME,
    NATURAL_SELECTION,
    REQUIRED_ARCHETYPES,
    SELECTION_FAIL,
    SELECTION_PASS,
    compile_cross_archetype_canary_selection,
    load_current_issuer_business_profile_manifest,
    load_current_live_selection_inputs,
    load_sealed_cross_archetype_canary_selection,
    seal_current_issuer_business_profile_manifest,
    validate_cross_archetype_canary_selection_manifest,
    seal_cross_archetype_canary_selection,
    summarize_cross_archetype_canary_selection,
)
from e2r.production.v6_issuer_business_profile import (
    IssuerBusinessProfileConfig,
    V6IssuerBusinessProfileMaterializer,
)
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PENDING,
    compile_cross_archetype_canary_directory,
)
from tests.test_e2r_v6_issuer_business_profile import (
    FakeCompatibilityProvider,
    FakeOpenDartFetcher,
)
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.cli.select_e2r_v6_cross_archetype_canaries import (
    CUTOVER_RELATIVE_ROOT,
    main as selection_cli_main,
)
from e2r.cli.materialize_e2r_v6_issuer_business_profiles import (
    load_canonical_profile_inputs,
    materialize_canonical_profile_manifest,
)


class E2RV6CanarySelectionTests(unittest.TestCase):
    AS_OF_DATE = "2026-08-07"

    def _candidate(self, index: int, archetype_id: str) -> dict:
        target_id = f"{index + 1:06d}"
        company_name = f"현재상장사{index + 1}"
        market = "KOSPI" if index % 2 == 0 else "KOSDAQ"
        endpoint = "stk_isu_base_info" if market == "KOSPI" else "ksq_is_base_info"
        # Match the canonical KRX endpoint spelling used by the materializer.
        if market == "KOSDAQ":
            endpoint = "ksq_isu_base_info"
        source_url = (
            f"https://data-dbg.krx.co.kr/svc/apis/sto/{endpoint}"
            f"?basDd={self.AS_OF_DATE.replace('-', '')}"
        )
        request_id = "KRXREQ-" + stable_hash(
            {
                "market": market,
                "effective_date": self.AS_OF_DATE,
                "endpoint": endpoint,
            }
        )[:24]
        source_event_id = f"SOURCE-EVENT-{index}"
        source_ref = f"SRC-{index}"
        trigger_payload = {"report_name": "current official event"}
        if index == 0:
            trigger_payload.update(
                {
                    "price_score_usage": "INVESTIGATION_ONLY",
                    "return_pct": 12.5,
                    "trading_value": 1_500_000_000,
                }
            )
        trigger_id = "TRIG-" + stable_hash(
            {
                "target": target_id,
                "source_event": source_event_id,
                "effective_date": self.AS_OF_DATE,
                "trigger_type": "OFFICIAL",
                "lifecycle_status": "CURRENT",
                "providers": ("KRX_OPENAPI",),
                "payload": trigger_payload,
            }
        )[:24]
        candidate_event_id = "CAND-" + stable_hash(
            {
                "target": target_id,
                "as_of_date": self.AS_OF_DATE,
                "signals": (trigger_id,),
            }
        )[:24]
        depth_id = "DEPTH-" + stable_hash(
            {
                "target": target_id,
                "as_of_date": self.AS_OF_DATE,
                "maximum": "L3_RESEARCH_BRAIN",
                "candidate": candidate_event_id,
            }
        )[:24]
        blind_id = f"BLIND-{index}"
        plan_id = stable_intelligence_id(
            "two-pass-plan", {"blind_input_id": blind_id}
        )
        plan = {
            "plan_id": plan_id,
            "blind_input_id": blind_id,
            "status": "COMPLETE",
            "blind_output": {"input_id": blind_id, "hypotheses": []},
            "critique_output": {
                "top_k_archetypes": [
                    {
                        "archetype_id": archetype_id,
                        "supporting_fact_ids": [f"FACT-{index}"],
                        "contradicting_fact_ids": [],
                        "recipe_ids": [f"RECIPE-{index}"],
                    }
                ],
                "supporting_current_fact_ids": [f"FACT-{index}"],
                "contradicting_current_fact_ids": [],
                "source_task_drafts": [
                    {
                        "recipe_id": f"RECIPE-{index}",
                        "preferred_source_families": ["OPENDART", "ISSUER_IR"],
                        "fallback_source_families": ["TRUSTED_NEWS"],
                    }
                ],
                "abstain": False,
            },
            "pending": None,
            "provider_traces": [
                {
                    "planner_pass": planner_pass,
                    "provider_name": "codex_cli_two_pass_planner",
                    "real_provider": True,
                    "fake_provider": False,
                    "prompt_hash": stable_hash(
                        {"index": index, "planner_pass": planner_pass, "kind": "prompt"}
                    ),
                    "response_hash": stable_hash(
                        {"index": index, "planner_pass": planner_pass, "kind": "response"}
                    ),
                }
                for planner_pass in ("BLIND_HYPOTHESIS", "MEMORY_CRITIQUE")
            ],
            "deterministic_stage_or_score_mutation": False,
        }
        planner_run_id = "LIVEPLAN-" + stable_hash(
            {"target": target_id, "blind_input": blind_id, "plan": plan_id}
        )[:24]
        return {
            "universe_row": {
                "symbol": target_id,
                "company_name": company_name,
                "market": market,
                "security_group": "주권",
                "stock_certificate_type": "보통주",
                "sector_type": "일반",
                "listing_date": "2020-01-01",
                "listing_status": "LISTED",
                "source_effective_date": self.AS_OF_DATE,
                "source_url": source_url,
                "source_document_id": f"krx:{market}:{self.AS_OF_DATE}",
                "source_content_hash": stable_hash(
                    {"market": market, "date": self.AS_OF_DATE}
                ),
                "source_request_id": request_id,
                "source_mode": "LIVE",
                "eligible": True,
                "exclusion_reason": None,
                "raw_fields": {"ISU_SRT_CD": target_id},
                "schema_version": "e2r_live_krx_universe_v1",
            },
            "candidate_event": {
                "candidate_event_id": candidate_event_id,
                "target_id": target_id,
                "target_name": company_name,
                "as_of_date": self.AS_OF_DATE,
                "latest_effective_date": self.AS_OF_DATE,
                "trigger_types": ["OFFICIAL"],
                "trigger_signal_ids": [trigger_id],
                "source_refs": [source_ref],
                "investigation_required": True,
                "active_thesis_present": False,
                "score_evidence_eligible": False,
                "summary": f"{company_name}: OFFICIAL current trigger 1건 검증 필요",
                "schema_version": "e2r_live_candidate_event_v1",
            },
            "depth_decision": {
                "depth_decision_id": depth_id,
                "target_id": target_id,
                "target_name": company_name,
                "as_of_date": self.AS_OF_DATE,
                "completed_depths": [
                    "L0_UNIVERSE",
                    "L1_BASELINE",
                    "L2_OFFICIAL_LIGHT",
                    "L3_RESEARCH_BRAIN",
                ],
                "maximum_depth": "L3_RESEARCH_BRAIN",
                "candidate_event_id": candidate_event_id,
                "trigger_signal_ids": [trigger_id],
                "priority_score": 1.0,
                "selected_for_official_light": True,
                "selected_for_deep": True,
                "selected_for_brain": True,
                "acquisition_eligible": True,
                "selection_reasons": ["current source-backed trigger"],
                "not_selected_reason": None,
                "source_task_budget": {"max_source_tasks": 3},
                "llm_budget": {"max_llm_calls": 2},
                "general_web_budget": {"max_fetches": 1},
                "forced_archetype_quota": False,
                "schema_version": "e2r_live_depth_decision_v1",
            },
            "planner_run": {
                "schema_version": "e2r_live_planner_run_v1",
                "planner_run_id": planner_run_id,
                "target_id": target_id,
                "target_name": company_name,
                "as_of_date": self.AS_OF_DATE,
                "depth_decision_id": depth_id,
                "candidate_event_id": candidate_event_id,
                "trigger_signal_ids": [trigger_id],
                "source_refs": [source_ref],
                "blind_input_id": blind_id,
                "compiled_fact_count": 1,
                "input_compilation_audit": {
                    "input_row_count": 1,
                    "compiled_fact_count": 1,
                    "future_evidence_dropped_count": 0,
                    "invalid_date_evidence_dropped_count": 0,
                    "outcome_evidence_dropped_count": 0,
                    "forbidden_context_evidence_dropped_count": 0,
                    "forbidden_assignment_stripped_count": 0,
                    "score_stage_field_forwarded_count": 0,
                    "archetype_label_field_forwarded_count": 0,
                    "source_primary_field_forwarded_count": 0,
                    "sector_context_forwarded_to_pass_a_count": 0,
                },
                "provider_name": "codex_cli_two_pass_planner",
                "provider_real": True,
                "provider_fake": False,
                "provider_call_count": 2,
                "real_provider_success": True,
                "terminal_status": "COMPLETE",
                "plan": plan,
            },
        }

    def _candidates(self) -> list[dict]:
        return [
            self._candidate(index, archetype_id)
            for index, archetype_id in enumerate(REQUIRED_ARCHETYPES)
        ]

    def _forced_profile_manifest(self, candidates: list[dict]) -> dict:
        industries = {
            candidates[0]["universe_row"]["symbol"]: "26120",
            candidates[1]["universe_row"]["symbol"]: "20110",
            candidates[2]["universe_row"]["symbol"]: "20202",
            candidates[3]["universe_row"]["symbol"]: "21101",
            candidates[4]["universe_row"]["symbol"]: "62010",
        }
        return dict(
            V6IssuerBusinessProfileMaterializer().materialize(
                IssuerBusinessProfileConfig(
                    as_of_date=self.AS_OF_DATE,
                    max_profile_fetches=5,
                ),
                universe_rows=[row["universe_row"] for row in candidates],
                credential="official-fixture-key",
                fetcher=FakeOpenDartFetcher(industries),
                compatibility_provider=FakeCompatibilityProvider(),
            )
        )

    def _abstained_candidates(self) -> list[dict]:
        candidates = self._candidates()
        for candidate in candidates:
            run = candidate["planner_run"]
            run["terminal_status"] = "ABSTAINED"
            run["plan"]["status"] = "ABSTAINED"
            run["plan"]["critique_output"]["abstain"] = True
        return candidates

    def _signal(self, candidate: dict, index: int = 0) -> dict:
        event = candidate["candidate_event"]
        payload = {"report_name": "current official event"}
        if index == 0:
            payload.update(
                {
                    "price_score_usage": "INVESTIGATION_ONLY",
                    "return_pct": 12.5,
                    "trading_value": 1_500_000_000,
                }
            )
        return {
            "trigger_signal_id": event["trigger_signal_ids"][0],
            "target_id": event["target_id"],
            "target_name": event["target_name"],
            "trigger_type": "OFFICIAL",
            "source_event_id": f"SOURCE-EVENT-{index}",
            "effective_date": self.AS_OF_DATE,
            "detected_at": self.AS_OF_DATE,
            "source_refs": list(event["source_refs"]),
            "provider_names": ["KRX_OPENAPI"],
            "subject_direct": True,
            "lifecycle_status": "CURRENT",
            "investigation_required": True,
            "score_evidence_eligible": False,
            "headline_or_snippet_only": False,
            "payload": payload,
            "schema_version": "e2r_live_trigger_signal_v1",
        }

    def _signals(
        self, candidates: list[dict], *, natural_indices: set[int] | None = None
    ) -> list[dict]:
        natural = set(range(len(candidates))) if natural_indices is None else natural_indices
        rows = [self._signal(candidate, index) for index, candidate in enumerate(candidates)]
        for index, row in enumerate(rows):
            if index not in natural:
                row["investigation_required"] = False
        return rows

    def _write_live_root(self, root: Path) -> tuple[list[dict], list[dict]]:
        candidates = self._candidates()
        signals = [self._signal(candidate, index) for index, candidate in enumerate(candidates)]
        prompt_rows = []
        response_rows = []
        for index, candidate in enumerate(candidates):
            traces = candidate["planner_run"]["plan"]["provider_traces"]
            for trace in traces:
                planner_pass = trace["planner_pass"]
                prompt_text = f"blind current prompt {index} {planner_pass}"
                response_payload = (
                    candidate["planner_run"]["plan"]["blind_output"]
                    if planner_pass == "BLIND_HYPOTHESIS"
                    else candidate["planner_run"]["plan"]["critique_output"]
                )
                raw_response = json.dumps(
                    response_payload,
                    sort_keys=True,
                )
                prompt_hash = hashlib.sha256(prompt_text.encode()).hexdigest()
                response_hash = hashlib.sha256(raw_response.encode()).hexdigest()
                trace["prompt_hash"] = prompt_hash
                trace["response_hash"] = response_hash
                call_id = "LLMCALL-" + stable_hash(
                    {
                        "target": candidate["planner_run"]["target_id"],
                        "attempt_id": "initial",
                        "planner_pass": planner_pass,
                        "prompt_hash": prompt_hash,
                    }
                )[:24]
                prompt_rows.append(
                    {
                        "schema_version": "e2r_live_llm_prompt_v1",
                        "call_id": call_id,
                        "target_id": candidate["planner_run"]["target_id"],
                        "attempt_id": "initial",
                        "planner_pass": planner_pass,
                        "provider_name": "codex_cli_two_pass_planner",
                        "prompt_hash": prompt_hash,
                        "prompt_text": prompt_text,
                    }
                )
                response_rows.append(
                    {
                        "schema_version": "e2r_live_llm_response_v1",
                        "call_id": call_id,
                        "target_id": candidate["planner_run"]["target_id"],
                        "attempt_id": "initial",
                        "planner_pass": planner_pass,
                        "provider_name": "codex_cli_two_pass_planner",
                        "status": "COMPLETED",
                        "response_hash": response_hash,
                        "raw_response": raw_response,
                        "response_payload": response_payload,
                        "error_category": None,
                    }
                )

        universe_rows = [deepcopy(row["universe_row"]) for row in candidates]
        for index in range(5, 1000):
            template = deepcopy(candidates[index % len(candidates)]["universe_row"])
            symbol = f"{100000 + index:06d}"
            template["symbol"] = symbol
            template["company_name"] = f"현재전체상장사{index}"
            template["raw_fields"] = {"ISU_SRT_CD": symbol}
            universe_rows.append(template)
        attempts = []
        for market in ("KOSPI", "KOSDAQ"):
            sample = next(row for row in universe_rows if row["market"] == market)
            attempts.append(
                {
                    "market": market,
                    "effective_date": self.AS_OF_DATE,
                    "canonical_url": sample["source_url"],
                    "content_hash": sample["source_content_hash"],
                    "request_id": sample["source_request_id"],
                    "provider_request_id": sample["source_request_id"],
                    "status": "FETCHED",
                    "fetched_at": "2026-08-07T00:00:00+00:00",
                    "error_category": None,
                    "rows": None,
                    "row_count": sum(row["market"] == market for row in universe_rows),
                }
            )

        def write_jsonl(name: str, rows: list[dict]) -> None:
            (root / name).write_text(
                "".join(
                    json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                    for row in rows
                ),
                encoding="utf-8",
            )

        def write_json(name: str, payload: dict) -> None:
            (root / name).write_text(
                json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
                encoding="utf-8",
            )

        write_jsonl("universe_eligible.jsonl", universe_rows)
        write_json(
            "universe_provenance.json",
            {
                "schema_version": "e2r_live_krx_universe_provenance_v1",
                "as_of_date": self.AS_OF_DATE,
                "source_effective_date": self.AS_OF_DATE,
                "status": "CURRENT_UNIVERSE_MATERIALIZATION_PASS",
                "blockers": [],
                "request_attempts": attempts,
                "raw_universe_hash": stable_hash(universe_rows),
                "eligible_universe_hash": stable_hash(universe_rows),
            },
        )
        write_json(
            "universe_audit.json",
            {
                "schema_version": "e2r_live_universe_audit_v1",
                "as_of_date": self.AS_OF_DATE,
                "eligible_universe_count": len(universe_rows),
                "provider_request_count": len(attempts),
                "critical_count_sum": 0,
                "hard_acceptance_pass": True,
            },
        )
        write_jsonl("trigger_signals.jsonl", signals)
        write_jsonl(
            "candidate_events.jsonl",
            [candidate["candidate_event"] for candidate in candidates],
        )
        write_json(
            "trigger_fusion_audit.json",
            {
                "schema_version": "e2r_live_trigger_fusion_audit_v1",
                "as_of_date": self.AS_OF_DATE,
                "trigger_signal_count": len(signals),
                "candidate_event_count": len(candidates),
                "critical_count_sum": 0,
                "hard_acceptance_pass": True,
            },
        )
        depth_rows = [deepcopy(candidate["depth_decision"]) for candidate in candidates]
        for universe_row in universe_rows[len(candidates) :]:
            target_id = universe_row["symbol"]
            depth_rows.append(
                {
                    "depth_decision_id": "DEPTH-"
                    + stable_hash(
                        {
                            "target": target_id,
                            "as_of_date": self.AS_OF_DATE,
                            "maximum": "L1_BASELINE",
                            "candidate": None,
                        }
                    )[:24],
                    "target_id": target_id,
                    "target_name": universe_row["company_name"],
                    "as_of_date": self.AS_OF_DATE,
                    "completed_depths": ["L0_UNIVERSE", "L1_BASELINE"],
                    "maximum_depth": "L1_BASELINE",
                    "candidate_event_id": None,
                    "trigger_signal_ids": [],
                    "priority_score": 0.0,
                    "selected_for_official_light": False,
                    "selected_for_deep": False,
                    "selected_for_brain": False,
                    "acquisition_eligible": False,
                    "selection_reasons": ["current bounded baseline only"],
                    "not_selected_reason": "no current investigation candidate",
                    "source_task_budget": {"max_source_tasks": 0},
                    "llm_budget": {"max_llm_calls": 0},
                    "general_web_budget": {"max_fetches": 0},
                    "forced_archetype_quota": False,
                    "schema_version": "e2r_live_depth_decision_v1",
                }
            )
        write_jsonl(
            "depth_decisions.jsonl",
            depth_rows,
        )
        write_json(
            "candidate_selection_audit.json",
            {
                "schema_version": "e2r_live_depth_selection_audit_v1",
                "as_of_date": self.AS_OF_DATE,
                "depth_decision_count": len(depth_rows),
                "critical_count_sum": 0,
                "hard_acceptance_pass": True,
            },
        )
        write_jsonl(
            "planner_runs.jsonl",
            [candidate["planner_run"] for candidate in candidates],
        )
        write_jsonl("llm_prompts.jsonl", prompt_rows)
        write_jsonl("llm_responses.jsonl", response_rows)
        write_json(
            "planner_validation.json",
            {
                "schema_version": "e2r_live_brain_planner_audit_v1",
                "as_of_date": self.AS_OF_DATE,
                "planner_run_count": len(candidates),
                "planner_call_count": len(response_rows),
                "critical_count_sum": 0,
                "hard_acceptance_pass": True,
            },
        )
        return candidates, signals

    def _rewrite_live_planners_as_abstained(
        self, root: Path, *, omit_top_k: bool
    ) -> None:
        run_path = root / "planner_runs.jsonl"
        runs = [json.loads(line) for line in run_path.read_text().splitlines()]
        for run in runs:
            run["terminal_status"] = "ABSTAINED"
            run["plan"]["status"] = "ABSTAINED"
            critique = run["plan"]["critique_output"]
            critique["abstain"] = True
            if omit_top_k:
                critique.pop("top_k_archetypes")
            raw_response = json.dumps(
                critique, ensure_ascii=False, sort_keys=True
            )
            for trace in run["plan"]["provider_traces"]:
                if trace["planner_pass"] == "MEMORY_CRITIQUE":
                    trace["response_hash"] = hashlib.sha256(
                        raw_response.encode("utf-8")
                    ).hexdigest()
        run_path.write_text(
            "".join(json.dumps(row, sort_keys=True) + "\n" for row in runs),
            encoding="utf-8",
        )

        run_by_target = {row["target_id"]: row for row in runs}
        response_path = root / "llm_responses.jsonl"
        responses = [
            json.loads(line) for line in response_path.read_text().splitlines()
        ]
        for response in responses:
            if response["planner_pass"] != "MEMORY_CRITIQUE":
                continue
            payload = run_by_target[response["target_id"]]["plan"][
                "critique_output"
            ]
            raw_response = json.dumps(
                payload, ensure_ascii=False, sort_keys=True
            )
            response["response_payload"] = payload
            response["raw_response"] = raw_response
            response["response_hash"] = hashlib.sha256(
                raw_response.encode("utf-8")
            ).hexdigest()
        response_path.write_text(
            "".join(json.dumps(row, sort_keys=True) + "\n" for row in responses),
            encoding="utf-8",
        )

    def test_selects_exact_five_without_score_or_stage_visibility(self):
        candidates = self._candidates()
        signals = self._signals(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
        )
        self.assertEqual(result["status"], SELECTION_PASS)
        self.assertEqual(result["selection_count"], 5)
        self.assertTrue(
            all(
                row["selection_mode"] == NATURAL_SELECTION
                for row in result["selections"]
            )
        )
        self.assertEqual(len({row["target_id"] for row in result["selections"]}), 5)
        summary = summarize_cross_archetype_canary_selection(result)
        self.assertEqual(summary["selected_archetype_count"], 5)
        self.assertEqual(summary["target_specific_code_branch_count"], 0)

    def test_forced_exact_five_require_complete_official_profile_and_abstention(self):
        candidates = self._abstained_candidates()
        profile_manifest = self._forced_profile_manifest(candidates)
        signals = self._signals(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
            issuer_business_profile_manifest=profile_manifest,
        )
        self.assertEqual(result["status"], SELECTION_PASS)
        self.assertTrue(
            all(
                row["selection_mode"] == FORCED_SELECTION
                and row["trigger_event_ids"] == []
                and row["direct_current_supporting_fact_ids"] == []
                and row["recipe_ids"] == []
                and row["production_daily_candidate"] is False
                and row["forced_validation_authority"] is False
                and row["score_or_stage_authority"] is False
                and row["gold_authority"] is False
                for row in result["selections"]
            )
        )
        self.assertEqual(
            result["issuer_business_profile_manifest_hash"],
            stable_hash(profile_manifest),
        )
        validate_cross_archetype_canary_selection_manifest(
            result,
            issuer_business_profile_manifest=profile_manifest,
        )

    def test_forced_abstained_exact_five_does_not_require_top_k(self):
        candidates = self._abstained_candidates()
        for candidate in candidates:
            candidate["planner_run"]["plan"]["critique_output"].pop(
                "top_k_archetypes"
            )
        profile_manifest = self._forced_profile_manifest(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
            issuer_business_profile_manifest=profile_manifest,
        )
        self.assertEqual(result["status"], SELECTION_PASS)
        self.assertEqual(result["selection_count"], len(REQUIRED_ARCHETYPES))
        self.assertTrue(
            all(
                row["selection_mode"] == FORCED_SELECTION
                for row in result["selections"]
            )
        )

    def test_forced_selection_reopens_from_tracked_sibling_in_a_clean_clone(self):
        candidates = self._abstained_candidates()
        for candidate in candidates:
            candidate["planner_run"]["plan"]["critique_output"].pop(
                "top_k_archetypes"
            )
        profile_manifest = self._forced_profile_manifest(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
            issuer_business_profile_manifest=profile_manifest,
        )
        with tempfile.TemporaryDirectory() as directory:
            clone_root = Path(directory)
            cutover_root = clone_root / CUTOVER_RELATIVE_ROOT
            profile_path = cutover_root / ISSUER_PROFILE_MANIFEST_NAME
            selection_path = cutover_root / "cross_archetype_canary_selection.json"
            seal_current_issuer_business_profile_manifest(
                profile_path, profile_manifest
            )
            seal_cross_archetype_canary_selection(
                selection_path,
                result,
                issuer_business_profile_manifest=profile_manifest,
            )

            # A git checkout normally restores tracked files as 0644.  No
            # ignored output tree or Collaboration journal is available here.
            profile_path.chmod(0o644)
            selection_path.chmod(0o644)
            self.assertFalse((clone_root / "output").exists())
            reopened = load_sealed_cross_archetype_canary_selection(selection_path)
            self.assertEqual(reopened["status"], SELECTION_PASS)
            self.assertEqual(
                reopened["selection_roster_hash"],
                result["selection_roster_hash"],
            )
            validate_cross_archetype_canary_selection_manifest(reopened)
            downstream = compile_cross_archetype_canary_directory(
                selection=reopened,
                live_root=cutover_root / "current_live_canaries",
            )
            self.assertEqual(downstream["status"], CANARY_COMPILATION_PENDING)

            profile_path.unlink()
            with self.assertRaisesRegex(ValueError, "unavailable"):
                load_sealed_cross_archetype_canary_selection(selection_path)

    def test_forced_selection_fails_without_complete_exact_profile(self):
        candidates = self._abstained_candidates()
        signals = self._signals(candidates)
        missing = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
        )
        self.assertEqual(missing["status"], SELECTION_FAIL)
        profile_manifest = self._forced_profile_manifest(candidates)
        pending = deepcopy(profile_manifest)
        pending["status"] = "PENDING"
        pending["audit"]["production_acceptance_pass"] = False
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
            issuer_business_profile_manifest=pending,
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertIn(
            "INVALID_ISSUER_BUSINESS_PROFILE_MANIFEST",
            {row["code"] for row in result["failures"]},
        )
        pending_planner_candidates = self._abstained_candidates()
        current_profile = self._forced_profile_manifest(pending_planner_candidates)
        pending_planner_candidates[0]["planner_run"]["terminal_status"] = "PENDING"
        pending_planner_candidates[0]["planner_run"]["plan"]["status"] = "PENDING"
        planner_pending = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=pending_planner_candidates,
            trigger_events=self._signals(pending_planner_candidates),
            issuer_business_profile_manifest=current_profile,
        )
        self.assertEqual(planner_pending["status"], SELECTION_FAIL)

    def test_forced_profile_tamper_and_natural_mislabel_fail_closed(self):
        candidates = self._abstained_candidates()
        profile_manifest = self._forced_profile_manifest(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
            issuer_business_profile_manifest=profile_manifest,
        )
        tampered_profile = deepcopy(profile_manifest)
        tampered_profile["selections"][0]["exact_quote_hash"] = "0" * 64
        with self.assertRaises(ValueError):
            validate_cross_archetype_canary_selection_manifest(
                result,
                issuer_business_profile_manifest=tampered_profile,
            )
        mislabeled = deepcopy(result)
        mislabeled["selections"][0]["selection_mode"] = NATURAL_SELECTION
        mislabeled["selection_roster_hash"] = stable_hash(mislabeled["selections"])
        with self.assertRaisesRegex(ValueError, "identity|lineage"):
            validate_cross_archetype_canary_selection_manifest(
                mislabeled,
                issuer_business_profile_manifest=profile_manifest,
            )

    def test_rejects_post_score_alias_and_candidate_schema_extension(self):
        candidates = self._candidates()
        candidates[0]["ranking_points_after_deep"] = 92.0
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertEqual(result["critical_counts"]["post_score_target_selection_count"], 1)

        candidates = self._candidates()
        signals = self._signals(candidates)
        signals[0]["payload"]["price_score_usage"] = "FINAL_SCORE"
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertIn(
            "POST_DEEP_SCORE_OR_STAGE_VISIBLE_AT_SELECTION",
            {row["code"] for row in result["failures"]},
        )

    def test_empty_required_roster_cannot_bypass_exact_five_contract(self):
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=self._candidates(),
            trigger_events=(),
            required_archetypes=(),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertIn(
            "REQUIRED_ARCHETYPE_CONTRACT_MISMATCH",
            {row["code"] for row in result["failures"]},
        )

    def test_planner_and_krx_identity_are_recomputed(self):
        for field, value in (
            ("planner_run_id", "LIVEPLAN-FORGED"),
            ("plan_hash", "not-an-input-field"),
        ):
            candidates = self._candidates()
            if field == "plan_hash":
                candidates[0]["planner_run"]["plan"]["plan_id"] = value
            else:
                candidates[0]["planner_run"][field] = value
            result = compile_cross_archetype_canary_selection(
                selection_as_of_date=self.AS_OF_DATE,
                candidates=candidates,
                trigger_events=(),
            )
            self.assertEqual(result["status"], SELECTION_FAIL)

        candidates = self._candidates()
        candidates[0]["universe_row"]["source_request_id"] = "KRXREQ-FORGED"
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)

        for field in ("candidate_event_id", "depth_decision_id"):
            candidates = self._candidates()
            owner = (
                candidates[0]["candidate_event"]
                if field == "candidate_event_id"
                else candidates[0]["depth_decision"]
            )
            owner[field] = f"{field.upper()}-FORGED"
            result = compile_cross_archetype_canary_selection(
                selection_as_of_date=self.AS_OF_DATE,
                candidates=candidates,
                trigger_events=(),
            )
            self.assertEqual(result["status"], SELECTION_FAIL)

        candidates = self._candidates()
        candidates[0]["planner_run"]["provider_name"] = (
            "codex_forged_without_validated_call_receipt"
        )
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)

        candidates = self._candidates()
        candidates[0]["planner_run"]["plan"]["provider_traces"] = []
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)

        candidates = self._candidates()
        old_date = "2020-01-01"
        row = candidates[0]["universe_row"]
        row["source_effective_date"] = old_date
        endpoint = row["source_url"].split("?", 1)[0].rsplit("/", 1)[-1]
        row["source_url"] = (
            row["source_url"].split("?", 1)[0]
            + "?basDd="
            + old_date.replace("-", "")
        )
        row["source_request_id"] = "KRXREQ-" + stable_hash(
            {
                "market": row["market"],
                "effective_date": old_date,
                "endpoint": endpoint,
            }
        )[:24]
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)

    def test_empty_or_invalid_trigger_date_is_not_natural(self):
        candidates = self._candidates()
        signal = self._signal(candidates[0])
        signal["effective_date"] = ""
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(signal,),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertIn("INVALID_TRIGGER_LINEAGE", {row["code"] for row in result["failures"]})

        candidates = self._candidates()
        signal = self._signal(candidates[0])
        signal["trigger_signal_id"] = "TRIG-FORGED"
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=(signal,),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertIn("INVALID_TRIGGER_LINEAGE", {row["code"] for row in result["failures"]})

    def test_missing_or_inactive_current_issuer_fails_closed(self):
        candidates = self._candidates()
        candidates[-1]["universe_row"]["eligible"] = False
        candidates[-1]["universe_row"]["exclusion_reason"] = "DELISTED"
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertEqual(result["critical_counts"]["required_archetype_missing_count"], 1)

    def test_pre_deep_seal_is_idempotent_and_rejects_symlink_or_hardlink(self):
        candidates = self._candidates()
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
        )
        self.assertEqual(result["status"], SELECTION_PASS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selection.json"
            seal_cross_archetype_canary_selection(path, result)
            first = path.read_bytes()
            seal_cross_archetype_canary_selection(path, result)
            self.assertEqual(path.read_bytes(), first)
            changed = deepcopy(result)
            changed["selections"][0]["company_name"] = "사후변경회사"
            with self.assertRaisesRegex(ValueError, "different payload|exact accepted"):
                seal_cross_archetype_canary_selection(path, changed)

            external = root / "external.json"
            external.write_bytes(first)
            symlink = root / "symlink.json"
            symlink.symlink_to(external)
            with self.assertRaisesRegex(ValueError, "regular file|symlink"):
                seal_cross_archetype_canary_selection(symlink, result)

            hardlink = root / "hardlink.json"
            os.link(external, hardlink)
            with self.assertRaisesRegex(ValueError, "private regular file"):
                seal_cross_archetype_canary_selection(hardlink, result)

            dangling_parent = root / "dangling-parent"
            dangling_parent.symlink_to(root / "not-created", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                seal_cross_archetype_canary_selection(
                    dangling_parent / "selection.json", result
                )

    def test_seal_detects_same_bytes_inode_replacement_after_link(self):
        candidates = self._candidates()
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
        )
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "selection.json"
            encoded = (
                json.dumps(
                    result,
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                    allow_nan=False,
                )
                + "\n"
            ).encode("utf-8")
            original_unlink = os.unlink
            attacked = False

            def replace_after_temp_unlink(path, *args, **kwargs):
                nonlocal attacked
                outcome = original_unlink(path, *args, **kwargs)
                name = os.fspath(path)
                if not attacked and name.startswith(".selection.json."):
                    attacked = True
                    directory_fd = kwargs.get("dir_fd")
                    original_unlink(destination.name, dir_fd=directory_fd)
                    descriptor = os.open(
                        destination.name,
                        os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                        0o600,
                        dir_fd=directory_fd,
                    )
                    try:
                        os.write(descriptor, encoded)
                    finally:
                        os.close(descriptor)
                return outcome

            with patch(
                "e2r.production.v6_canary_selection.os.unlink",
                side_effect=replace_after_temp_unlink,
            ):
                with self.assertRaisesRegex(ValueError, "changed after atomic creation"):
                    seal_cross_archetype_canary_selection(destination, result)
            self.assertFalse(destination.exists())

    def test_seal_never_writes_through_a_parent_symlink_swap(self):
        candidates = self._candidates()
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "cutover"
            displaced = root / "cutover-original"
            victim = root / "outside"
            parent.mkdir()
            victim.mkdir()
            destination = parent / "selection.json"
            original_link = os.link
            attacked = False

            def swap_parent_before_link(*args, **kwargs):
                nonlocal attacked
                if not attacked:
                    attacked = True
                    parent.rename(displaced)
                    parent.symlink_to(victim, target_is_directory=True)
                return original_link(*args, **kwargs)

            with patch(
                "e2r.production.v6_canary_selection.os.link",
                side_effect=swap_parent_before_link,
            ):
                with self.assertRaisesRegex(ValueError, "parent changed"):
                    seal_cross_archetype_canary_selection(destination, result)

            self.assertFalse((victim / destination.name).exists())
            self.assertFalse((displaced / destination.name).exists())

    def test_phase105_cli_does_not_claim_the_phase106_result_summary_path(self):
        candidates = self._candidates()
        signals = self._signals(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
        )
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory).resolve()
            argv = [
                "select_e2r_v6_cross_archetype_canaries",
                "--as-of-date",
                self.AS_OF_DATE,
                "--repo-root",
                str(repo),
            ]
            with (
                patch.object(sys, "argv", argv),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "canonical_repository_root",
                    return_value=repo,
                ),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "_repository_identity_is_trusted",
                    return_value=True,
                ),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "load_current_live_selection_inputs",
                    return_value=(candidates, signals),
                ),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "compile_cross_archetype_canary_selection",
                    return_value=result,
                ),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "seal_cross_archetype_canary_selection"
                ) as seal,
                redirect_stdout(io.StringIO()) as stdout,
            ):
                self.assertEqual(selection_cli_main(), 0)
            seal.assert_called_once()
            self.assertEqual(
                Path(seal.call_args.args[0]).name,
                "cross_archetype_canary_selection.json",
            )
            output = json.loads(stdout.getvalue())
            self.assertNotIn("summary_path", output)

    def test_phase105_cli_exactly_binds_forced_profile_manifest(self):
        candidates = self._abstained_candidates()
        signals = self._signals(candidates)
        profile_manifest = self._forced_profile_manifest(candidates)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
            issuer_business_profile_manifest=profile_manifest,
        )
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory).resolve()
            profile_path = (
                repo / CUTOVER_RELATIVE_ROOT / ISSUER_PROFILE_MANIFEST_NAME
            )
            argv = [
                "select_e2r_v6_cross_archetype_canaries",
                "--as-of-date",
                self.AS_OF_DATE,
                "--repo-root",
                str(repo),
                "--issuer-profile-manifest",
                str(profile_path),
            ]
            with (
                patch.object(sys, "argv", argv),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "canonical_repository_root",
                    return_value=repo,
                ),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "_repository_identity_is_trusted",
                    return_value=True,
                ),
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "load_current_issuer_business_profile_manifest",
                    return_value=profile_manifest,
                ) as profile_loader,
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "load_current_live_selection_inputs",
                    return_value=(candidates, signals),
                ) as live_loader,
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "compile_cross_archetype_canary_selection",
                    return_value=result,
                ) as compiler,
                patch(
                    "e2r.cli.select_e2r_v6_cross_archetype_canaries."
                    "seal_cross_archetype_canary_selection"
                ) as seal,
                redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(selection_cli_main(), 0)
            profile_loader.assert_called_once_with(
                profile_path, selection_as_of_date=self.AS_OF_DATE
            )
            self.assertIs(
                live_loader.call_args.kwargs["issuer_business_profile_manifest"],
                profile_manifest,
            )
            self.assertIs(
                compiler.call_args.kwargs["issuer_business_profile_manifest"],
                profile_manifest,
            )
            self.assertIs(
                seal.call_args.kwargs["issuer_business_profile_manifest"],
                profile_manifest,
            )

    def test_selection_seal_rejects_whitespace_target_collision(self):
        candidates = self._candidates()
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=self._signals(candidates),
        )
        forged = deepcopy(result)
        forged["selections"][1]["target_id"] = (
            forged["selections"][0]["target_id"] + " "
        )
        forged["selection_roster_hash"] = stable_hash(forged["selections"])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "identity|canonical"):
                seal_cross_archetype_canary_selection(
                    Path(directory) / "selection.json", forged
                )

    def test_operational_loader_requires_full_audited_live_root(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ):
                candidates, signals = load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )
            self.assertEqual(len(candidates), 5)
            self.assertEqual(len(signals), 5)
            result = compile_cross_archetype_canary_selection(
                selection_as_of_date=self.AS_OF_DATE,
                candidates=candidates,
                trigger_events=signals,
            )
            self.assertEqual(result["status"], SELECTION_PASS)
            self.assertTrue(
                all(
                    row["selection_mode"] == NATURAL_SELECTION
                    for row in result["selections"]
                )
            )

    def test_profile_candidate_loader_uses_full_actual_shaped_audit_and_journal(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            candidates, _signals = self._write_live_root(root)
            self._rewrite_live_planners_as_abstained(root, omit_top_k=True)
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ):
                inputs = load_canonical_profile_inputs(
                    root, as_of_date=self.AS_OF_DATE
                )
            self.assertEqual(inputs.l3_target_count, len(candidates))
            self.assertEqual(inputs.natural_complete_count, 0)
            self.assertEqual(inputs.eligible_abstained_count, len(candidates))
            self.assertEqual(inputs.ineligible_abstained_count, 0)
            self.assertEqual(inputs.pending_count, 0)
            self.assertEqual(
                tuple(row["symbol"] for row in inputs.universe_rows),
                tuple(
                    candidate["universe_row"]["symbol"]
                    for candidate in candidates
                ),
            )
            full_krx_rows = [
                json.loads(line)
                for line in (root / "universe_eligible.jsonl").read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip()
            ]
            self.assertEqual(inputs.forced_discovery_rows, tuple(full_krx_rows))
            self.assertTrue(
                {row["symbol"] for row in inputs.universe_rows}.issubset(
                    {row["symbol"] for row in inputs.forced_discovery_rows}
                )
            )

            run_path = root / "planner_runs.jsonl"
            original_runs = run_path.read_bytes()
            runs = [json.loads(line) for line in original_runs.splitlines()]
            runs[0]["plan"]["final_score"] = 99
            run_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in runs),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "post-deep authority"):
                load_canonical_profile_inputs(root, as_of_date=self.AS_OF_DATE)
            run_path.write_bytes(original_runs)

            response_path = root / "llm_responses.jsonl"
            responses = [
                json.loads(line) for line in response_path.read_text().splitlines()
            ]
            responses[0]["response_hash"] = "0" * 64
            response_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in responses),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "response receipt hash"):
                load_canonical_profile_inputs(root, as_of_date=self.AS_OF_DATE)

    def test_complete_profile_materialization_seals_only_the_tracked_cutover_leaf(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory).resolve()
            live_root = (
                repo / "output" / "live_materialization" / self.AS_OF_DATE
            )
            live_root.mkdir(parents=True)
            candidates, _signals = self._write_live_root(live_root)
            self._rewrite_live_planners_as_abstained(
                live_root, omit_top_k=True
            )
            industries = dict(
                zip(
                    (
                        candidate["universe_row"]["symbol"]
                        for candidate in candidates
                    ),
                    ("26120", "20110", "20202", "21101", "62010"),
                    strict=True,
                )
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ):
                result, destination, inputs = materialize_canonical_profile_manifest(
                    repo_root=repo,
                    config=IssuerBusinessProfileConfig(
                        as_of_date=self.AS_OF_DATE,
                        max_profile_fetches=5,
                    ),
                    credential="official-fixture-key",
                    fetcher=FakeOpenDartFetcher(industries),
                    compatibility_provider=FakeCompatibilityProvider(),
                )
            self.assertEqual(result["status"], "COMPLETE")
            self.assertEqual(inputs.eligible_abstained_count, 5)
            self.assertEqual(
                destination,
                repo
                / CUTOVER_RELATIVE_ROOT
                / ISSUER_PROFILE_MANIFEST_NAME,
            )
            self.assertTrue(destination.is_file())
            self.assertFalse(
                (live_root / ISSUER_PROFILE_MANIFEST_NAME).exists()
            )
            loaded = load_current_issuer_business_profile_manifest(
                destination, selection_as_of_date=self.AS_OF_DATE
            )
            self.assertEqual(stable_hash(loaded), stable_hash(result))

    def test_operational_loader_admits_only_profile_bound_abstained_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            candidates, _signals = self._write_live_root(root)
            profile_manifest = self._forced_profile_manifest(candidates)
            profile_path = root / "issuer_business_profile.json"
            profile_path.write_text(
                json.dumps(profile_manifest, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            runs = [
                json.loads(line)
                for line in (root / "planner_runs.jsonl").read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip()
            ]
            for run in runs:
                run["terminal_status"] = "ABSTAINED"
                run["plan"]["status"] = "ABSTAINED"
                run["plan"]["critique_output"]["abstain"] = True
                critique_raw = json.dumps(
                    run["plan"]["critique_output"],
                    ensure_ascii=False,
                    sort_keys=True,
                )
                for trace in run["plan"]["provider_traces"]:
                    if trace["planner_pass"] == "MEMORY_CRITIQUE":
                        trace["response_hash"] = hashlib.sha256(
                            critique_raw.encode("utf-8")
                        ).hexdigest()
            (root / "planner_runs.jsonl").write_text(
                "".join(
                    json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                    for row in runs
                ),
                encoding="utf-8",
            )
            responses = [
                json.loads(line)
                for line in (root / "llm_responses.jsonl").read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip()
            ]
            run_by_target = {row["target_id"]: row for row in runs}
            for response in responses:
                if response["planner_pass"] != "MEMORY_CRITIQUE":
                    continue
                payload = run_by_target[response["target_id"]]["plan"][
                    "critique_output"
                ]
                raw_response = json.dumps(payload, ensure_ascii=False, sort_keys=True)
                response["response_payload"] = payload
                response["raw_response"] = raw_response
                response["response_hash"] = hashlib.sha256(
                    raw_response.encode("utf-8")
                ).hexdigest()
            (root / "llm_responses.jsonl").write_text(
                "".join(
                    json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                    for row in responses
                ),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ):
                loaded_profile = load_current_issuer_business_profile_manifest(
                    profile_path,
                    selection_as_of_date=self.AS_OF_DATE,
                )
                loaded_candidates, signals = load_current_live_selection_inputs(
                    root,
                    selection_as_of_date=self.AS_OF_DATE,
                    issuer_business_profile_manifest=loaded_profile,
                )
            self.assertEqual(len(loaded_candidates), 5)
            result = compile_cross_archetype_canary_selection(
                selection_as_of_date=self.AS_OF_DATE,
                candidates=loaded_candidates,
                trigger_events=signals,
                issuer_business_profile_manifest=loaded_profile,
            )
            self.assertEqual(result["status"], SELECTION_PASS)
            self.assertTrue(
                all(
                    row["selection_mode"] == FORCED_SELECTION
                    for row in result["selections"]
                )
            )

    def test_operational_loader_rejects_call_or_universe_tamper(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            response_path = root / "llm_responses.jsonl"
            responses = [
                json.loads(line)
                for line in response_path.read_text(encoding="utf-8").splitlines()
            ]
            responses[0]["response_hash"] = "0" * 64
            response_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in responses),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "response receipt hash"):
                load_current_live_selection_inputs(root, selection_as_of_date=self.AS_OF_DATE)

        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            universe_path = root / "universe_eligible.jsonl"
            rows = universe_path.read_text(encoding="utf-8").splitlines()[:999]
            universe_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            provenance_path = root / "universe_provenance.json"
            provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
            provenance["eligible_universe_hash"] = stable_hash(
                [json.loads(row) for row in rows]
            )
            provenance_path.write_text(
                json.dumps(provenance, sort_keys=True) + "\n", encoding="utf-8"
            )
            audit_path = root / "universe_audit.json"
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            audit["eligible_universe_count"] = 999
            audit_path.write_text(
                json.dumps(audit, sort_keys=True) + "\n", encoding="utf-8"
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "audit roster"):
                load_current_live_selection_inputs(root, selection_as_of_date=self.AS_OF_DATE)

    def test_operational_loader_rejects_future_signal_and_duplicate_trace(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            signal_path = root / "trigger_signals.jsonl"
            signals = [
                json.loads(line)
                for line in signal_path.read_text(encoding="utf-8").splitlines()
            ]
            signals[0]["effective_date"] = "2026-08-08"
            signals[0]["detected_at"] = "2026-08-08"
            signals[0]["trigger_signal_id"] = "TRIG-" + stable_hash(
                {
                    "target": signals[0]["target_id"],
                    "source_event": signals[0]["source_event_id"],
                    "effective_date": signals[0]["effective_date"],
                    "trigger_type": signals[0]["trigger_type"],
                    "lifecycle_status": signals[0]["lifecycle_status"],
                    "providers": tuple(signals[0]["provider_names"]),
                    "payload": signals[0]["payload"],
                }
            )[:24]
            signal_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in signals),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "future trigger"):
                load_current_live_selection_inputs(root, selection_as_of_date=self.AS_OF_DATE)

        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            runs_path = root / "planner_runs.jsonl"
            runs = [
                json.loads(line)
                for line in runs_path.read_text(encoding="utf-8").splitlines()
            ]
            runs[0]["plan"]["provider_traces"].append(
                deepcopy(runs[0]["plan"]["provider_traces"][0])
            )
            runs[0]["provider_call_count"] = 3
            runs_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in runs),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(
                ValueError, "call journal|exactly its two successful calls"
            ):
                load_current_live_selection_inputs(root, selection_as_of_date=self.AS_OF_DATE)

    def test_candidate_event_must_exactly_recompute_its_current_trigger_aggregate(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            event_path = root / "candidate_events.jsonl"
            events = [
                json.loads(line)
                for line in event_path.read_text(encoding="utf-8").splitlines()
            ]
            # The event ID does not include this summary field.  The selector
            # must still recompute it from the underlying trigger roster.
            events[0]["latest_effective_date"] = "2026-08-08"
            event_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in events),
                encoding="utf-8",
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ):
                candidates, signals = load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )
            result = compile_cross_archetype_canary_selection(
                selection_as_of_date=self.AS_OF_DATE,
                candidates=candidates,
                trigger_events=signals,
            )
            self.assertEqual(result["status"], SELECTION_FAIL)
            self.assertIn(
                "CANDIDATE_TRIGGER_ROSTER_MISMATCH",
                {row["code"] for row in result["failures"]},
            )

        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            signal_path = root / "trigger_signals.jsonl"
            signals = [
                json.loads(line)
                for line in signal_path.read_text(encoding="utf-8").splitlines()
            ]
            extra = deepcopy(signals[0])
            extra["source_event_id"] = "SOURCE-EVENT-EXTRA"
            extra["source_refs"] = ["SRC-EXTRA"]
            extra["trigger_signal_id"] = "TRIG-" + stable_hash(
                {
                    "target": extra["target_id"],
                    "source_event": extra["source_event_id"],
                    "effective_date": extra["effective_date"],
                    "trigger_type": extra["trigger_type"],
                    "lifecycle_status": extra["lifecycle_status"],
                    "providers": tuple(extra["provider_names"]),
                    "payload": extra["payload"],
                }
            )[:24]
            signals.append(extra)
            signal_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in signals),
                encoding="utf-8",
            )
            audit_path = root / "trigger_fusion_audit.json"
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            audit["trigger_signal_count"] = len(signals)
            audit_path.write_text(
                json.dumps(audit, sort_keys=True) + "\n", encoding="utf-8"
            )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ):
                candidates, loaded_signals = load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )
            result = compile_cross_archetype_canary_selection(
                selection_as_of_date=self.AS_OF_DATE,
                candidates=candidates,
                trigger_events=loaded_signals,
            )
            self.assertEqual(result["status"], SELECTION_FAIL)
            self.assertIn(
                "CANDIDATE_TRIGGER_ROSTER_MISMATCH",
                {row["code"] for row in result["failures"]},
            )

    def test_operational_loader_requires_canonical_exact_two_pass_call_receipts(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            for name in ("llm_prompts.jsonl", "llm_responses.jsonl"):
                path = root / name
                rows = [json.loads(line) for line in path.read_text().splitlines()]
                rows[0]["call_id"] = "LLMCALL-FORGED-EXTRA"
                path.write_text(
                    "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
                    encoding="utf-8",
                )
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "content does not recompute"):
                load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )

    def test_completed_target_rejects_an_extra_failed_call_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            prompt_path = root / "llm_prompts.jsonl"
            response_path = root / "llm_responses.jsonl"
            prompts = [json.loads(line) for line in prompt_path.read_text().splitlines()]
            responses = [
                json.loads(line) for line in response_path.read_text().splitlines()
            ]
            extra_prompt = deepcopy(prompts[0])
            extra_response = deepcopy(responses[0])
            extra_prompt["attempt_id"] = "provider-error"
            extra_prompt["prompt_text"] += " provider error"
            extra_prompt["prompt_hash"] = hashlib.sha256(
                extra_prompt["prompt_text"].encode()
            ).hexdigest()
            call_id = "LLMCALL-" + stable_hash(
                {
                    "target": extra_prompt["target_id"],
                    "attempt_id": extra_prompt["attempt_id"],
                    "planner_pass": extra_prompt["planner_pass"],
                    "prompt_hash": extra_prompt["prompt_hash"],
                }
            )[:24]
            extra_prompt["call_id"] = call_id
            extra_response.update(
                {
                    "call_id": call_id,
                    "attempt_id": "provider-error",
                    "status": "PROVIDER_ERROR",
                    "response_hash": "",
                    "raw_response": None,
                    "response_payload": None,
                    "error_category": "PROVIDER_ERROR",
                }
            )
            prompts.append(extra_prompt)
            responses.append(extra_response)
            prompt_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in prompts),
                encoding="utf-8",
            )
            response_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in responses),
                encoding="utf-8",
            )
            audit_path = root / "planner_validation.json"
            audit = json.loads(audit_path.read_text())
            audit["planner_call_count"] = len(responses)
            audit_path.write_text(json.dumps(audit, sort_keys=True) + "\n")
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(
                ValueError, "call journal|exactly its two successful calls"
            ):
                load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )

        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            prompt_path = root / "llm_prompts.jsonl"
            response_path = root / "llm_responses.jsonl"
            prompts = [json.loads(line) for line in prompt_path.read_text().splitlines()]
            responses = [
                json.loads(line) for line in response_path.read_text().splitlines()
            ]
            orphan_prompt = deepcopy(prompts[0])
            orphan_response = deepcopy(responses[0])
            orphan_prompt.update(
                {
                    "target_id": "999999",
                    "attempt_id": "orphan-error",
                    "prompt_text": "orphan provider error",
                }
            )
            orphan_prompt["prompt_hash"] = hashlib.sha256(
                orphan_prompt["prompt_text"].encode()
            ).hexdigest()
            orphan_call_id = "LLMCALL-" + stable_hash(
                {
                    "target": orphan_prompt["target_id"],
                    "attempt_id": orphan_prompt["attempt_id"],
                    "planner_pass": orphan_prompt["planner_pass"],
                    "prompt_hash": orphan_prompt["prompt_hash"],
                }
            )[:24]
            orphan_prompt["call_id"] = orphan_call_id
            orphan_response.update(
                {
                    "call_id": orphan_call_id,
                    "target_id": "999999",
                    "attempt_id": "orphan-error",
                    "status": "PROVIDER_ERROR",
                    "response_hash": "",
                    "raw_response": None,
                    "response_payload": None,
                    "error_category": "PROVIDER_ERROR",
                }
            )
            prompts.append(orphan_prompt)
            responses.append(orphan_response)
            prompt_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in prompts),
                encoding="utf-8",
            )
            response_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in responses),
                encoding="utf-8",
            )
            audit_path = root / "planner_validation.json"
            audit = json.loads(audit_path.read_text())
            audit["planner_call_count"] = len(responses)
            audit_path.write_text(json.dumps(audit, sort_keys=True) + "\n")
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "call journal"):
                load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )

        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            root = repo / "output" / "live_materialization" / self.AS_OF_DATE
            root.mkdir(parents=True)
            self._write_live_root(root)
            prompt_path = root / "llm_prompts.jsonl"
            response_path = root / "llm_responses.jsonl"
            run_path = root / "planner_runs.jsonl"
            prompts = [json.loads(line) for line in prompt_path.read_text().splitlines()]
            responses = [
                json.loads(line) for line in response_path.read_text().splitlines()
            ]
            runs = [json.loads(line) for line in run_path.read_text().splitlines()]
            extra_prompt = deepcopy(prompts[0])
            extra_response = deepcopy(responses[0])
            extra_prompt["attempt_id"] = "extra"
            extra_prompt["prompt_text"] += " extra"
            extra_prompt["prompt_hash"] = hashlib.sha256(
                extra_prompt["prompt_text"].encode()
            ).hexdigest()
            extra_call_id = "LLMCALL-" + stable_hash(
                {
                    "target": extra_prompt["target_id"],
                    "attempt_id": extra_prompt["attempt_id"],
                    "planner_pass": extra_prompt["planner_pass"],
                    "prompt_hash": extra_prompt["prompt_hash"],
                }
            )[:24]
            extra_prompt["call_id"] = extra_call_id
            extra_response["call_id"] = extra_call_id
            extra_response["attempt_id"] = "extra"
            prompts.append(extra_prompt)
            responses.append(extra_response)
            runs[0]["plan"]["provider_traces"].append(
                {
                    **deepcopy(runs[0]["plan"]["provider_traces"][0]),
                    "prompt_hash": extra_prompt["prompt_hash"],
                }
            )
            runs[0]["provider_call_count"] = 3
            prompt_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in prompts),
                encoding="utf-8",
            )
            response_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in responses),
                encoding="utf-8",
            )
            run_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in runs),
                encoding="utf-8",
            )
            audit_path = root / "planner_validation.json"
            audit = json.loads(audit_path.read_text())
            audit["planner_call_count"] = len(responses)
            audit_path.write_text(json.dumps(audit, sort_keys=True) + "\n")
            with patch(
                "e2r.production.v6_canary_selection.canonical_repository_root",
                return_value=repo,
            ), patch(
                "e2r.production.v6_canary_selection._repository_identity_is_trusted",
                return_value=True,
            ), self.assertRaisesRegex(ValueError, "exactly its two successful calls"):
                load_current_live_selection_inputs(
                    root, selection_as_of_date=self.AS_OF_DATE
                )

    def test_candidate_cannot_reference_a_missing_trigger_signal(self):
        candidates = self._candidates()
        signals = self._signals(candidates)
        signals.pop(0)
        result = compile_cross_archetype_canary_selection(
            selection_as_of_date=self.AS_OF_DATE,
            candidates=candidates,
            trigger_events=signals,
        )
        self.assertEqual(result["status"], SELECTION_FAIL)
        self.assertIn(
            "CANDIDATE_TRIGGER_ROSTER_MISMATCH",
            {row["code"] for row in result["failures"]},
        )


if __name__ == "__main__":
    unittest.main()
