"""Verifier-ready Initial Full Research prompt compiler for ResearchDossierV3."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from e2r.pro_first.ids import canonical_hash

from .loader import load_research_contract
from .question_planner import ResearchQuestionPlan, build_research_question_plan


INITIAL_PROMPT_V3_TEMPLATE = "e2r_pro_v3_initial_full_research.md"
RESEARCH_PACKET_V3_SCHEMA_VERSION = "e2r_pro_research_packet_v3"
RESEARCH_DOSSIER_V3_SCHEMA_VERSION = "e2r_pro_research_dossier_v3"
MAX_INITIAL_PROMPT_CHARS = 100_000

VERIFIER_PREFLIGHT_TRUE_FIELDS = (
    "source_opened",
    "canonical_url_used",
    "exact_excerpt_copied_from_source",
    "statement_not_broader_than_excerpt",
    "single_atomic_predicate",
    "target_subject_scope_confirmed",
    "publication_date_confirmed",
    "as_of_cutoff_pass",
    "lineage_duplicate_checked",
)
VERIFIER_PREFLIGHT_FALSE_FIELDS = (
    "derived_calculation_mixed_into_fact",
)


@dataclass(frozen=True)
class CompiledProResearchPromptV3:
    """Immutable Initial Prompt V3 plus its deterministic attachment receipt."""

    pass_name: str
    primary_archetype_ids: tuple[str, ...]
    contract_ids: tuple[str, ...]
    mandatory_question_ids: tuple[str, ...]
    prompt_text: str
    prompt_hash: str
    dossier_schema_hash: str

    def to_receipt(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_compiled_pro_research_prompt_v3",
            "pass_name": self.pass_name,
            "primary_archetype_ids": list(self.primary_archetype_ids),
            "contract_ids": list(self.contract_ids),
            "mandatory_question_ids": list(self.mandatory_question_ids),
            "mandatory_question_count": len(self.mandatory_question_ids),
            "prompt_hash": self.prompt_hash,
            "dossier_schema_hash": self.dossier_schema_hash,
            "prompt_char_count": len(self.prompt_text),
            "atomic_evidence_contract": True,
            "score_authority": False,
            "stage_authority": False,
        }


class ProResearchPromptCompilerV3:
    """Compile the common V3 contract for one-to-three primary archetypes."""

    def __init__(
        self,
        *,
        template_root: str | Path | None = None,
        dossier_schema_path: str | Path | None = None,
    ) -> None:
        repo_root = Path(__file__).resolve().parents[4]
        self.template_root = (
            Path(template_root).resolve()
            if template_root
            else repo_root / "configs/prompts"
        )
        self.dossier_schema_path = (
            Path(dossier_schema_path).resolve()
            if dossier_schema_path
            else repo_root / "configs/e2r_pro_research_dossier_v3.schema.json"
        )

    def compile(
        self,
        *,
        packet: Mapping[str, Any],
        primary_archetype_ids: Sequence[str],
        conversation_id: str | None = None,
        research_pass_id: str | None = None,
        parent_pass_id: str | None = None,
    ) -> CompiledProResearchPromptV3:
        """Compile an actual fresh-session Initial Full Research pass."""

        _validate_packet(packet)
        plan = build_research_question_plan(primary_archetype_ids)
        compiled_primary_ids = tuple(
            str(value) for value in primary_archetype_ids
        )
        selected = tuple(
            str(value) for value in packet.get("selected_archetypes") or ()
        )
        candidates = tuple(
            str(value) for value in packet.get("candidate_archetypes") or ()
        )
        if selected and compiled_primary_ids != selected:
            raise ValueError(
                "compiled primary contracts must exactly match packet selected_archetypes"
            )
        if not selected and not set(compiled_primary_ids).issubset(set(candidates)):
            raise ValueError("compiled primary contracts escape packet archetype roster")
        return self._compile_contracts(
            packet=packet,
            plan=plan,
            conversation_id=conversation_id,
            research_pass_id=research_pass_id,
            parent_pass_id=parent_pass_id,
        )

    def compile_contract_snapshot(
        self,
        *,
        packet: Mapping[str, Any],
        archetype_id: str,
    ) -> CompiledProResearchPromptV3:
        """Compile one of all 36 canonical contracts for the tracked CI audit.

        A primary snapshot is an actual one-primary job and therefore contains
        all four R13 cross guards.  A cross-guard snapshot is a unit audit only;
        live jobs never select a cross guard as a primary contract.
        """

        contract = load_research_contract(archetype_id)
        if contract["contract_role"] == "PRIMARY":
            return self.compile(
                packet=packet,
                primary_archetype_ids=(archetype_id,),
            )
        _validate_packet(packet, allow_cross_guard_snapshot=True)
        schema = self._load_dossier_schema()
        mandatory_ids = tuple(
            str(row["question_family_id"])
            for row in contract["question_families"]
            if row["mandatory_for_full_thesis"] is True
        )
        context = self._render_context(
            packet=packet,
            primary_contracts=(),
            cross_guard_contracts=(contract,),
            conversation_id=None,
            research_pass_id=None,
            parent_pass_id=None,
            dossier_schema=schema,
            contract_unit_snapshot=True,
        )
        prompt = self._bind_template(context)
        return CompiledProResearchPromptV3(
            pass_name="INITIAL_FULL_RESEARCH",
            primary_archetype_ids=(),
            contract_ids=(archetype_id,),
            mandatory_question_ids=mandatory_ids,
            prompt_text=prompt,
            prompt_hash=canonical_hash({"prompt": prompt}),
            dossier_schema_hash=canonical_hash(schema),
        )

    def _compile_contracts(
        self,
        *,
        packet: Mapping[str, Any],
        plan: ResearchQuestionPlan,
        conversation_id: str | None,
        research_pass_id: str | None,
        parent_pass_id: str | None,
    ) -> CompiledProResearchPromptV3:
        schema = self._load_dossier_schema()
        context = self._render_context(
            packet=packet,
            primary_contracts=plan.bundle.primary_contracts,
            cross_guard_contracts=plan.bundle.cross_guard_contracts,
            conversation_id=conversation_id,
            research_pass_id=research_pass_id,
            parent_pass_id=parent_pass_id,
            dossier_schema=schema,
            contract_unit_snapshot=False,
        )
        prompt = self._bind_template(context)
        return CompiledProResearchPromptV3(
            pass_name="INITIAL_FULL_RESEARCH",
            primary_archetype_ids=tuple(
                str(row["archetype_id"])
                for row in plan.bundle.primary_contracts
            ),
            contract_ids=plan.bundle.contract_ids,
            mandatory_question_ids=plan.mandatory_question_ids,
            prompt_text=prompt,
            prompt_hash=canonical_hash({"prompt": prompt}),
            dossier_schema_hash=canonical_hash(schema),
        )

    def _bind_template(self, context: str) -> str:
        template_path = self.template_root / INITIAL_PROMPT_V3_TEMPLATE
        template = template_path.read_text(encoding="utf-8")
        if template.count("{{COMPILED_CONTEXT}}") != 1:
            raise ValueError(f"prompt template requires one context slot: {template_path}")
        prompt = template.replace("{{COMPILED_CONTEXT}}", context).rstrip() + "\n"
        if re.search(r"\{\{[A-Z][A-Z0-9_]*\}\}", prompt):
            raise ValueError("compiled V3 prompt contains an unresolved template variable")
        if len(prompt) > MAX_INITIAL_PROMPT_CHARS:
            raise ValueError(
                "compiled V3 initial prompt exceeds the 100,000 character boundary"
            )
        return prompt

    def _load_dossier_schema(self) -> Mapping[str, Any]:
        schema = json.loads(self.dossier_schema_path.read_text(encoding="utf-8"))
        expected = schema.get("properties", {}).get("schema_version", {}).get("const")
        if expected != RESEARCH_DOSSIER_V3_SCHEMA_VERSION:
            raise ValueError("compiled output schema is not ResearchDossierV3")
        return schema

    def _render_context(
        self,
        *,
        packet: Mapping[str, Any],
        primary_contracts: Sequence[Mapping[str, Any]],
        cross_guard_contracts: Sequence[Mapping[str, Any]],
        conversation_id: str | None,
        research_pass_id: str | None,
        parent_pass_id: str | None,
        dossier_schema: Mapping[str, Any],
        contract_unit_snapshot: bool,
    ) -> str:
        target = packet["target"]
        target_id = target.get("target_id") or target.get("symbol")
        pass_id = research_pass_id or "TO_BE_BOUND_BY_ORCHESTRATOR"
        lines = [
            "## CompiledProResearchPromptV3 authority",
            "",
            "- prompt_contract_version: `v3`",
            "- pass_name: `INITIAL_FULL_RESEARCH`",
            f"- job_id: `{packet.get('job_id')}`",
            f"- run_id: `{packet.get('run_id')}`",
            f"- target: `{target_id} {target.get('company_name')}`",
            f"- as_of_date: `{packet.get('as_of_date')}`",
            f"- conversation_id: `{conversation_id or 'TO_BE_BOUND_BY_ORCHESTRATOR'}`",
            f"- research_pass_id: `{pass_id}`",
            f"- parent_pass_id: `{parent_pass_id or 'NONE'}`",
            f"- contract_unit_snapshot: `{str(contract_unit_snapshot).lower()}`",
            "- same_conversation_scope_required: `true`",
            "- output_schema: `e2r_pro_research_dossier_v3`",
            "- score_authority: `false`",
            "- stage_authority: `false`",
            "- future_source_allowed: `false`",
            "- investment_recommendation_allowed: `false`",
            "",
            f"최종 응답에는 `[[E2R_PRO_RUN_ID:{packet.get('run_id')}]]`, "
            f"`[[E2R_PRO_JOB_ID:{packet.get('job_id')}]]`, "
            f"`[[E2R_PRO_PASS_ID:{pass_id}]]`, "
            f"`[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id or 'NONE'}]]` marker를 각각 정확히 한 번 출력한다.",
            "",
            "packet의 roster 밖 archetype이 더 적합해 보여도 새 ID를 만들지 않는다. "
            "`ARCHETYPE_RESELECTION_REQUIRED`와 기존 registry ID 및 source-backed 근거만 반환한다.",
            "",
            "## 선택된 primary research contracts",
            "",
        ]
        if not primary_contracts:
            lines.extend(
                [
                    "이 파일은 R13 contract-unit CI snapshot이다. 실제 job에서는 1~3개 primary contract와 모든 R13 guard에 붙는다.",
                    "",
                ]
            )
        for contract in primary_contracts:
            lines.extend(_render_contract_v3(contract))
        lines.extend(["## 모든 실제 job에 적용되는 R13 cross guards", ""])
        for contract in cross_guard_contracts:
            lines.extend(_render_contract_v3(contract))
        packet_context = {
            "schema_version": packet.get("schema_version"),
            "job_id": packet.get("job_id"),
            "run_id": packet.get("run_id"),
            "target": packet.get("target"),
            "as_of_date": packet.get("as_of_date"),
            "research_mode": packet.get("research_mode"),
            "candidate_archetypes": packet.get("candidate_archetypes"),
            "selected_archetypes": packet.get("selected_archetypes"),
            "trigger_summary": packet.get("trigger_summary"),
            "business_snapshot": packet.get("business_snapshot"),
            "structured_financial_snapshot": packet.get(
                "structured_financial_snapshot"
            ),
            "revision_valuation_snapshot": packet.get(
                "revision_valuation_snapshot"
            ),
            "research_objectives": packet.get("research_objectives"),
            "source_preferences": packet.get("source_preferences"),
            "forbidden_inferences": packet.get("forbidden_inferences"),
            "fresh_blind_boundary": packet.get("fresh_blind_boundary"),
        }
        lines.extend(
            [
                "## 현재 ResearchPacketV3 context",
                "",
                "```json",
                json.dumps(packet_context, ensure_ascii=False, indent=2, sort_keys=True),
                "```",
                "",
                "이 packet은 연구 범위와 시작점일 뿐 정답, score 또는 Stage authority가 아니다.",
                "",
                "## ResearchDossierV3 exact output schema",
                "",
                "아래 JSON Schema를 정확히 만족하는 JSON을 "
                "`E2R_RESEARCH_DOSSIER_JSON_BEGIN`과 "
                "`E2R_RESEARCH_DOSSIER_JSON_END` 사이에 정확히 하나 출력한다.",
                "",
                "```json",
                # Preserve the complete exact schema while avoiding almost
                # 10k characters of non-semantic indentation.  The schema
                # hash and every key/value remain unchanged.
                json.dumps(
                    dossier_schema,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                "```",
                "",
                "schema의 `verifier_preflight`에서 다음 9개 필드는 모두 true여야 한다: "
                + ", ".join(f"`{value}`" for value in VERIFIER_PREFLIGHT_TRUE_FIELDS)
                + ".",
                "`derived_calculation_mixed_into_fact`는 false여야 한다.",
                "DerivedMetricV3는 `input_fact_ids`와 `formula`로 계산 계보를 분리하며 quoted atomic fact에 계산 결과를 섞지 않는다.",
                "검증을 통과하지 못한 candidate는 accepted fact로 강행하지 말고 unresolved gap에 남긴다.",
            ]
        )
        return "\n".join(lines)


def _render_contract_v3(contract: Mapping[str, Any]) -> list[str]:
    lines = [
        f"### `{contract['archetype_id']}`",
        "",
        f"- contract_role: `{contract['contract_role']}`",
        f"- economic_mechanism: {contract['economic_mechanism']}",
        "- required_bridge_axes: "
        + (", ".join(contract["required_bridge_axes"]) or "GUARD_ONLY"),
        "- source_role_policy: `"
        + json.dumps(
            contract["source_role_policy"],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "`",
        "- false_positive_guards: "
        + json.dumps(contract["false_positive_guards"], ensure_ascii=False),
        "- score_authority: `false`",
        "- stage_authority: `false`",
        "",
        "Mandatory question families:",
        "",
    ]
    for index, question in enumerate(contract["question_families"], 1):
        adequate = question["adequate_search_requirements"]
        lines.extend(
            [
                f"{index}. `{question['question_family_id']}` — {question['question_text']}",
                "   - mandatory_for_full_thesis: `"
                + str(question["mandatory_for_full_thesis"]).lower()
                + "`",
                f"   - question_roles: {', '.join(question['question_roles'])}",
                "   - required_primitives: "
                + (", ".join(question["required_primitives"]) or "DIRECT_PREDICATE"),
                "   - required_source_roles: "
                + ", ".join(question["required_source_roles"]),
                "   - preferred_source_families: "
                + ", ".join(question["preferred_source_families"]),
                "   - affected_component_ids: "
                + (", ".join(question["affected_component_ids"]) or "GUARD_ONLY"),
                "   - allowed_terminal_statuses: "
                + ", ".join(question["allowed_terminal_statuses"]),
                "   - adequate_search: official-first=`"
                + str(adequate["official_route_attempt_required"]).lower()
                + "`, minimum_distinct_source_routes=`"
                + str(adequate["minimum_distinct_source_routes"])
                + "`, independent_no_new_route_confirmations=`"
                + str(
                    adequate[
                        "independent_no_new_route_confirmations_for_absence"
                    ]
                )
                + "`",
                "   - false_positive_guards: "
                + json.dumps(question["false_positive_guards"], ensure_ascii=False),
            ]
        )
    lines.append("")
    return lines


def _validate_packet(
    packet: Mapping[str, Any],
    *,
    allow_cross_guard_snapshot: bool = False,
) -> None:
    _assert_blind_safe(packet)
    if packet.get("schema_version") != RESEARCH_PACKET_V3_SCHEMA_VERSION:
        raise ValueError("Initial Prompt V3 requires ResearchPacketV3")
    target = packet.get("target") or {}
    if not isinstance(target, Mapping):
        raise ValueError("ResearchPacketV3 target must be an object")
    target_id = str(target.get("target_id") or target.get("symbol") or "")
    company_name = str(target.get("company_name") or "")
    job_id = str(packet.get("job_id") or "")
    run_id = str(packet.get("run_id") or "")
    as_of_date = str(packet.get("as_of_date") or "")
    if not target_id or not company_name or not job_id or not run_id or not as_of_date:
        raise ValueError(
            "compiled V3 prompt requires job/run/target/company/as_of_date"
        )
    try:
        date.fromisoformat(as_of_date)
    except ValueError as exc:
        raise ValueError("ResearchPacketV3 as_of_date must be an ISO date") from exc
    candidates = tuple(packet.get("candidate_archetypes") or ())
    selected = tuple(packet.get("selected_archetypes") or ())
    if not allow_cross_guard_snapshot and not (candidates or selected):
        raise ValueError("ResearchPacketV3 requires an archetype roster")
    for label, roster in (
        ("candidate_archetypes", candidates),
        ("selected_archetypes", selected),
    ):
        if roster and not 1 <= len(roster) <= 3:
            raise ValueError(f"ResearchPacketV3 {label} requires one to three IDs")
        if len(roster) != len(set(str(value) for value in roster)):
            raise ValueError(f"ResearchPacketV3 {label} contains duplicate IDs")


def _assert_blind_safe(value: Any, path: tuple[str, ...] = ()) -> None:
    forbidden = {
        "expected_score",
        "expected_stage",
        "gold_score",
        "gold_stage",
        "gold_answer",
        "future_outcome",
        "forward_return",
        "mfe",
        "mae",
    }
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).casefold().replace("-", "_")
            if normalized in forbidden:
                location = "/".join((*path, str(key)))
                raise ValueError(f"forbidden answer field in V3 prompt input: {location}")
            _assert_blind_safe(child, (*path, str(key)))
    elif isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        for index, child in enumerate(value):
            _assert_blind_safe(child, (*path, str(index)))


__all__ = [
    "CompiledProResearchPromptV3",
    "INITIAL_PROMPT_V3_TEMPLATE",
    "MAX_INITIAL_PROMPT_CHARS",
    "ProResearchPromptCompilerV3",
    "RESEARCH_PACKET_V3_SCHEMA_VERSION",
    "VERIFIER_PREFLIGHT_FALSE_FIELDS",
    "VERIFIER_PREFLIGHT_TRUE_FIELDS",
]
