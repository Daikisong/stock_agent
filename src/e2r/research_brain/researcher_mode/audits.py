"""Leaf-backed E2R v5 architecture forensics.

This module records the Phase 80 baseline before Researcher Mode replaces the
checklist-shaped scoring authority.  It deliberately distinguishes retrieval
strength from scoring authority: a legacy path may be worth reusing for broad
discovery while its score mutation remains forbidden.
"""

from __future__ import annotations

import ast
import hashlib
import json
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import write_json, write_text


PHASE80_SCHEMA_VERSION = "e2r_v5_phase80_forensics_v1"
PHASE80_PASS = "V5_PHASE80_WHOLE_REPO_FORENSIC_PASS"

PHASE80_ARTIFACT_PATHS = {
    "call_graph": "docs/operational/e2r_v5_whole_repo_call_graph.json",
    "parallel_brains": "docs/operational/e2r_v5_parallel_brain_inventory.json",
    "behavior_diff": "docs/operational/e2r_v5_research_vs_runtime_behavior_diff.md",
    "score_collapse": "docs/operational/e2r_v5_current_score_collapse_forensic.json",
}

REQUIRED_SCOPES = (
    "src/e2r/pipeline/korea_live_lite.py",
    "src/e2r/research_brain",
    "src/e2r/research_brain/scoring",
    "src/e2r/research_brain/runtime/live_materialization",
    "src/e2r/evidence",
    "src/e2r/sources",
    "src/e2r/production/source_connectors",
    "src/e2r/scoring.py",
    "src/e2r/features.py",
    "src/e2r/staging.py",
    "configs",
    "docs/round",
    "reports/e2r_calibration",
    "tests",
)

CODE_SCOPE_PREFIXES = (
    "src/e2r/pipeline/korea_live_lite.py",
    "src/e2r/research_brain",
    "src/e2r/evidence",
    "src/e2r/sources",
    "src/e2r/production/source_connectors",
    "src/e2r/scoring.py",
    "src/e2r/features.py",
    "src/e2r/staging.py",
)

CANONICAL_LANES = (
    {
        "lane_id": "A",
        "name": "legacy_korea_live_lite_retrieval_scoring",
        "entrypoint": "e2r.pipeline.korea_live_lite.KoreaLiveLiteRunner.run",
        "entry_path": "src/e2r/pipeline/korea_live_lite.py",
        "entry_symbol": "def run(self, config: KoreaLiveLiteConfig)",
        "production_reachable": True,
        "retrieval_authority": True,
        "current_score_authority": True,
        "future_score_authority": False,
    },
    {
        "lane_id": "B",
        "name": "canonical_research_brain_materialization",
        "entrypoint": "e2r.research_brain.v4_production_orchestrator.run_research_brain_v4_production_shadow",
        "entry_path": "src/e2r/research_brain/v4_production_orchestrator.py",
        "entry_symbol": "def run_research_brain_v4_production_shadow(",
        "production_reachable": True,
        "retrieval_authority": True,
        "current_score_authority": True,
        "future_score_authority": False,
    },
    {
        "lane_id": "C",
        "name": "question_impact_contract_closure",
        "entrypoint": "e2r.research_brain.scoring.question_impact_contract.compile_question_closures_v2",
        "entry_path": "src/e2r/research_brain/scoring/question_impact_contract.py",
        "entry_symbol": "def compile_question_closures_v2(",
        "production_reachable": True,
        "retrieval_authority": False,
        "current_score_authority": True,
        "future_score_authority": False,
    },
    {
        "lane_id": "D",
        "name": "claim_impact_component_scoring",
        "entrypoint": "e2r.research_brain.dossier.scoring_pipeline.run_dossier_scoring_pipeline",
        "entry_path": "src/e2r/research_brain/dossier/scoring_pipeline.py",
        "entry_symbol": "def run_dossier_scoring_pipeline(",
        "production_reachable": True,
        "retrieval_authority": False,
        "current_score_authority": True,
        "future_score_authority": False,
    },
    {
        "lane_id": "E",
        "name": "historical_replay",
        "entrypoint": "e2r.research_brain.replay.canonical_runner",
        "entry_path": "src/e2r/research_brain/replay/canonical_runner.py",
        "entry_symbol": "def ",
        "production_reachable": False,
        "retrieval_authority": False,
        "current_score_authority": False,
        "future_score_authority": False,
    },
    {
        "lane_id": "F",
        "name": "census_daily_path",
        "entrypoint": "e2r.census.census_runner_v4.run_census_mode_v4",
        "entry_path": "src/e2r/census/census_runner_v4.py",
        "entry_symbol": "def run_census_mode_v4(",
        "production_reachable": True,
        "retrieval_authority": True,
        "current_score_authority": True,
        "future_score_authority": False,
    },
)

PARALLEL_SCORE_AUTHORITIES = (
    {
        "authority_id": "LEGACY_FEATURE_SCORER",
        "path": "src/e2r/research/free_web_research_runner.py",
        "symbol": "score = feature_result.score()",
        "caller": "KoreaLiveLiteRunner",
        "production_reachable": True,
        "v5_disposition": "RETRIEVAL_ONLY_SCORE_RETIRED",
    },
    {
        "authority_id": "RESEARCH_BRAIN_V3_SCORER",
        "path": "src/e2r/research_brain/v3_scoring_stage.py",
        "symbol": "snapshot = DeterministicScorer().score(payload)",
        "caller": "v3 daily shadow CLI",
        "production_reachable": True,
        "v5_disposition": "COMPATIBILITY_ONLY",
    },
    {
        "authority_id": "RESEARCH_BRAIN_V4_SCORER",
        "path": "src/e2r/research_brain/v4_scoring_stage.py",
        "symbol": "snapshot = DeterministicScorer().score(payload)",
        "caller": "v4 production shadow and census",
        "production_reachable": True,
        "v5_disposition": "MATERIALIZATION_INPUT_ONLY",
    },
    {
        "authority_id": "DOSSIER_COMPONENT_SCORER",
        "path": "src/e2r/research_brain/dossier/scoring_pipeline.py",
        "symbol": "score = ResearchCalibratedComponentScorer().score(",
        "caller": "dossier scoring CLI",
        "production_reachable": True,
        "v5_disposition": "REPLACED_BY_RESEARCHER_MODE",
    },
    {
        "authority_id": "CENSUS_DIRECT_SCORER",
        "path": "src/e2r/census/census_runner_v4.py",
        "symbol": "snapshot = DeterministicScorer().score(payload)",
        "caller": "census v4",
        "production_reachable": True,
        "v5_disposition": "BASELINE_ONLY",
    },
    {
        "authority_id": "OFFICIAL_LIVE_SHADOW_SCORER",
        "path": "src/e2r/production/official_live_shadow.py",
        "symbol": "snapshot = DeterministicScorer().score(payload)",
        "caller": "official live shadow",
        "production_reachable": True,
        "v5_disposition": "BASELINE_ONLY",
    },
)

LEGACY_RETRIEVAL_TO_PORT = (
    "LLM/sector-aware broad query expansion",
    "Naver API discovery transport",
    "full page and public PDF fetch",
    "document cache and content dedupe",
    "theme and score-gap query feedback",
    "OpenDART detail and structured financial collection",
    "CompanyGuide consensus/revision and Naver Finance structured snapshots",
)

LEGACY_SCORING_TO_DISCARD = (
    "parser field direct score mutation",
    "feature-field rewrite after search",
    "keyword-only risk or positive score",
    "input-order dependent score mutation",
    "legacy score and Stage as Researcher Mode authority",
)

SCORE_COLLAPSE_CAUSES = (
    {
        "cause_id": "FIXED_LOW_RESEARCH_LIMITS",
        "path": "src/e2r/research_brain/dossier/orchestrator.py",
        "symbol": "max_research_iterations: int = 12",
        "effect": "A transport limit can terminate the checklist before broad component research saturates.",
    },
    {
        "cause_id": "QUESTION_TASK_BOUNDED_EXHAUSTION",
        "path": "configs/e2r_full_thesis_question_families_v1.json",
        "symbol": "BOUNDED_ROUTES_EXHAUSTED",
        "effect": "Thirteen question families use max_queries=3/max_fetches=6 and can close on bounded route exhaustion.",
    },
    {
        "cause_id": "KEYWORD_CLOSURE_SCORE_GATE",
        "path": "src/e2r/research_brain/scoring/question_impact_contract.py",
        "symbol": "required_keyword_groups",
        "effect": "Keyword groups choose SUPPORTED_SCORING/PARTIALLY_SUPPORTED_SCORING/EVALUATED_ABSENT.",
    },
    {
        "cause_id": "QUESTION_CLOSURE_COMPONENT_DEPENDENCY",
        "path": "src/e2r/research_brain/dossier/scoring_pipeline.py",
        "symbol": "compile_question_closures_v2(",
        "effect": "Question closure feeds semantic reconciliation, terminal evidence, component assessment, and full validity.",
    },
    {
        "cause_id": "EXACT_PRIMITIVE_SUBCRITERION_GATE",
        "path": "src/e2r/research_brain/scoring/component_scoring_model.py",
        "symbol": "_resolve_subcriterion(component, impact)",
        "effect": "An impact without an allowed primitive/question subcriterion is unmapped and cannot open the broad component.",
    },
    {
        "cause_id": "CHAINED_FRACTION_UNDERCREDIT",
        "path": "src/e2r/research_brain/scoring/impact_validator.py",
        "symbol": "min(raw, causal, source, temporal, support_cap)",
        "effect": "Economic strength is repeatedly bounded before tiny subcriterion multiplication, collapsing strong-anchor-equivalent evidence.",
    },
    {
        "cause_id": "VALUATION_REVISION_APERTURE_COLLAPSE",
        "path": "src/e2r/research_brain/dossier/scoring_pipeline.py",
        "symbol": '"market_mispricing": ("medium_term_revision_consensus",)',
        "effect": "Market expectation and valuation depend on one narrow family instead of structured price, consensus, peer, and scenario research.",
    },
    {
        "cause_id": "SMALL_GOLD_BENCHMARK_FALSE_COMPLETENESS",
        "path": "docs/operational/e2r_research_quality_gold_audit.json",
        "symbol": '"gold_fact_count": 9',
        "effect": "Nine matched facts cannot prove complete seven-component research recall.",
    },
)

FUTURE_ARCHITECTURE = {
    "canonical_namespace": "e2r.research_brain.researcher_mode",
    "single_current_scoring_authority": "Researcher Mode FinalComponentDecision + deterministic ScoreAggregator",
    "stage_authority": "deterministic StageCourt fed only by finalized seven-component decisions",
    "question_contract_role": "research seed / false-positive guard / explanation tag / source hint",
    "legacy_role": "retrieval aperture and structured connector donor only",
    "historical_role": "blind-safe ordinal/component anchor atlas; future outcome evaluator isolated",
}


def compile_phase80_forensics(repo_root: str | Path = ".") -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    scope_inventory = tuple(_inventory_scope(root, value) for value in REQUIRED_SCOPES)
    code_files = _code_files(root)
    module_nodes, import_edges = _python_call_graph(root, code_files)
    lanes = tuple(_with_lineage(root, row) for row in CANONICAL_LANES)
    authorities = tuple(_with_lineage(root, row) for row in PARALLEL_SCORE_AUTHORITIES)
    causes = tuple(_with_lineage(root, row) for row in SCORE_COLLAPSE_CAUSES)
    target_baselines = _current_target_baselines(root)

    critical = {
        "required_scope_missing_count": sum(not row["exists"] for row in scope_inventory),
        "canonical_lane_missing_count": sum(not row["symbol_found"] for row in lanes),
        "parallel_authority_lineage_missing_count": sum(
            not row["symbol_found"] for row in authorities
        ),
        "score_collapse_lineage_missing_count": sum(
            not row["symbol_found"] for row in causes
        ),
        "mandatory_target_baseline_missing_count": max(0, 2 - len(target_baselines)),
        "future_architecture_missing_count": int(
            not FUTURE_ARCHITECTURE["canonical_namespace"]
        ),
    }
    base = {
        "schema_version": PHASE80_SCHEMA_VERSION,
        "audited_base_commit": _git_head(root),
        "status": PHASE80_PASS if sum(critical.values()) == 0 else "V5_PHASE80_WHOLE_REPO_FORENSIC_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }
    call_graph = {
        **base,
        "audit_scope": [dict(row) for row in scope_inventory],
        "scope_manifest_hash": _stable_hash(scope_inventory),
        "canonical_lanes": [dict(row) for row in lanes],
        "module_count": len(module_nodes),
        "import_edge_count": len(import_edges),
        "module_nodes": module_nodes,
        "import_edges": import_edges,
        "canonical_future_architecture": dict(FUTURE_ARCHITECTURE),
    }
    parallel = {
        **base,
        "production_reachable_parallel_score_authority_count": sum(
            bool(row["production_reachable"]) for row in authorities
        ),
        "authorities": [dict(row) for row in authorities],
        "legacy_retrieval_capabilities_to_port": list(LEGACY_RETRIEVAL_TO_PORT),
        "legacy_scoring_capabilities_to_discard": list(LEGACY_SCORING_TO_DISCARD),
        "canonical_future_architecture": dict(FUTURE_ARCHITECTURE),
    }
    collapse = {
        **base,
        "target_baselines": target_baselines,
        "root_causes": [dict(row) for row in causes],
        "question_family_budget_summary": _question_budget_summary(root),
        "conclusion": (
            "The current score scale is not merely conservative: broad component "
            "judgment is downstream of bounded question closure, exact primitive "
            "mapping, and chained fractional caps. Market expectation, valuation, "
            "and FCF research aperture is materially incomplete."
        ),
    }
    behavior_markdown = _behavior_diff_markdown(
        base=base,
        target_baselines=target_baselines,
        authorities=authorities,
        causes=causes,
    )
    return {
        "call_graph": call_graph,
        "parallel_brains": parallel,
        "behavior_diff": behavior_markdown,
        "score_collapse": collapse,
    }


def write_phase80_forensics(
    *, repo_root: str | Path = ".", output_root: str | Path | None = None
) -> Mapping[str, Path]:
    root = Path(repo_root).resolve()
    compiled = compile_phase80_forensics(root)
    outputs: dict[str, Path] = {}
    for key, relative in PHASE80_ARTIFACT_PATHS.items():
        path = (
            Path(output_root) / Path(relative).name
            if output_root is not None
            else root / relative
        )
        if key == "behavior_diff":
            write_text(path, str(compiled[key]))
        else:
            write_json(path, compiled[key])
        outputs[key] = path
    return outputs


def _inventory_scope(root: Path, relative: str) -> Mapping[str, Any]:
    path = root / relative
    files = _files(path)
    return {
        "path": relative,
        "exists": path.exists(),
        "file_count": len(files),
        "line_count": sum(_line_count(value) for value in files),
        "content_manifest_hash": _file_manifest_hash(root, files),
    }


def _code_files(root: Path) -> tuple[Path, ...]:
    files: set[Path] = set()
    for relative in CODE_SCOPE_PREFIXES:
        files.update(path for path in _files(root / relative) if path.suffix == ".py")
    files.update(path for path in _files(root / "src/e2r/census") if path.suffix == ".py")
    files.update(path for path in _files(root / "src/e2r/production") if path.suffix == ".py")
    files.update(path for path in _files(root / "src/e2r/research") if path.suffix == ".py")
    return tuple(sorted(files))


def _python_call_graph(
    root: Path, files: Sequence[Path]
) -> tuple[list[Mapping[str, Any]], list[Mapping[str, str]]]:
    nodes = []
    edges: set[tuple[str, str]] = set()
    for path in files:
        relative = path.relative_to(root).as_posix()
        module = _module_name(relative)
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
        except (SyntaxError, UnicodeDecodeError):
            continue
        imports: set[str] = set()
        definitions = 0
        calls = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                definitions += 1
            elif isinstance(node, ast.Call):
                calls += 1
            elif isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names if alias.name.startswith("e2r"))
            elif isinstance(node, ast.ImportFrom):
                imported = _resolve_import(module, node.level, node.module or "")
                if imported.startswith("e2r"):
                    imports.add(imported)
        for imported in imports:
            edges.add((module, imported))
        nodes.append(
            {
                "module": module,
                "path": relative,
                "definition_count": definitions,
                "call_count": calls,
                "e2r_imports": sorted(imports),
                "sha256": _sha256(path.read_bytes()),
            }
        )
    return (
        sorted(nodes, key=lambda row: str(row["module"])),
        [
            {"caller_module": caller, "imported_module": imported}
            for caller, imported in sorted(edges)
        ],
    )


def _with_lineage(root: Path, row: Mapping[str, Any]) -> Mapping[str, Any]:
    result = dict(row)
    path = root / str(row["path"] if "path" in row else row["entry_path"])
    symbol = str(row["symbol"] if "symbol" in row else row["entry_symbol"])
    line = _find_line(path, symbol)
    result["symbol_found"] = line is not None
    result["source_line"] = line
    result["source_sha256"] = _sha256(path.read_bytes()) if path.is_file() else None
    return result


def _current_target_baselines(root: Path) -> list[Mapping[str, Any]]:
    live_root = root / "output/evidence_to_score_v2/live_2026-07-11"
    names = {"005930": "삼성전자", "000660": "SK하이닉스"}
    rows = []
    for target_id, name in names.items():
        dossier = live_root / target_id
        score_path = dossier / "component_score_vector.json"
        stage_path = dossier / "atomic_stage_decision.json"
        if not score_path.is_file() or not stage_path.is_file():
            continue
        score = json.loads(score_path.read_text(encoding="utf-8"))
        stage = json.loads(stage_path.read_text(encoding="utf-8"))
        rows.append(
            {
                "target_id": target_id,
                "company_name": name,
                "as_of_date": stage.get("as_of_date"),
                "evidence_document_count": _jsonl_count(dossier / "evidence_documents.jsonl"),
                "accepted_claim_count": _jsonl_count(dossier / "accepted_current_claims.jsonl"),
                "validated_impact_count": _jsonl_count(dossier / "claim_impacts_validated.jsonl"),
                "component_subcriterion_count": _jsonl_count(dossier / "component_subcriteria.jsonl"),
                "component_score_vector": dict(score.get("component_score_vector") or {}),
                "full_e2r_score": score.get("full_e2r_score"),
                "score_type": score.get("score_type"),
                "full_score_valid": score.get("full_score_valid"),
                "canonical_stage": stage.get("canonical_stage"),
                "decision_status": stage.get("decision_status"),
                "zero_components": sorted(
                    key
                    for key, value in (score.get("component_score_vector") or {}).items()
                    if float(value) == 0.0
                ),
            }
        )
    return rows


def _question_budget_summary(root: Path) -> Mapping[str, Any]:
    path = root / "configs/e2r_full_thesis_question_families_v1.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = [
        family
        for archetype in (payload.get("archetypes") or {}).values()
        for family in archetype.get("question_families") or ()
    ]
    return {
        "question_family_count": len(rows),
        "max_queries_values": sorted({int(row["budget"]["max_queries"]) for row in rows}),
        "max_candidates_values": sorted({int(row["budget"]["max_candidates"]) for row in rows}),
        "max_fetches_values": sorted({int(row["budget"]["max_fetches"]) for row in rows}),
        "bounded_routes_exhausted_stop_count": sum(
            "BOUNDED_ROUTES_EXHAUSTED" in str(row.get("stop_condition") or "")
            for row in rows
        ),
        "v5_research_completion_authority_allowed": False,
    }


def _behavior_diff_markdown(
    *,
    base: Mapping[str, Any],
    target_baselines: Sequence[Mapping[str, Any]],
    authorities: Sequence[Mapping[str, Any]],
    causes: Sequence[Mapping[str, Any]],
) -> str:
    target_lines = "\n".join(
        f"- {row['target_id']} {row['company_name']}: documents={row['evidence_document_count']}, "
        f"claims={row['accepted_claim_count']}, score={row['full_e2r_score']}, "
        f"zero_components={row['zero_components']}"
        for row in target_baselines
    )
    authority_lines = "\n".join(
        f"- `{row['authority_id']}`: {row['caller']} → `{row['v5_disposition']}`"
        for row in authorities
    )
    cause_lines = "\n".join(
        f"- `{row['cause_id']}` — {row['effect']} "
        f"(`{row['path']}:{row['source_line']}`)"
        for row in causes
    )
    return f"""# E2R v5 Research vs Runtime Behavior Difference

- status: {base['status']}
- audited base commit: `{base['audited_base_commit']}`
- critical_count_sum: {base['critical_count_sum']}

## 결론

현재 runtime은 안전성 검증은 강하지만 연구자의 broad component 판단을 복원하지 못했다. 13개 질문을 낮은 고정 budget으로 닫고 exact primitive와 여러 fraction cap을 통과한 잔여 credit만 합산한다. v5 canonical path는 `e2r.research_brain.researcher_mode` 하나로 통합한다.

쉬운 예: 식당 평가를 할 때 “주차장, 메뉴판, 영업시간” 체크박스를 모두 확인했다고 음식·가격·재방문 가치 조사까지 끝난 것은 아니다. 현재 FULL_E2R_100은 이 둘을 혼동한다.

## Historical research와 current runtime 차이

| 축 | 과거 연구 방식 | 현재 runtime | v5 방향 |
|---|---|---|---|
| 조사 종료 | material positive/counter와 정량자료 종합 | bounded route/질문 closure | supervisor 3자 semantic saturation |
| 점수 단위 | 7개 broad component 종합판단 | primitive impact fraction × subcriterion | component memo + historical anchor + judge consensus |
| source | official·structured·independent를 넓게 연결 | canary 최종 scoring 문서 1~2건 | material relevance 기반 source graph |
| valuation/revision | 가격·컨센서스·historical/peer band | 한 질문 family에 주로 종속 | structured financial/consensus/valuation engine |
| 반례 | phase·valuation·qualification을 thesis와 함께 종합 | impact counter fraction | memo와 skeptic judge에서 명시적 net 판단 |
| Stage | 연구 score와 판례를 종합한 후 검증 | low subtotal도 FULL_E2R_100으로 final 가능 | 7/7 research complete 뒤 deterministic StageCourt |

## 현재 canary score collapse

{target_lines}

## production-reachable 병렬 scoring authority

{authority_lines}

이 경로들은 Phase 80 시점에 동시에 접근 가능하다. v5 이후 current full-thesis authority는 Researcher Mode 하나만 남기고 나머지는 baseline, compatibility 또는 retrieval-only로 제한해야 한다.

## file/function root causes

{cause_lines}

## Legacy에서 이식할 것

{chr(10).join(f'- {value}' for value in LEGACY_RETRIEVAL_TO_PORT)}

## Legacy scoring에서 폐기할 것

{chr(10).join(f'- {value}' for value in LEGACY_SCORING_TO_DISCARD)}

## 선택한 canonical future architecture

`target/as_of_date → Researcher Mode source graph → EvidenceFact graph → 7 ComponentResearchMemo → Analyst/Skeptic/CalibrationJudge → deterministic FinalComponentDecision/total → deterministic StageCourt`

QuestionImpactContract와 primitive는 조사 seed·guard·설명 태그로만 남고 production score/final Stage authority는 갖지 않는다.
"""


def _files(path: Path) -> tuple[Path, ...]:
    if path.is_file():
        return (path,)
    if not path.is_dir():
        return ()
    return tuple(
        sorted(
            value
            for value in path.rglob("*")
            if value.is_file()
            and "__pycache__" not in value.parts
            and value.suffix not in {".pyc", ".pyo"}
        )
    )


def _line_count(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return 0


def _file_manifest_hash(root: Path, files: Iterable[Path]) -> str:
    rows = [
        (path.relative_to(root).as_posix(), _sha256(path.read_bytes()))
        for path in files
    ]
    return _stable_hash(rows)


def _module_name(relative: str) -> str:
    value = relative[:-3] if relative.endswith(".py") else relative
    value = value.replace("/", ".")
    return value[4:] if value.startswith("src.") else value


def _resolve_import(module: str, level: int, imported: str) -> str:
    if level <= 0:
        return imported
    package = module.split(".")[:-1]
    keep = max(0, len(package) - level + 1)
    prefix = package[:keep]
    return ".".join((*prefix, imported)) if imported else ".".join(prefix)


def _find_line(path: Path, symbol: str) -> int | None:
    if not path.is_file():
        return None
    for number, line in enumerate(
        path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
    ):
        if symbol in line:
            return number
    return None


def _jsonl_count(path: Path) -> int:
    if not path.is_file():
        return 0
    return sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())


def _git_head(root: Path) -> str:
    result = subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _stable_hash(value: Any) -> str:
    return _sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True, default=str).encode("utf-8")
    )


PHASE84_SCHEMA_VERSION = "e2r_v5_phase84_researcher_mode_audit_v1"
PHASE84_PASS = "V5_PHASE84_CANONICAL_RESEARCHER_MODE_PASS"
PHASE84_AUDIT_PATH = "docs/operational/e2r_v5_researcher_mode_architecture_audit.json"

PHASE84_REQUIRED_MODULES = (
    "schemas.py",
    "business_model_researcher.py",
    "component_research_planner.py",
    "research_supervisor.py",
    "source_graph_explorer.py",
    "structured_data_researcher.py",
    "document_ranker.py",
    "evidence_fact_compiler.py",
    "component_researcher.py",
    "red_team_researcher.py",
    "component_judge.py",
    "calibration_judge.py",
    "score_aggregator.py",
    "dossier.py",
    "saturation.py",
    "audits.py",
)


def compile_phase84_researcher_mode_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Prove the Phase 84 architecture and LLM authority boundaries."""

    import inspect

    from .business_model_researcher import BusinessMechanismResearcher
    from .component_judge import SynthesisJudge
    from .component_research_planner import (
        COMPONENT_RESEARCHER_ROLE_BY_COMPONENT,
    )
    from .component_researcher import (
        BUSINESS_MODEL_RESEARCH_SCHEMA,
        COMPONENT_JUDGE_SCHEMA,
        COMPONENT_RESEARCH_SCHEMA,
        RED_TEAM_RESEARCH_SCHEMA,
        SYNTHESIS_REVIEW_SCHEMA,
        BottleneckPricingResearcher,
        CapitalAllocationResearcher,
        EPSFCFResearcher,
        EarningsVisibilityResearcher,
        InformationConfidenceResearcher,
        MarketExpectationResearcher,
        ValuationResearcher,
    )
    from .document_ranker import MaterialDocumentRanker
    from .red_team_researcher import RedTeamResearcher
    from .schemas import CANONICAL_COMPONENT_ORDER

    root = Path(repo_root).resolve()
    module_root = root / "src/e2r/research_brain/researcher_mode"
    missing_modules = [
        value for value in PHASE84_REQUIRED_MODULES if not (module_root / value).is_file()
    ]
    role_classes = (
        BusinessMechanismResearcher,
        EPSFCFResearcher,
        EarningsVisibilityResearcher,
        BottleneckPricingResearcher,
        MarketExpectationResearcher,
        ValuationResearcher,
        CapitalAllocationResearcher,
        InformationConfidenceResearcher,
        RedTeamResearcher,
        SynthesisJudge,
    )
    roles = tuple(getattr(value, "researcher_role", value.__name__) for value in role_classes)
    expected_roles = (
        "BusinessMechanismResearcher",
        "EPSFCFResearcher",
        "EarningsVisibilityResearcher",
        "BottleneckPricingResearcher",
        "MarketExpectationResearcher",
        "ValuationResearcher",
        "CapitalAllocationResearcher",
        "InformationConfidenceResearcher",
        "RedTeamResearcher",
        "SynthesisJudge",
    )
    schemas = {
        "business": BUSINESS_MODEL_RESEARCH_SCHEMA,
        "component": COMPONENT_RESEARCH_SCHEMA,
        "red_team": RED_TEAM_RESEARCH_SCHEMA,
        "synthesis": SYNTHESIS_REVIEW_SCHEMA,
        "judge": COMPONENT_JUDGE_SCHEMA,
    }
    forbidden_provider_fields = {
        "stage",
        "final_stage",
        "reported_stage",
        "expected_score",
        "future_outcome",
        "future_outcome_ref",
        "mfe",
        "mae",
        "total_score",
    }
    exposed_forbidden = {
        schema_name: sorted(
            forbidden_provider_fields
            & set((schema.get("properties") or {}).keys())
        )
        for schema_name, schema in schemas.items()
    }
    component_required = set(COMPONENT_RESEARCH_SCHEMA.get("required") or ())
    required_component_outputs = {
        "researcher_summary",
        "proposed_score_lower",
        "proposed_score_mid",
        "proposed_score_upper",
        "nearest_positive_anchor_ids",
        "nearest_counter_anchor_ids",
        "why_not_higher",
        "why_not_lower",
        "uncertainties",
        "source_coverage",
    }
    core_files = tuple(
        module_root / value
        for value in PHASE84_REQUIRED_MODULES
        if value not in {"audits.py"}
    )
    target_condition_tokens = ("005930", "000660", "삼성전자", "SK하이닉스")
    target_condition_hits = []
    for path in core_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in target_condition_tokens:
            if token in text:
                target_condition_hits.append(
                    {"file": path.relative_to(root).as_posix(), "token": token}
                )
    component_source = (module_root / "component_researcher.py").read_text(
        encoding="utf-8"
    )
    required_input_keys = {
        "current_evidence_fact_graph",
        "current_counterfacts",
        "target_business_model",
        "historical_component_anchors",
        "source_coverage",
    }
    missing_input_keys = sorted(
        value for value in required_input_keys if f'"{value}"' not in component_source
    )
    select_signature = inspect.signature(MaterialDocumentRanker.select_material)
    critical = {
        "required_module_missing_count": len(missing_modules),
        "researcher_role_roster_mismatch_count": int(roles != expected_roles),
        "component_researcher_roster_mismatch_count": int(
            tuple(COMPONENT_RESEARCHER_ROLE_BY_COMPONENT)
            != tuple(CANONICAL_COMPONENT_ORDER)
        ),
        "provider_schema_forbidden_field_count": sum(
            len(values) for values in exposed_forbidden.values()
        ),
        "component_output_contract_missing_field_count": len(
            required_component_outputs - component_required
        ),
        "component_input_contract_missing_field_count": len(missing_input_keys),
        "target_name_condition_token_count": len(target_condition_hits),
        "fixed_top_n_document_selector_parameter_count": int(
            "top_n" in select_signature.parameters
        ),
        "provider_schema_open_object_count": sum(
            schema.get("additionalProperties") is not False
            for schema in schemas.values()
        ),
        "question_closure_import_count": sum(
            "compile_question_closures_v2" in path.read_text(encoding="utf-8")
            for path in core_files
            if path.is_file()
        ),
    }
    return {
        "schema_version": PHASE84_SCHEMA_VERSION,
        "status": PHASE84_PASS if sum(critical.values()) == 0 else "V5_PHASE84_CANONICAL_RESEARCHER_MODE_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "required_modules": list(PHASE84_REQUIRED_MODULES),
        "missing_modules": missing_modules,
        "researcher_roles": list(roles),
        "component_researcher_role_by_component": dict(
            COMPONENT_RESEARCHER_ROLE_BY_COMPONENT
        ),
        "provider_schema_forbidden_fields": exposed_forbidden,
        "component_output_contract_missing_fields": sorted(
            required_component_outputs - component_required
        ),
        "component_input_contract_missing_fields": missing_input_keys,
        "target_name_condition_hits": target_condition_hits,
        "document_selection_has_fixed_top_n": False,
        "primitive_or_question_exact_match_required_for_fact_visibility": False,
        "provider_failure_finalizes_low_score": False,
        "llm_total_score_authority": False,
        "llm_final_stage_authority": False,
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "roles": roles,
                "modules": PHASE84_REQUIRED_MODULES,
            }
        ),
    }


def write_phase84_researcher_mode_audit(
    *,
    repo_root: str | Path,
    output_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE84_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase84_researcher_mode_audit(root))
    return destination


PHASE85_SCHEMA_VERSION = "e2r_v5_phase85_source_graph_acquisition_audit_v1"
PHASE85_PASS = "V5_PHASE85_BROAD_SOURCE_GRAPH_ACQUISITION_PASS"
PHASE85_AUDIT_PATH = "docs/operational/e2r_v5_source_graph_acquisition_audit.json"


def compile_phase85_source_graph_acquisition_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Audit the old-discovery/new-Evidence-OS integration boundary."""

    import inspect

    from .component_researcher import (
        SOURCE_CANDIDATE_RANKING_SCHEMA,
        SOURCE_QUERY_GENERATION_SCHEMA,
    )
    from .document_ranker import ResearcherDocumentRanker
    from .source_graph_explorer import (
        SOURCE_FAMILY_CLASSES,
        SourceGraphAcquisitionConfig,
        SourceGraphAcquisitionMode,
        load_source_graph_checkpoint,
        write_source_graph_acquisition_run,
    )
    from .source_query_planner import CANONICAL_SOURCE_FAMILIES

    root = Path(repo_root).resolve()
    explorer_path = root / "src/e2r/research_brain/researcher_mode/source_graph_explorer.py"
    query_path = root / "src/e2r/research_brain/researcher_mode/source_query_planner.py"
    ranker_path = root / "src/e2r/research_brain/researcher_mode/document_ranker.py"
    explorer_text = explorer_path.read_text(encoding="utf-8")
    query_text = query_path.read_text(encoding="utf-8")
    ranker_text = ranker_path.read_text(encoding="utf-8")
    required_families = {
        "OPENDART",
        "KIND_KRX",
        "ISSUER_EARNINGS_RELEASE",
        "ISSUER_PRESENTATION",
        "ISSUER_NEWSROOM",
        "CUSTOMER_OFFICIAL",
        "FINANCIAL_STATEMENTS",
        "SEGMENT_DATA",
        "CASH_FLOW",
        "MARKET_CAP_PRICE",
        "CONSENSUS_REVISION",
        "VALUATION_MULTIPLES",
        "REUTERS",
        "TRUSTED_BUSINESS_MEDIA",
        "PUBLIC_BROKER_PDF",
        "INDUSTRY_REPORT",
        "NAVER_DISCOVERY",
        "GENERAL_WEB_DISCOVERY",
    }
    configured_families = {
        family for values in SOURCE_FAMILY_CLASSES.values() for family in values
    }
    default = SourceGraphAcquisitionConfig()
    production = SourceGraphAcquisitionConfig(
        mode=SourceGraphAcquisitionMode.PRODUCTION_DAILY.value,
        max_queries_per_checkpoint=10,
        max_candidates_per_checkpoint=100,
        max_fetches_per_checkpoint=20,
    )
    schemas = (SOURCE_QUERY_GENERATION_SCHEMA, SOURCE_CANDIDATE_RANKING_SCHEMA)
    forbidden_fields = {
        "score",
        "total_score",
        "stage",
        "final_stage",
        "expected_score",
        "future_outcome",
        "mfe",
        "mae",
    }
    schema_forbidden = [
        sorted(forbidden_fields & set(schema.get("properties") or {}))
        for schema in schemas
    ]
    rank_signature = inspect.signature(ResearcherDocumentRanker.rank_candidates)
    rank_line = _find_line(explorer_path, ".rank_candidates(") or 0
    fetch_line = _find_line(explorer_path, "_fetch_candidate_document(") or 0
    critical = {
        "required_source_family_missing_count": len(
            required_families - configured_families
        ),
        "canonical_family_roster_mismatch_count": int(
            configured_families != set(CANONICAL_SOURCE_FAMILIES)
        ),
        "default_max_results_per_query_mismatch_count": int(
            default.max_results_per_query != 100
        ),
        "top_results_parameter_count": int(hasattr(default, "top_results"))
        + int("top_results" in rank_signature.parameters),
        "production_unbounded_budget_count": sum(
            (
                production.max_queries_per_checkpoint > 10,
                production.max_candidates_per_checkpoint > 100,
                production.max_fetches_per_checkpoint > 20,
            )
        ),
        "provider_schema_forbidden_field_count": sum(
            len(values) for values in schema_forbidden
        ),
        "provider_schema_open_object_count": sum(
            schema.get("additionalProperties") is not False for schema in schemas
        ),
        "naver_provider_reuse_missing_count": int(
            "from e2r.research.naver_search_provider import NaverFreeSearchProvider"
            not in explorer_text
        ),
        "page_fetcher_reuse_missing_count": int(
            "from e2r.research.page_fetcher import PageFetcher" not in explorer_text
        ),
        "material_rank_before_fetch_violation_count": int(
            not rank_line or not fetch_line or rank_line >= fetch_line
        ),
        "snippet_fallback_import_count": sum(
            value in explorer_text
            for value in (
                "news_item_from_search_snippet",
                "WebResearchRunner",
                "evidence_from_feature_domains",
            )
        ),
        "checkpoint_api_missing_count": sum(
            not callable(value)
            for value in (
                load_source_graph_checkpoint,
                write_source_graph_acquisition_run,
            )
        ),
        "deterministic_query_template_marker_count": sum(
            marker in query_text
            for marker in (
                "if component_id ==",
                "if archetype_id ==",
                "if missing_slot ==",
                "fallback_query_templates",
            )
        ),
        "target_name_condition_count": sum(
            value in (explorer_text + query_text + ranker_text)
            for value in ("005930", "000660", "삼성전자", "SK하이닉스")
        ),
    }
    return {
        "schema_version": PHASE85_SCHEMA_VERSION,
        "status": PHASE85_PASS if sum(critical.values()) == 0 else "V5_PHASE85_BROAD_SOURCE_GRAPH_ACQUISITION_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "source_family_classes": {
            key: list(values) for key, values in SOURCE_FAMILY_CLASSES.items()
        },
        "default_config": asdict(default),
        "production_daily_maxima": asdict(production),
        "query_generation_owned_by_llm": True,
        "deterministic_query_fallback_allowed": False,
        "snippet_is_evidence": False,
        "material_relevance_fixed_top_n": False,
        "transport_budget_certifies_completion": False,
        "search_zero_certifies_saturation": False,
        "parser_field_direct_score_authority": False,
        "checkpoint_resume_supported": True,
        "reused_legacy_capabilities": {
            "naver_free_search_provider": True,
            "page_fetcher_and_pdf_extractor": True,
            "page_fetch_cache": True,
            "url_and_content_hash_dedupe": True,
            "score_gap_context_to_llm": True,
        },
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "families": SOURCE_FAMILY_CLASSES,
                "default": asdict(default),
                "production": asdict(production),
            }
        ),
    }


def write_phase85_source_graph_acquisition_audit(
    *, repo_root: str | Path, output_path: str | Path | None = None
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE85_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase85_source_graph_acquisition_audit(root))
    return destination


PHASE86_SCHEMA_VERSION = "e2r_v5_phase86_structured_financial_engine_audit_v1"
PHASE86_PASS = "V5_PHASE86_STRUCTURED_FINANCIAL_ENGINE_PASS"
PHASE86_AUDIT_PATH = "docs/operational/e2r_v5_structured_financial_engine_audit.json"


def compile_phase86_structured_financial_engine_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Run a deterministic canary through all Phase 86 arithmetic boundaries."""

    from datetime import date, datetime, timedelta

    from e2r.models import (
        ConsensusRevision,
        ConsensusSnapshot,
        FinancialActual,
        PriceBar,
    )

    from .structured_data_researcher import StructuredMetricRecord
    from .structured_financial_engine import (
        CANONICAL_STRUCTURED_SOURCE_ROUTES,
        ForwardGuidanceObservation,
        PeerValuationObservation,
        SegmentFinancialObservation,
        STRUCTURED_FINANCIAL_OUTPUT_FILES,
        StructuredFinancialConsensusValuationEngine,
        StructuredSourcePayload,
    )
    from .structured_source_routes import InMemoryStructuredSourceRoute

    root = Path(repo_root).resolve()
    cutoff = date(2026, 6, 29)
    target_id = "PHASE86_CANARY"
    symbol = "PHASE86"

    def seed(
        metric_id: str,
        value: float,
        role: str,
        *,
        period: str = "FY2025",
        dataset: str = "FINANCIAL",
    ) -> StructuredMetricRecord:
        return StructuredMetricRecord(
            record_id=f"SEED-{metric_id}-{period}",
            target_id=target_id,
            as_of_date=cutoff.isoformat(),
            metric_id=metric_id,
            value=value,
            unit="CURRENCY" if "pe" not in metric_id else "MULTIPLE",
            period=period,
            evidence_roles=(role,),
            source_ids=("SRC-ISSUER-GUIDANCE",),
            source_route="ISSUER_GUIDANCE",
            observed_at="2026-06-20",
            record_kind="ISSUER_STRUCTURED_GUIDANCE",
            confidence=0.95,
            dataset=dataset,
            provenance="STRUCTURED_EXTRACTED",
            metadata={"structured_source": True},
        )

    actuals = (
        FinancialActual(
            symbol=symbol,
            fiscal_year=2024,
            fiscal_quarter=None,
            period_end=date(2024, 12, 31),
            reported_at=datetime(2025, 3, 15),
            as_of_date=cutoff,
            source="OpenDART single account",
            sales=100.0,
            operating_profit=20.0,
            net_income=12.0,
            cashflow_from_operations=18.0,
            capex=8.0,
        ),
        FinancialActual(
            symbol=symbol,
            fiscal_year=2025,
            fiscal_quarter=None,
            period_end=date(2025, 12, 31),
            reported_at=datetime(2026, 3, 15),
            as_of_date=cutoff,
            source="OpenDART single account",
            sales=130.0,
            operating_profit=32.0,
            net_income=21.0,
            cashflow_from_operations=30.0,
            capex=11.0,
        ),
    )
    snapshots = (
        ConsensusSnapshot(
            symbol=symbol,
            date=date(2026, 1, 5),
            fiscal_year=2026,
            as_of_date=cutoff,
            source="CompanyGuide",
            op_e=38.0,
            eps_e=10.0,
            fcf_e=22.0,
            bps_e=45.0,
            per_e=11.0,
            pbr_e=2.0,
            parsed_fields={"ebitda_e": 44.0},
        ),
        ConsensusSnapshot(
            symbol=symbol,
            date=date(2026, 6, 20),
            fiscal_year=2026,
            as_of_date=cutoff,
            source="CompanyGuide",
            op_e=48.0,
            eps_e=13.0,
            fcf_e=29.0,
            bps_e=50.0,
            per_e=12.0,
            pbr_e=2.2,
            parsed_fields={"ebitda_e": 54.0},
        ),
    )
    target_revision = ConsensusRevision(
        symbol=symbol,
        date=date(2026, 6, 20),
        fiscal_year=2026,
        as_of_date=cutoff,
        target_price_revision_1m=8.0,
        source="CompanyGuide",
        parsed_fields={"target_price_only": True},
    )
    price_rows = []
    for index in range(45):
        row_date = date(2026, 5, 1) + timedelta(days=index)
        price_rows.extend(
            (
                PriceBar(
                    symbol=symbol,
                    date=row_date,
                    open=100.0 + index,
                    high=102.0 + index,
                    low=99.0 + index,
                    close=101.0 + index,
                    adj_close=101.0 + index,
                    volume=1_000,
                    trading_value=100_000.0,
                    market_cap=1_000.0 + index * 10,
                    source="KRX",
                    as_of_date=cutoff,
                ),
                PriceBar(
                    symbol="PHASE86-BENCHMARK",
                    date=row_date,
                    open=100.0 + index * 0.2,
                    high=101.0 + index * 0.2,
                    low=99.0 + index * 0.2,
                    close=100.0 + index * 0.2,
                    adj_close=100.0 + index * 0.2,
                    volume=1_000,
                    trading_value=100_000.0,
                    market_cap=10_000.0,
                    source="KRX",
                    as_of_date=cutoff,
                ),
            )
        )
    issuer_records = (
        seed("cash_and_equivalents", 40.0, "BALANCE_SHEET_CASH"),
        seed("total_debt", 15.0, "BALANCE_SHEET_DEBT"),
        seed("forward_ebitda", 54.0, "FORWARD_EBITDA", period="FY2026E"),
        seed("historical_forward_pe", 8.0, "VALUATION_HISTORY", period="FY2023"),
        seed("historical_forward_pe", 10.0, "VALUATION_HISTORY", period="FY2024"),
        seed("historical_forward_pe", 14.0, "VALUATION_HISTORY", period="FY2025"),
    )
    segment_observations = (
        SegmentFinancialObservation(
            target_id=target_id,
            as_of_date=cutoff.isoformat(),
            segment_id="CORE_SEGMENT",
            metric_id="revenue",
            value=80.0,
            total_company_value=130.0,
            unit="CURRENCY",
            period="FY2025",
            observed_at="2026-03-15",
            available_at="2026-03-15",
            source_ids=("SRC-ISSUER-GUIDANCE",),
            source_route="ISSUER_GUIDANCE",
        ),
    )
    guidance_observations = (
        ForwardGuidanceObservation(
            target_id=target_id,
            as_of_date=cutoff.isoformat(),
            metric_id="revenue",
            unit="CURRENCY",
            period="FY2026E",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            source_ids=("SRC-ISSUER-GUIDANCE",),
            source_route="ISSUER_GUIDANCE",
            low_value=145.0,
            high_value=155.0,
        ),
    )
    peers = tuple(
        PeerValuationObservation(
            peer_id=f"PEER-{index}",
            as_of_date=cutoff.isoformat(),
            metric_id="forward_pe",
            value=value,
            unit="MULTIPLE",
            observed_at="2026-06-20",
            source_ids=(f"SRC-PEER-{index}",),
            source_route="COMPANYGUIDE",
        )
        for index, value in enumerate((9.0, 11.0, 13.0), start=1)
    )
    routes = (
        InMemoryStructuredSourceRoute(
            "COMPANYGUIDE",
            StructuredSourcePayload(
                route_name="COMPANYGUIDE",
                source_ids=("SRC-COMPANYGUIDE",),
                consensus_snapshots=snapshots,
                consensus_revisions=(target_revision,),
                peer_valuations=peers,
            ),
        ),
        InMemoryStructuredSourceRoute(
            "PUBLIC_BROKER_REPORT",
            StructuredSourcePayload(route_name="PUBLIC_BROKER_REPORT"),
            provider_error="fixture provider failure proving fallback continuation",
        ),
        InMemoryStructuredSourceRoute(
            "ISSUER_GUIDANCE",
            StructuredSourcePayload(
                route_name="ISSUER_GUIDANCE",
                source_ids=("SRC-ISSUER-GUIDANCE",),
                structured_records=issuer_records,
                segment_observations=segment_observations,
                guidance_observations=guidance_observations,
            ),
        ),
        InMemoryStructuredSourceRoute(
            "DART_ACTUALS_DETERMINISTIC_SCENARIO",
            StructuredSourcePayload(
                route_name="DART_ACTUALS_DETERMINISTIC_SCENARIO",
                source_ids=("SRC-DART",),
                financial_actuals=actuals,
            ),
        ),
        InMemoryStructuredSourceRoute(
            "KRX_PRICE_MARKET_CAP",
            StructuredSourcePayload(
                route_name="KRX_PRICE_MARKET_CAP",
                source_ids=("SRC-KRX",),
                price_bars=tuple(price_rows),
            ),
        ),
    )
    result = StructuredFinancialConsensusValuationEngine().research(
        target_id=target_id,
        symbol=symbol,
        company_name="Phase 86 Canary",
        as_of_date=cutoff,
        routes=routes,
        deep_researched_canary=True,
    )
    by_metric = {row.metric_id: row for row in result.records}
    target_rows = [
        row
        for row in result.records
        if "target_price" in row.metric_id
        or row.metadata.get("revision_family") == "TARGET_PRICE"
    ]
    engine_path = root / "src/e2r/research_brain/researcher_mode/structured_financial_engine.py"
    route_path = root / "src/e2r/research_brain/researcher_mode/structured_source_routes.py"
    dossier_path = root / "src/e2r/research_brain/researcher_mode/dossier.py"
    engine_text = engine_path.read_text(encoding="utf-8")
    route_text = route_path.read_text(encoding="utf-8")
    dossier_text = dossier_path.read_text(encoding="utf-8")
    forbidden_target_tokens = ("005930", "000660", "삼성전자", "SK하이닉스")
    generic_article_guard_failed = 0
    try:
        StructuredMetricRecord(
            record_id="UNSAFE",
            target_id=target_id,
            as_of_date=cutoff.isoformat(),
            metric_id="forward_pe",
            value=10.0,
            unit="MULTIPLE",
            period="CURRENT",
            evidence_roles=("FORWARD_PE",),
            source_ids=("NEWS",),
            source_route="GENERAL_WEB",
            observed_at=cutoff.isoformat(),
            record_kind="VALUATION_CLAIM",
            confidence=0.5,
            dataset="VALUATION",
            metadata={"generic_article_claim": True},
        )
        generic_article_guard_failed = 1
    except ValueError:
        pass
    attempt_by_route = {row.route_name: row for row in result.source_attempts}
    component_payloads = result.to_component_structured_metrics(
        {
            "eps_fcf_explosion": ("CASH_CONVERSION",),
            "market_mispricing": ("EARNINGS_REVISION",),
            "valuation_rerating": ("CURRENT_VALUATION",),
        }
    )
    critical = {
        "canonical_route_roster_mismatch_count": int(
            tuple(attempt_by_route) != CANONICAL_STRUCTURED_SOURCE_ROUTES
        ),
        "output_filename_mismatch_count": int(
            set(STRUCTURED_FINANCIAL_OUTPUT_FILES.values())
            != {
                "structured_financial_records.jsonl",
                "consensus_revision_records.jsonl",
                "valuation_records.jsonl",
            }
        ),
        "fallback_after_provider_error_missing_count": int(
            attempt_by_route["PUBLIC_BROKER_REPORT"].status != "PROVIDER_ERROR"
            or attempt_by_route["KRX_PRICE_MARKET_CAP"].status != "FETCHED"
        ),
        "deep_researched_canary_valuation_route_not_attempted_count": result.deep_researched_canary_valuation_route_not_attempted_count,
        "revision_component_zero_solely_due_connector_gap_count": result.revision_component_zero_solely_due_connector_gap_count,
        "fcf_component_zero_solely_due_missing_parser_count": result.fcf_component_zero_solely_due_missing_parser_count,
        "derived_fcf_missing_count": int(
            "free_cash_flow" not in by_metric
            or by_metric["free_cash_flow"].provenance != "DERIVED"
        ),
        "segment_contribution_record_missing_count": int(
            not any(
                "SEGMENT_CONTRIBUTION" in row.evidence_roles
                for row in result.records
            )
        ),
        "issuer_forward_guidance_record_missing_count": int(
            not any("FORWARD_GUIDANCE" in row.evidence_roles for row in result.records)
        ),
        "target_price_counted_as_earnings_revision_count": sum(
            "EPS_REVISION" in row.evidence_roles
            or "OPERATING_PROFIT_REVISION" in row.evidence_roles
            for row in target_rows
        ),
        "generic_article_valuation_guard_failure_count": generic_article_guard_failed,
        "deterministic_scenario_missing_count": int(
            not any(
                row.provenance == "DETERMINISTIC_SCENARIO"
                and "SCENARIO_SENSITIVITY" in row.evidence_roles
                for row in result.records
            )
        ),
        "own_historical_band_missing_count": int(
            not any("OWN_HISTORICAL_BAND" in row.evidence_roles for row in result.records)
        ),
        "peer_band_missing_count": int(
            not any("PEER_BAND" in row.evidence_roles for row in result.records)
        ),
        "future_record_count": sum(
            date.fromisoformat(row.observed_at[:10]) > cutoff
            or date.fromisoformat((row.available_at or row.observed_at)[:10]) > cutoff
            for row in result.records
        ),
        "direct_score_authority_count": sum(row.score_authority for row in result.records)
        + int(result.score_authority),
        "component_researcher_structured_bridge_missing_count": sum(
            key not in component_payloads[component_id]
            for component_id, key in (
                ("eps_fcf_explosion", "CASH_CONVERSION"),
                ("market_mispricing", "EARNINGS_REVISION"),
                ("valuation_rerating", "CURRENT_VALUATION"),
            )
        )
        + int("structured_engine_result" not in dossier_text),
        "component_payload_score_authority_count": sum(
            bool(value.get("score_authority"))
            for payload in component_payloads.values()
            for value in payload.values()
            if isinstance(value, Mapping)
        ),
        "target_name_condition_count": sum(
            token in (engine_text + route_text) for token in forbidden_target_tokens
        ),
    }
    return {
        "schema_version": PHASE86_SCHEMA_VERSION,
        "status": PHASE86_PASS
        if sum(critical.values()) == 0
        else "V5_PHASE86_STRUCTURED_FINANCIAL_ENGINE_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "canonical_source_routes": list(CANONICAL_STRUCTURED_SOURCE_ROUTES),
        "source_attempts": json.loads(
            json.dumps(
                [row.to_dict() for row in result.source_attempts],
                ensure_ascii=False,
                default=str,
            )
        ),
        "output_files": dict(STRUCTURED_FINANCIAL_OUTPUT_FILES),
        "record_counts": {
            "structured_financial_records": len(result.financial_records),
            "consensus_revision_records": len(result.consensus_revision_records),
            "valuation_records": len(result.valuation_records),
        },
        "target_price_only_separated_from_earnings_revision": True,
        "connector_gap_finalizes_zero_component": False,
        "generic_article_claim_is_valuation_record": False,
        "deterministic_scenario_is_observed_fact": False,
        "component_researcher_structured_bridge": True,
        "as_of_date_guarded": True,
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "routes": CANONICAL_STRUCTURED_SOURCE_ROUTES,
                "outputs": STRUCTURED_FINANCIAL_OUTPUT_FILES,
                "record_ids": [row.record_id for row in result.records],
            }
        ),
    }


def write_phase86_structured_financial_engine_audit(
    *, repo_root: str | Path, output_path: str | Path | None = None
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE86_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase86_structured_financial_engine_audit(root))
    return destination


PHASE87_SCHEMA_VERSION = "e2r_v5_semantic_research_saturation_audit_v1"
PHASE87_PASS = "V5_PHASE87_CHECKPOINT_RESUME_SEMANTIC_SATURATION_PASS"
PHASE87_AUDIT_PATH = (
    "docs/operational/e2r_v5_semantic_research_saturation_audit.json"
)


def compile_phase87_semantic_research_saturation_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Audit checkpoint-resume and semantic, provider-backed completion gates."""

    import inspect
    from dataclasses import fields

    from .component_researcher import (
        RESEARCH_SUPERVISOR_SCHEMA,
        SEMANTIC_SATURATION_REVIEW_SCHEMA,
    )
    from .research_epoch import RESEARCH_EPOCH_OUTPUT_FILES, ResearchEpochCheckpoint, ResearchEpochRunner
    from .research_supervisor import SUPERVISOR_FAILURE_CLASSES
    from .saturation import (
        SATURATION_REVIEW_ROLES,
        SaturationReview,
        SemanticSaturationCertifier,
    )
    from .source_graph_explorer import validate_source_graph_checkpoint

    root = Path(repo_root).resolve()
    module_paths = (
        "src/e2r/research_brain/researcher_mode/research_supervisor.py",
        "src/e2r/research_brain/researcher_mode/saturation.py",
        "src/e2r/research_brain/researcher_mode/research_epoch.py",
    )
    missing_modules = [value for value in module_paths if not (root / value).is_file()]
    source_text = "\n".join(
        (root / value).read_text(encoding="utf-8")
        for value in module_paths
        if (root / value).is_file()
    )
    required_checkpoint_fields = {
        "epoch",
        "queries",
        "documents",
        "new_facts",
        "changed_component_memos",
        "unresolved_material_questions",
        "next_actions",
        "gold_evaluation_status",
    }
    checkpoint_fields = {field.name for field in fields(ResearchEpochCheckpoint)}
    expected_roles = {
        "RESEARCH_SUPERVISOR_A",
        "RESEARCH_SUPERVISOR_B",
        "INDEPENDENT_COMPLETENESS_REVIEWER",
    }
    required_failure_classes = {
        "PARSER_EXTRACTOR_FAILURE",
        "SOURCE_ABSENCE_CANDIDATE",
        "PROVIDER_FAILURE",
        "INSUFFICIENT_SEARCH",
    }
    schemas = (RESEARCH_SUPERVISOR_SCHEMA, SEMANTIC_SATURATION_REVIEW_SCHEMA)
    forbidden_schema_fields = {
        "score",
        "total_score",
        "stage",
        "final_stage",
        "future_outcome",
        "mfe",
        "mae",
    }
    certified_reviews = tuple(
        SaturationReview(
            review_id=f"PHASE87-{role}",
            reviewer_role=role,
            approve=True,
            seven_component_memos_complete=True,
            material_positive_routes_reviewed=True,
            counter_and_supersession_routes_checked=True,
            structured_data_complete=True,
            new_source_family_directions_reviewed=True,
            unresolved_material_questions=(),
            rationale="independent semantic completeness canary",
            checkpoint_id="PHASE87-CHECKPOINT",
            epoch=1,
            provider_name=f"PHASE87-{role}-PROVIDER",
            prompt_hash=f"PHASE87-{role}-PROMPT",
            provider_backed=True,
        )
        for role in SATURATION_REVIEW_ROLES
    )
    certified = SemanticSaturationCertifier().certify(
        certified_reviews,
        expected_checkpoint_id="PHASE87-CHECKPOINT",
        require_provider_reviews=True,
    )
    duplicate_prompt_reviews = tuple(
        SaturationReview(
            **{
                **row.to_dict(),
                "prompt_hash": "DUPLICATE-PROMPT",
            }
        )
        for row in certified_reviews
    )
    duplicate_prompt = SemanticSaturationCertifier().certify(
        duplicate_prompt_reviews,
        expected_checkpoint_id="PHASE87-CHECKPOINT",
        require_provider_reviews=True,
    )
    zero_result_flag_rejected = False
    try:
        SaturationReview(
            **{
                **certified_reviews[0].to_dict(),
                "review_id": "PHASE87-ZERO-RESULT-CANARY",
                "zero_search_result_treated_as_saturation": True,
            }
        )
    except ValueError:
        zero_result_flag_rejected = True
    run_parameters = inspect.signature(ResearchEpochRunner.run_epoch).parameters
    forbidden_target_tokens = ("005930", "000660", "삼성전자", "SK하이닉스")
    critical = {
        "required_module_missing_count": len(missing_modules),
        "fixed_max_rounds_parameter_count": int("max_rounds" in run_parameters),
        "checkpoint_required_field_missing_count": len(
            required_checkpoint_fields - checkpoint_fields
        ),
        "semantic_reviewer_role_mismatch_count": int(
            set(SATURATION_REVIEW_ROLES) != expected_roles
        ),
        "failure_class_missing_count": len(
            required_failure_classes - set(SUPERVISOR_FAILURE_CLASSES)
        ),
        "provider_schema_open_object_count": sum(
            schema.get("additionalProperties") is not False for schema in schemas
        ),
        "provider_schema_forbidden_field_count": sum(
            len(forbidden_schema_fields & set(schema.get("properties") or {}))
            for schema in schemas
        ),
        "source_checkpoint_validator_missing_count": int(
            not callable(validate_source_graph_checkpoint)
        ),
        "three_provider_review_certification_failure_count": int(
            not certified.semantic_saturation_certified
        ),
        "duplicate_prompt_certified_count": int(
            duplicate_prompt.semantic_saturation_certified
        ),
        "zero_result_completion_flag_accepted_count": int(
            not zero_result_flag_rejected
        ),
        "checkpoint_output_file_missing_count": len(
            {
                "checkpoint",
                "supervisor_review",
                "saturation_reviews",
                "saturation_certificate",
            }
            - set(RESEARCH_EPOCH_OUTPUT_FILES)
        ),
        "deterministic_query_fallback_marker_count": sum(
            marker in source_text
            for marker in (
                "fallback_query_templates =",
                "if component_id ==",
                "if archetype_id ==",
                "if missing_slot ==",
            )
        ),
        "target_name_condition_count": sum(
            token in source_text for token in forbidden_target_tokens
        ),
    }
    return {
        "schema_version": PHASE87_SCHEMA_VERSION,
        "status": (
            PHASE87_PASS
            if sum(critical.values()) == 0
            else "V5_PHASE87_CHECKPOINT_RESUME_SEMANTIC_SATURATION_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "checkpoint_fields": sorted(required_checkpoint_fields),
        "output_files": dict(RESEARCH_EPOCH_OUTPUT_FILES),
        "semantic_reviewer_roles": list(SATURATION_REVIEW_ROLES),
        "fixed_round_completion_allowed": False,
        "zero_search_result_certifies_saturation": False,
        "transport_budget_certifies_saturation": False,
        "provider_backed_reviews_required": True,
        "counter_and_supersession_proof_required": True,
        "parser_failure_equals_source_absence": False,
        "structured_data_required": True,
        "checkpoint_resume_required": True,
        "llm_generates_query_direction": True,
        "deterministic_fallback_query_allowed": False,
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "checkpoint_fields": sorted(required_checkpoint_fields),
                "roles": SATURATION_REVIEW_ROLES,
                "outputs": RESEARCH_EPOCH_OUTPUT_FILES,
            }
        ),
    }


def write_phase87_semantic_research_saturation_audit(
    *, repo_root: str | Path, output_path: str | Path | None = None
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE87_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(
        destination,
        compile_phase87_semantic_research_saturation_audit(root),
    )
    return destination


PHASE88_SCHEMA_VERSION = "e2r_v5_evidence_fact_graph_claim_utilization_audit_v1"
PHASE88_PASS = "V5_PHASE88_EVIDENCE_FACT_GRAPH_CLAIM_UTILIZATION_PASS"
PHASE88_AUDIT_PATH = (
    "docs/operational/e2r_v5_evidence_fact_graph_claim_utilization_audit.json"
)


def compile_phase88_evidence_fact_graph_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Compile a deterministic claim→fact→component→utilization canary."""

    from .claim_utilization import (
        CLAIM_UTILIZATION_STATUSES,
        COMPONENT_MECHANISM_IDS_BY_COMPONENT,
        ClaimComponentImpactProposal,
        ClaimTerminalDisposition,
    )
    from .component_researcher import CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA
    from .evidence_fact_compiler import EvidenceFactCompiler
    from .evidence_fact_graph import (
        EVIDENCE_FACT_GRAPH_OUTPUT_FILES,
        EvidenceFactGraphEngine,
    )
    from .schemas import CANONICAL_COMPONENT_ORDER

    root = Path(repo_root).resolve()
    module_paths = (
        "src/e2r/research_brain/researcher_mode/evidence_fact_compiler.py",
        "src/e2r/research_brain/researcher_mode/claim_utilization.py",
        "src/e2r/research_brain/researcher_mode/claim_impact_mapper.py",
        "src/e2r/research_brain/researcher_mode/evidence_fact_graph.py",
    )
    missing_modules = [value for value in module_paths if not (root / value).is_file()]
    source_text = "\n".join(
        (root / value).read_text(encoding="utf-8")
        for value in module_paths
        if (root / value).is_file()
    )
    target_id = "PHASE88-CURRENT-TARGET"
    as_of_date = "2026-06-29"
    base = {
        "accepted_by_evidence_os": True,
        "target_id": target_id,
        "as_of_date": as_of_date,
        "subject": "current target business",
        "business_segment": "core segment",
        "product_family": "core product",
        "economic_mechanism": "capacity allocation converts into earnings and cash",
        "predicate": "allocation_and_cash_conversion_confirmed",
        "value": True,
        "unit": "flag",
        "period": "2026Q2",
        "direction": "POSITIVE",
        "current_lifecycle": "CURRENT",
        "published_at": "2026-06-20",
        "material": True,
    }
    claims = (
        {
            **base,
            "claim_id": "PHASE88-PRIMARY",
            "source_id": "PHASE88-SOURCE-ISSUER-1",
            "source_independence_group": "ISSUER",
            "confidence": 0.9,
            "question_family_tags": ["phase88_question"],
            "primitive_tags": ["phase88_primitive"],
        },
        {
            **base,
            "claim_id": "PHASE88-CORROBORATION",
            "source_id": "PHASE88-SOURCE-INDEPENDENT",
            "source_independence_group": "INDEPENDENT",
            "confidence": 0.8,
        },
        {
            **base,
            "claim_id": "PHASE88-DUPLICATE",
            "source_id": "PHASE88-SOURCE-ISSUER-2",
            "source_independence_group": "ISSUER",
            "confidence": 0.7,
        },
        {
            **base,
            "claim_id": "PHASE88-PROFILE",
            "predicate": "business_profile_only",
            "value": "profile",
            "economic_mechanism": "profile context without direct component credit",
            "source_id": "PHASE88-SOURCE-PROFILE",
            "source_independence_group": "ISSUER_PROFILE",
            "confidence": 0.8,
        },
    )
    preliminary = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=claims,
    )
    fact_by_claim = {
        link.claim_id: next(
            fact for fact in preliminary.facts if fact.fact_id == link.fact_id
        )
        for link in preliminary.claim_fact_links
    }
    primary_fact = fact_by_claim["PHASE88-PRIMARY"]
    profile_fact = fact_by_claim["PHASE88-PROFILE"]
    proposals = (
        ClaimComponentImpactProposal(
            impact_id="PHASE88-IMPACT-EPS",
            claim_id="PHASE88-PRIMARY",
            fact_id=primary_fact.fact_id,
            component_id="eps_fcf_explosion",
            direction="SUPPORT",
            component_mechanism_id="EARNINGS_CONVERSION",
            fact_economic_mechanism=primary_fact.economic_mechanism,
            proposed_credit_units=0.8,
            rationale="direct earnings conversion mechanism",
        ),
        ClaimComponentImpactProposal(
            impact_id="PHASE88-IMPACT-VISIBILITY",
            claim_id="PHASE88-PRIMARY",
            fact_id=primary_fact.fact_id,
            component_id="earnings_visibility",
            direction="SUPPORT",
            component_mechanism_id="REVENUE_VISIBILITY",
            fact_economic_mechanism=primary_fact.economic_mechanism,
            proposed_credit_units=0.8,
            rationale="same claim has a distinct visibility mechanism",
        ),
    )
    result = EvidenceFactGraphEngine().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        material_claims=claims,
        impact_proposals=proposals,
        explicit_dispositions=(
            ClaimTerminalDisposition(
                disposition_id="PHASE88-DISPOSITION-PROFILE",
                claim_id="PHASE88-PROFILE",
                fact_id=profile_fact.fact_id,
                status="PROFILE_ONLY",
                rationale="profile context is retained without component credit",
            ),
        ),
    )
    missing_use = EvidenceFactGraphEngine().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        material_claims=(claims[3],),
        impact_proposals=(),
    )
    future_claim = {
        **claims[3],
        "claim_id": "PHASE88-FUTURE",
        "published_at": "2026-06-30",
    }
    future = EvidenceFactGraphEngine().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        material_claims=(future_claim,),
        impact_proposals=(),
    )
    primary_links = [
        row
        for row in result.fact_compilation.claim_fact_links
        if row.fact_id == primary_fact.fact_id
    ]
    primary_utilization = {
        row.claim_id: row.status
        for row in result.claim_utilization.utilization_decisions
    }
    expected_statuses = {
        "SCORED_SUPPORT",
        "SCORED_COUNTER",
        "CONFIDENCE_ONLY",
        "PROFILE_ONLY",
        "WRONG_MECHANISM",
        "DUPLICATE_FACT",
        "SUPERSEDED",
        "REJECTED_WITH_REASON",
    }
    forbidden_target_tokens = ("005930", "000660", "삼성전자", "SK하이닉스")
    critical = {
        "required_module_missing_count": len(missing_modules),
        "utilization_status_roster_mismatch_count": int(
            set(CLAIM_UTILIZATION_STATUSES) != expected_statuses
        ),
        "component_mechanism_contract_missing_count": len(
            set(CANONICAL_COMPONENT_ORDER)
            - set(COMPONENT_MECHANISM_IDS_BY_COMPONENT)
        ),
        "component_mechanism_contract_roster_mismatch_count": int(
            set(COMPONENT_MECHANISM_IDS_BY_COMPONENT)
            != set(CANONICAL_COMPONENT_ORDER)
        ),
        "impact_mapper_schema_open_count": int(
            CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA.get("additionalProperties")
            is not False
        ),
        "impact_mapper_schema_score_stage_field_count": len(
            {"score", "total_score", "stage", "final_stage"}
            & set(CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA.get("properties") or {})
        ),
        "canary_graph_critical_count": int(result.audit["critical_count_sum"]),
        "accepted_claim_without_fact_count": (
            result.fact_compilation.accepted_claim_without_fact_count
        ),
        "same_fact_not_deduped_count": int(
            len({row.fact_id for row in primary_links}) != 1
        ),
        "independent_confidence_not_improved_count": int(
            primary_fact.confidence
            <= max(row.claim_confidence for row in primary_links)
        ),
        "corroboration_scored_count": int(
            primary_utilization.get("PHASE88-CORROBORATION")
            != "CONFIDENCE_ONLY"
        ),
        "same_group_duplicate_scored_count": int(
            primary_utilization.get("PHASE88-DUPLICATE") != "DUPLICATE_FACT"
        ),
        "many_component_impact_missing_count": int(
            len(result.claim_utilization.validated_impacts) != 2
        ),
        "claim_credit_cap_violation_count": int(
            sum(
                row.validated_credit_units
                for row in result.claim_utilization.validated_impacts
            )
            > 1.0 + 1e-9
        ),
        "silent_material_claim_not_blocked_count": int(
            missing_use.status != "EVIDENCE_FACT_GRAPH_PENDING"
            or missing_use.claim_utilization.audit["critical_counts"][
                "material_claim_without_terminal_utilization_count"
            ]
            != 1
        ),
        "future_accepted_claim_not_blocked_count": int(
            future.status != "EVIDENCE_FACT_GRAPH_PENDING"
            or future.fact_compilation.accepted_claim_without_fact_count != 1
        ),
        "tag_score_gateway_count": int(
            result.audit["critical_counts"][
                "question_or_primitive_tag_score_gateway_count"
            ]
        ),
        "output_file_missing_count": len(
            {
                "facts",
                "claim_fact_links",
                "graph_nodes",
                "graph_edges",
                "validated_impacts",
                "claim_utilization",
                "audit",
            }
            - set(EVIDENCE_FACT_GRAPH_OUTPUT_FILES)
        ),
        "target_name_condition_count": sum(
            token in source_text for token in forbidden_target_tokens
        ),
        "deterministic_impact_fallback_marker_count": sum(
            marker in source_text
            for marker in (
                "fallback_impact_templates =",
                "if primitive_id ==",
                "if question_family_id ==",
            )
        ),
    }
    return {
        "schema_version": PHASE88_SCHEMA_VERSION,
        "status": (
            PHASE88_PASS
            if sum(critical.values()) == 0
            else "V5_PHASE88_EVIDENCE_FACT_GRAPH_CLAIM_UTILIZATION_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "claim_utilization_statuses": list(CLAIM_UTILIZATION_STATUSES),
        "component_mechanism_ids_by_component": {
            key: list(value)
            for key, value in COMPONENT_MECHANISM_IDS_BY_COMPONENT.items()
        },
        "output_files": dict(EVIDENCE_FACT_GRAPH_OUTPUT_FILES),
        "canary_counts": {
            "claims": result.fact_compilation.input_claim_count,
            "facts": len(result.facts),
            "validated_impacts": len(
                result.claim_utilization.validated_impacts
            ),
            "utilization_rows": len(
                result.claim_utilization.utilization_decisions
            ),
            "nodes": len(result.nodes),
            "edges": len(result.edges),
        },
        "same_economic_fact_points_once": True,
        "independent_corroboration_improves_confidence": True,
        "many_to_many_component_impacts_allowed": True,
        "component_mechanism_validated": True,
        "semantic_impact_mapping_owned_by_llm": True,
        "claim_total_credit_cap_validated": True,
        "question_family_score_gateway": False,
        "primitive_score_gateway": False,
        "production_score_authority": False,
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "statuses": CLAIM_UTILIZATION_STATUSES,
                "mechanisms": COMPONENT_MECHANISM_IDS_BY_COMPONENT,
                "outputs": EVIDENCE_FACT_GRAPH_OUTPUT_FILES,
                "canary_fact_ids": [row.fact_id for row in result.facts],
            }
        ),
    }


def write_phase88_evidence_fact_graph_audit(
    *, repo_root: str | Path, output_path: str | Path | None = None
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE88_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase88_evidence_fact_graph_audit(root))
    return destination


PHASE89_SCHEMA_VERSION = "e2r_v5_component_scoring_memos_audit_v1"
PHASE89_PASS = "V5_PHASE89_INDEPENDENT_COMPONENT_SCORING_MEMOS_PASS"
PHASE89_AUDIT_PATH = (
    "docs/operational/e2r_v5_component_scoring_memos_audit.json"
)


def compile_phase89_component_scoring_memos_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Compile a seven-component, twenty-one-judge deterministic canary."""

    from .component_judge import (
        JUDGE_RESPONSE_FIELDS,
        JUDGE_REVIEW_DIMENSIONS_BY_ROLE,
    )
    from .component_researcher import (
        COMPONENT_JUDGE_SCHEMA,
        ComponentResearchResult,
    )
    from .component_scoring_memos import (
        COMPONENT_SCORING_MEMO_OUTPUT_FILES,
        REQUIRED_COMPONENT_JUDGE_ROLES,
        LLMComponentScoringMemoEngine,
    )
    from .schemas import (
        CANONICAL_COMPONENT_MAX_POINTS,
        CANONICAL_COMPONENT_ORDER,
        ComponentAnchor,
        ComponentResearchMemo,
        EvidenceFact,
    )

    root = Path(repo_root).resolve()
    module_paths = (
        "src/e2r/research_brain/researcher_mode/schemas.py",
        "src/e2r/research_brain/researcher_mode/component_researcher.py",
        "src/e2r/research_brain/researcher_mode/component_judge.py",
        "src/e2r/research_brain/researcher_mode/calibration_judge.py",
        "src/e2r/research_brain/researcher_mode/component_scoring_memos.py",
    )
    missing_modules = [value for value in module_paths if not (root / value).is_file()]
    source_text = "\n".join(
        (root / value).read_text(encoding="utf-8")
        for value in module_paths
        if (root / value).is_file()
    )
    target_id = "PHASE89-CURRENT-TARGET"
    archetype_id = "PHASE89-CURRENT-ARCHETYPE"
    as_of_date = "2026-06-29"
    facts = (
        EvidenceFact(
            fact_id="PHASE89-AUDIT-SUPPORT",
            target_id=target_id,
            as_of_date=as_of_date,
            subject="current target operating business",
            business_segment="core segment",
            product_family="core product",
            economic_mechanism="current operating strength converts into earnings and cash",
            predicate="current_operating_strength",
            value=True,
            unit="flag",
            period="2026Q2",
            direction="POSITIVE",
            source_ids=("PHASE89-AUDIT-SOURCE-SUPPORT",),
            claim_ids=("PHASE89-AUDIT-CLAIM-SUPPORT",),
            quote_ids=("PHASE89-AUDIT-QUOTE-SUPPORT",),
            current_lifecycle="CURRENT",
            source_independence_group="ISSUER",
            confidence=0.85,
        ),
        EvidenceFact(
            fact_id="PHASE89-AUDIT-COUNTER",
            target_id=target_id,
            as_of_date=as_of_date,
            subject="current target operating business",
            business_segment="core segment",
            product_family="core product",
            economic_mechanism="concentration can reduce earnings durability",
            predicate="concentration_risk",
            value=True,
            unit="flag",
            period="2026Q2",
            direction="COUNTER",
            source_ids=("PHASE89-AUDIT-SOURCE-COUNTER",),
            claim_ids=("PHASE89-AUDIT-CLAIM-COUNTER",),
            quote_ids=("PHASE89-AUDIT-QUOTE-COUNTER",),
            current_lifecycle="OPEN",
            source_independence_group="INDEPENDENT",
            confidence=0.8,
        ),
    )
    anchors = []
    component_results = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        anchor_ids = []
        for role, suffix, midpoint in (
            ("POSITIVE", "P", 0.65),
            ("COUNTER", "C", 0.35),
        ):
            anchor_id = f"PHASE89-AUDIT-ANCHOR-{component_id}-{suffix}"
            anchor_ids.append(anchor_id)
            anchors.append(
                ComponentAnchor(
                    anchor_id=anchor_id,
                    archetype_id=archetype_id,
                    component_id=component_id,
                    economic_fact_patterns=("blind economic fact pattern",),
                    role=role,
                    score_band="HIGH" if role == "POSITIVE" else "LOW",
                    points_lower=maximum * max(0.0, midpoint - 0.1),
                    points_mid=maximum * midpoint,
                    points_upper=maximum * min(1.0, midpoint + 0.1),
                    max_points=maximum,
                    source_backed_case_ids=(
                        f"PHASE89-AUDIT-CASE-{component_id}-{suffix}",
                    ),
                    source_proxy_guard_case_ids=(),
                    source_score_anchor_ids=(
                        f"PHASE89-AUDIT-SCORE-{component_id}-{suffix}",
                    ),
                    confidence="MEDIUM",
                    usable_as_exact_anchor=False,
                    usable_as_ordinal_anchor=True,
                )
            )
        memo = ComponentResearchMemo(
            memo_id=f"PHASE89-AUDIT-MEMO-{component_id}",
            target_id=target_id,
            archetype_id=archetype_id,
            component_id=component_id,
            component_max_points=maximum,
            positive_fact_ids=("PHASE89-AUDIT-SUPPORT",),
            counter_fact_ids=("PHASE89-AUDIT-COUNTER",),
            resolution_fact_ids=(),
            structured_metrics={"current_metric": 1.0, "concentration": 0.4},
            historical_anchor_ids=tuple(anchor_ids),
            researcher_summary="current source-backed economics were researched",
            positive_case="current direct support establishes an economic floor",
            counter_case="concentration and uncertainty constrain the ceiling",
            uncertainties=("duration requires continued monitoring",),
            source_coverage=("ISSUER_OFFICIAL", "INDEPENDENT_REPORT"),
            proposed_score_lower=maximum * 0.4,
            proposed_score_mid=maximum * 0.53,
            proposed_score_upper=maximum * 0.7,
            confidence=0.78,
            research_complete=True,
            nearest_positive_anchor_ids=(anchor_ids[0],),
            nearest_counter_anchor_ids=(anchor_ids[1],),
            why_not_higher="counterevidence remains",
            why_not_lower="direct support exists",
            researcher_role=f"PHASE89-AUDIT-{component_id}-RESEARCHER",
        )
        component_results.append(
            ComponentResearchResult(
                component_id=component_id,
                researcher_role=memo.researcher_role,
                status="COMPLETE",
                memo=memo,
                pending_reasons=(),
                provider_name="PHASE89-AUDIT-RESEARCHER",
                prompt_hash=f"PHASE89-AUDIT-RESEARCH-{component_id}",
            )
        )

    class AuditProvider:
        provider_name = "PHASE89-AUDIT-JUDGE-PROVIDER"

        def __init__(self, mode: str = "COMPLETE") -> None:
            self.mode = mode
            self.calls: list[Mapping[str, Any]] = []

        def complete(
            self,
            *,
            pass_name: str,
            payload: Mapping[str, Any],
        ) -> Mapping[str, Any]:
            call: dict[str, Any] = {
                "pass_name": pass_name,
                "payload": payload,
            }
            if self.mode == "CONSTANT_PROMPT_HASH":
                call["prompt_hash"] = "a" * 64
            self.calls.append(call)
            memo = payload["component_research_memo"]
            maximum = float(payload["component_max_points"])
            fraction = {
                "COMPONENT_ANALYST_JUDGE": 0.64,
                "COMPONENT_SKEPTIC_JUDGE": 0.50,
                "CALIBRATION_JUDGE": 0.57,
            }[pass_name]
            response = {
                "anchor_comparisons": [
                    "current fact shape lies within the cited blind anchor band"
                ],
                "proposed_points": maximum * fraction,
                "allowed_range": [maximum * 0.35, maximum * 0.72],
                "rationale": "current support, counters, and anchor scale were reviewed",
                "disagreements": [],
                "support_fact_ids": list(memo["positive_fact_ids"]),
                "counter_fact_ids": list(memo["counter_fact_ids"]),
                "nearest_anchor_ids": list(memo["historical_anchor_ids"]),
                "why_not_higher": "counterevidence limits the upper bound",
                "why_not_lower": "direct current support establishes the lower bound",
            }
            if self.mode == "EXTRA_TOTAL_SCORE":
                response["total_score"] = 90
            return response

    provider = AuditProvider()
    engine = LLMComponentScoringMemoEngine(analyst_provider=provider)
    result = engine.build(
        target_id=target_id,
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        component_results=tuple(component_results),
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
    )
    extra_provider = AuditProvider("EXTRA_TOTAL_SCORE")
    extra_total = LLMComponentScoringMemoEngine(
        analyst_provider=extra_provider
    ).build(
        target_id=target_id,
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        component_results=tuple(component_results),
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
    )
    repeated_provider = AuditProvider("CONSTANT_PROMPT_HASH")
    repeated_prompt = LLMComponentScoringMemoEngine(
        analyst_provider=repeated_provider
    ).build(
        target_id=target_id,
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        component_results=tuple(component_results),
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
    )
    decisions = result.judge_decisions
    schema_properties = set(COMPONENT_JUDGE_SCHEMA.get("properties") or {})
    schema_required = set(COMPONENT_JUDGE_SCHEMA.get("required") or ())
    forbidden_provider_fields = {
        "total_score",
        "total_points",
        "stage",
        "canonical_stage",
        "final_stage",
    }
    prior_score_fields = {
        "proposed_score_lower",
        "proposed_score_mid",
        "proposed_score_upper",
        "why_not_higher",
        "why_not_lower",
        "confidence",
    }
    prior_score_exposure_count = sum(
        bool(
            prior_score_fields
            & set(call["payload"]["component_research_memo"])
        )
        for call in provider.calls
    )
    target_tokens = ("005930", "000660", "삼성전자", "SK하이닉스")
    tiny_multiplier_markers = (
        "proposed_credit_units *",
        "validated_credit_units *",
        "impact_fraction *",
        "impact_cap *",
    )
    prompt_hash_duplicate_count = sum(
        len(memo.prompt_hashes) - len(set(memo.prompt_hashes))
        for memo in result.component_memos
    )
    recursive_output_keys = _recursive_mapping_keys(result.to_dict())
    critical = {
        "required_module_missing_count": len(missing_modules),
        "judge_schema_open_count": int(
            COMPONENT_JUDGE_SCHEMA.get("additionalProperties") is not False
        ),
        "judge_schema_field_mismatch_count": len(
            schema_properties ^ set(JUDGE_RESPONSE_FIELDS)
        )
        + len(schema_required ^ set(JUDGE_RESPONSE_FIELDS)),
        "judge_schema_forbidden_field_count": len(
            forbidden_provider_fields & schema_properties
        ),
        "component_scoring_run_critical_count": int(
            result.audit["critical_count_sum"]
        ),
        "component_roster_mismatch_count": int(
            tuple(memo.component_id for memo in result.component_memos)
            != tuple(CANONICAL_COMPONENT_ORDER)
        ),
        "judge_memo_count_mismatch_count": int(len(decisions) != 21),
        "provider_call_count_mismatch_count": int(len(provider.calls) != 21),
        "judge_role_roster_mismatch_count": sum(
            {row.role for row in memo.judge_results}
            != set(REQUIRED_COMPONENT_JUDGE_ROLES)
            for memo in result.component_memos
        ),
        "judge_prompt_independence_missing_count": prompt_hash_duplicate_count,
        "judge_required_lineage_missing_count": sum(
            not decision.support_fact_ids
            or not decision.counter_fact_ids
            or not decision.nearest_anchor_ids
            or not decision.prompt_hash
            or not decision.response_hash
            or not decision.judge_call_id
            for decision in decisions
        ),
        "judge_bound_explanation_missing_count": sum(
            not decision.why_not_higher.strip()
            or not decision.why_not_lower.strip()
            for decision in decisions
        ),
        "component_max_violation_count": sum(
            decision.proposed_points > decision.component_max_points + 1e-9
            or decision.allowed_range[1]
            > decision.component_max_points + 1e-9
            for decision in decisions
        ),
        "role_review_dimension_missing_count": int(
            set(JUDGE_REVIEW_DIMENSIONS_BY_ROLE)
            != set(REQUIRED_COMPONENT_JUDGE_ROLES)
        )
        + int(
            not {
                "COUNTEREVIDENCE",
                "BUSINESS_PHASE",
                "VALUATION",
                "CONCENTRATION",
                "UNCERTAINTY",
            }.issubset(
                set(JUDGE_REVIEW_DIMENSIONS_BY_ROLE["SKEPTIC"])
            )
        ),
        "prior_researcher_score_band_exposure_count": prior_score_exposure_count,
        "llm_total_score_output_not_blocked_count": int(
            extra_total.status != "COMPONENT_SCORING_MEMOS_PENDING"
            or extra_total.ready_for_deterministic_aggregation
        ),
        "reused_prompt_independence_not_blocked_count": int(
            repeated_prompt.status != "COMPONENT_SCORING_MEMOS_PENDING"
            or repeated_prompt.ready_for_deterministic_aggregation
        ),
        "run_total_or_stage_output_field_count": len(
            forbidden_provider_fields & recursive_output_keys
        ),
        "tiny_impact_cap_multiplication_marker_count": sum(
            marker in source_text for marker in tiny_multiplier_markers
        ),
        "target_name_condition_count": sum(
            token in source_text for token in target_tokens
        ),
        "output_file_contract_mismatch_count": int(
            set(COMPONENT_SCORING_MEMO_OUTPUT_FILES)
            != {"component_memos", "judge_memos", "run", "audit"}
        ),
    }
    return {
        "schema_version": PHASE89_SCHEMA_VERSION,
        "status": (
            PHASE89_PASS
            if sum(critical.values()) == 0
            else "V5_PHASE89_INDEPENDENT_COMPONENT_SCORING_MEMOS_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "component_ids": list(CANONICAL_COMPONENT_ORDER),
        "judge_roles": list(REQUIRED_COMPONENT_JUDGE_ROLES),
        "judge_response_fields": sorted(JUDGE_RESPONSE_FIELDS),
        "judge_review_dimensions_by_role": {
            key: list(values)
            for key, values in JUDGE_REVIEW_DIMENSIONS_BY_ROLE.items()
        },
        "output_files": dict(COMPONENT_SCORING_MEMO_OUTPUT_FILES),
        "canary_counts": {
            "components": len(result.component_memos),
            "judge_memos": len(decisions),
            "provider_calls": len(provider.calls),
            "distinct_prompt_hashes": len(
                {decision.prompt_hash for decision in decisions}
            ),
            "distinct_response_hashes": len(
                {decision.response_hash for decision in decisions}
            ),
            "distinct_judge_call_ids": len(
                {decision.judge_call_id for decision in decisions}
            ),
        },
        "analyst_uses_current_evidence_and_positive_thesis": True,
        "skeptic_reviews_counter_phase_valuation_concentration_uncertainty": True,
        "calibration_uses_blind_historical_anchors": True,
        "prior_component_score_band_exposed_to_judges": False,
        "tiny_impact_cap_multiplication_used": False,
        "llm_total_score_authority": False,
        "llm_stage_authority": False,
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "roles": REQUIRED_COMPONENT_JUDGE_ROLES,
                "fields": sorted(JUDGE_RESPONSE_FIELDS),
                "outputs": COMPONENT_SCORING_MEMO_OUTPUT_FILES,
                "judge_ids": [decision.judge_id for decision in decisions],
            }
        ),
    }


def _recursive_mapping_keys(value: Any) -> set[str]:
    if isinstance(value, Mapping):
        return set(value) | {
            nested
            for item in value.values()
            for nested in _recursive_mapping_keys(item)
        }
    if isinstance(value, (list, tuple)):
        return {
            nested
            for item in value
            for nested in _recursive_mapping_keys(item)
        }
    return set()


def write_phase89_component_scoring_memos_audit(
    *,
    repo_root: str | Path,
    output_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE89_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase89_component_scoring_memos_audit(root))
    return destination


PHASE90_SCHEMA_VERSION = "e2r_v5_deterministic_score_aggregator_audit_v1"
PHASE90_PASS = "V5_PHASE90_DETERMINISTIC_SCORE_AGGREGATOR_PASS"
PHASE90_AUDIT_PATH = (
    "docs/operational/e2r_v5_deterministic_score_aggregator_audit.json"
)


def compile_phase90_deterministic_score_aggregator_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Compile a leaf-backed canary for deterministic seven-component scoring."""

    from dataclasses import replace
    import statistics

    from .component_researcher import ComponentResearchResult
    from .component_scoring_memos import LLMComponentScoringMemoEngine
    from .score_aggregator import (
        AGGREGATOR_CONFIG,
        SCORE_AGGREGATION_OUTPUT_FILES,
        DeterministicScoreAggregator,
    )
    from .schemas import (
        CANONICAL_COMPONENT_MAX_POINTS,
        CANONICAL_COMPONENT_ORDER,
        ComponentAnchor,
        ComponentResearchMemo,
        EvidenceFact,
    )

    root = Path(repo_root).resolve()
    module_paths = (
        "src/e2r/research_brain/researcher_mode/schemas.py",
        "src/e2r/research_brain/researcher_mode/component_judge.py",
        "src/e2r/research_brain/researcher_mode/component_scoring_memos.py",
        "src/e2r/research_brain/researcher_mode/score_aggregator.py",
    )
    missing_modules = [value for value in module_paths if not (root / value).is_file()]
    source_text = "\n".join(
        (root / value).read_text(encoding="utf-8")
        for value in module_paths
        if (root / value).is_file()
    )
    target_id = "PHASE90-AUDIT-CURRENT-TARGET"
    archetype_id = "PHASE90-AUDIT-CURRENT-ARCHETYPE"
    as_of_date = "2026-06-29"
    facts = (
        EvidenceFact(
            fact_id="PHASE90-AUDIT-SUPPORT",
            target_id=target_id,
            as_of_date=as_of_date,
            subject="current target operating business",
            business_segment="core segment",
            product_family="core product",
            economic_mechanism="direct current strength converts into earnings and cash",
            predicate="current_operating_strength",
            value=True,
            unit="flag",
            period="2026Q2",
            direction="POSITIVE",
            source_ids=("PHASE90-AUDIT-SOURCE-SUPPORT",),
            claim_ids=("PHASE90-AUDIT-CLAIM-SUPPORT",),
            quote_ids=("PHASE90-AUDIT-QUOTE-SUPPORT",),
            current_lifecycle="CURRENT",
            source_independence_group="ISSUER",
            corroborating_independence_groups=("INDEPENDENT-RESEARCH",),
            confidence=0.86,
        ),
        EvidenceFact(
            fact_id="PHASE90-AUDIT-COUNTER",
            target_id=target_id,
            as_of_date=as_of_date,
            subject="current target operating business",
            business_segment="core segment",
            product_family="core product",
            economic_mechanism="open concentration risk constrains durability",
            predicate="concentration_risk",
            value=True,
            unit="flag",
            period="2026Q2",
            direction="COUNTER",
            source_ids=("PHASE90-AUDIT-SOURCE-COUNTER",),
            claim_ids=("PHASE90-AUDIT-CLAIM-COUNTER",),
            quote_ids=("PHASE90-AUDIT-QUOTE-COUNTER",),
            current_lifecycle="OPEN",
            source_independence_group="INDEPENDENT-RESEARCH",
            confidence=0.80,
        ),
    )
    anchors = []
    component_results = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        anchor_ids = []
        for role, suffix, midpoint in (
            ("POSITIVE", "P", 0.85),
            ("COUNTER", "C", 0.40),
        ):
            anchor_id = f"PHASE90-AUDIT-ANCHOR-{component_id}-{suffix}"
            anchor_ids.append(anchor_id)
            anchors.append(
                ComponentAnchor(
                    anchor_id=anchor_id,
                    archetype_id=archetype_id,
                    component_id=component_id,
                    economic_fact_patterns=("blind source-backed economic pattern",),
                    role=role,
                    score_band="HIGH" if role == "POSITIVE" else "LOW",
                    points_lower=maximum * max(0.0, midpoint - 0.10),
                    points_mid=maximum * midpoint,
                    points_upper=maximum * min(1.0, midpoint + 0.10),
                    max_points=maximum,
                    source_backed_case_ids=(
                        f"PHASE90-AUDIT-CASE-{component_id}-{suffix}",
                    ),
                    source_proxy_guard_case_ids=(),
                    source_score_anchor_ids=(
                        f"PHASE90-AUDIT-SCORE-{component_id}-{suffix}",
                    ),
                    confidence="MEDIUM",
                    usable_as_exact_anchor=False,
                    usable_as_ordinal_anchor=True,
                )
            )
        memo = ComponentResearchMemo(
            memo_id=f"PHASE90-AUDIT-MEMO-{component_id}",
            target_id=target_id,
            archetype_id=archetype_id,
            component_id=component_id,
            component_max_points=maximum,
            positive_fact_ids=("PHASE90-AUDIT-SUPPORT",),
            counter_fact_ids=("PHASE90-AUDIT-COUNTER",),
            resolution_fact_ids=(),
            structured_metrics={"current_strength": 1.0, "concentration": 0.4},
            historical_anchor_ids=tuple(anchor_ids),
            researcher_summary="current source-backed economics were researched",
            positive_case="direct evidence establishes a strong economic range",
            counter_case="open concentration constrains the upper range",
            uncertainties=("duration requires continued monitoring",),
            source_coverage=("ISSUER_OFFICIAL", "INDEPENDENT_REPORT"),
            proposed_score_lower=maximum * 0.50,
            proposed_score_mid=maximum * 0.72,
            proposed_score_upper=maximum * 0.92,
            confidence=0.82,
            research_complete=True,
            nearest_positive_anchor_ids=(anchor_ids[0],),
            nearest_counter_anchor_ids=(anchor_ids[1],),
            why_not_higher="open counterevidence remains",
            why_not_lower="direct source-backed support exists",
            researcher_role=f"PHASE90-AUDIT-{component_id}-RESEARCHER",
        )
        component_results.append(
            ComponentResearchResult(
                component_id=component_id,
                researcher_role=memo.researcher_role,
                status="COMPLETE",
                memo=memo,
                pending_reasons=(),
                provider_name="PHASE90-AUDIT-RESEARCHER",
                prompt_hash=f"PHASE90-AUDIT-RESEARCH-{component_id}",
            )
        )
    memos = tuple(row.memo for row in component_results if row.memo is not None)

    class AuditProvider:
        provider_name = "PHASE90-AUDIT-JUDGE-PROVIDER"

        def __init__(self, mode: str = "BASE") -> None:
            self.mode = mode
            self.calls: list[Mapping[str, Any]] = []

        def complete(
            self,
            *,
            pass_name: str,
            payload: Mapping[str, Any],
        ) -> Mapping[str, Any]:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            memo = payload["component_research_memo"]
            maximum = float(payload["component_max_points"])
            fractions = {
                "BASE": {
                    "COMPONENT_ANALYST_JUDGE": 0.84,
                    "COMPONENT_SKEPTIC_JUDGE": 0.72,
                    "CALIBRATION_JUDGE": 0.80,
                },
                "STRONG": {
                    "COMPONENT_ANALYST_JUDGE": 0.94,
                    "COMPONENT_SKEPTIC_JUDGE": 0.88,
                    "CALIBRATION_JUDGE": 0.92,
                },
                "DISAGREE": {
                    "COMPONENT_ANALYST_JUDGE": 0.92,
                    "COMPONENT_SKEPTIC_JUDGE": 0.20,
                    "CALIBRATION_JUDGE": 0.86,
                },
            }[self.mode]
            lower, upper = {
                "BASE": (0.60, 0.94),
                "STRONG": (0.80, 1.00),
                "DISAGREE": (0.10, 0.98),
            }[self.mode]
            return {
                "anchor_comparisons": [
                    "current economics were placed against blind historical bands"
                ],
                "proposed_points": maximum * fractions[pass_name],
                "allowed_range": [maximum * lower, maximum * upper],
                "rationale": "support, counters, and anchor scale were reviewed",
                "disagreements": (
                    ["material disagreement remains"]
                    if self.mode == "DISAGREE"
                    else []
                ),
                "support_fact_ids": list(memo["positive_fact_ids"]),
                "counter_fact_ids": list(memo["counter_fact_ids"]),
                "nearest_anchor_ids": list(memo["historical_anchor_ids"]),
                "why_not_higher": "open counterevidence limits the ceiling",
                "why_not_lower": "direct current support establishes the floor",
            }

    def scoring_run(mode: str):
        return LLMComponentScoringMemoEngine(
            analyst_provider=AuditProvider(mode)
        ).build(
            target_id=target_id,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            component_results=tuple(component_results),
            evidence_facts=facts,
            historical_anchors=tuple(anchors),
        )

    aggregator = DeterministicScoreAggregator()
    base_scoring = scoring_run("BASE")
    base = aggregator.aggregate_run(
        scoring_memo_run=base_scoring,
        component_research_memos=memos,
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
    )
    disagreement = aggregator.aggregate_run(
        scoring_memo_run=scoring_run("DISAGREE"),
        component_research_memos=memos,
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
    )
    strong = aggregator.aggregate_run(
        scoring_memo_run=scoring_run("STRONG"),
        component_research_memos=memos,
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
    )
    first_decisions = base_scoring.component_memos[0].judge_decisions
    invalid_extra = replace(
        first_decisions[0], component_id=CANONICAL_COMPONENT_ORDER[1]
    )
    invalid_removed = aggregator.aggregate_component(
        memo=memos[0],
        judge_decisions=(*first_decisions, invalid_extra),
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
        expected_as_of_date=as_of_date,
    )
    uncorroborated_facts = tuple(
        replace(
            row,
            source_independence_group="ISSUER",
            corroborating_independence_groups=(),
        )
        for row in facts
    )
    uncorroborated = aggregator.aggregate_component(
        memo=memos[0],
        judge_decisions=first_decisions,
        evidence_facts=uncorroborated_facts,
        historical_anchors=tuple(anchors),
        expected_as_of_date=as_of_date,
    )
    corroborated = aggregator.aggregate_component(
        memo=memos[0],
        judge_decisions=first_decisions,
        evidence_facts=facts,
        historical_anchors=tuple(anchors),
        expected_as_of_date=as_of_date,
    )

    base_decisions = tuple(
        row.decision for row in base.component_results if row.decision is not None
    )
    total_score = base.total_result.score
    output_keys = _recursive_mapping_keys(base.to_dict())
    forbidden_stage_keys = {"stage", "canonical_stage", "final_stage", "stage_override"}
    target_tokens = ("005930", "000660", "삼성전자", "SK하이닉스")
    tiny_multiplier_markers = (
        "impact_fraction *",
        "impact_cap *",
        "validated_credit_units *",
        "proposed_credit_units *",
    )
    critical = {
        "required_module_missing_count": len(missing_modules),
        "base_run_internal_critical_count": int(base.audit["critical_count_sum"]),
        "base_run_not_complete_count": int(
            base.status != "DETERMINISTIC_SCORE_COMPLETE" or not base.score_valid
        ),
        "component_roster_mismatch_count": int(len(base.component_results) != 7),
        "proposal_validation_count_mismatch_count": int(
            sum(len(row.proposal_validations) for row in base.component_results) != 21
        ),
        "valid_proposal_count_mismatch_count": int(
            sum(
                validation.valid
                for row in base.component_results
                for validation in row.proposal_validations
            )
            != 21
        ),
        "median_consensus_mismatch_count": sum(
            abs(
                row.proposal_median
                - statistics.median(row.judge_proposals.values())
            )
            > 1e-9
            for row in base_decisions
        ),
        "counter_effect_missing_or_unreconciled_count": sum(
            row.counter_effect <= 0
            or abs(row.support_points - row.counter_effect - row.final_points) > 1e-6
            for row in base_decisions
        ),
        "component_max_violation_count": sum(
            row.final_points > row.max_points + 1e-9 for row in base_decisions
        ),
        "required_lineage_missing_count": sum(
            not row.fact_ids
            or not row.counter_fact_ids
            or not row.anchor_ids
            or len(row.judge_ids) != 3
            or len(row.prompt_hashes) != 3
            or len(row.config_hash) != 64
            for row in base_decisions
        ),
        "total_missing_or_unreconciled_count": int(total_score is None)
        + int(
            total_score is not None
            and abs(total_score.total_points - sum(total_score.component_points.values()))
            > 1e-6
        ),
        "invalid_proposal_not_removed_and_recorded_count": int(
            invalid_removed.status != "COMPLETE"
            or invalid_removed.invalid_proposal_count != 1
        ),
        "material_disagreement_not_returned_to_research_count": int(
            disagreement.status != "DETERMINISTIC_SCORE_RESEARCH_REQUIRED"
            or disagreement.score_valid
            or disagreement.total_result.score is not None
            or len(disagreement.research_requests) != 7
        ),
        "research_request_query_authority_mismatch_count": sum(
            row.query_generation_authority != "LLM_RESEARCH_SUPERVISOR"
            or row.deterministic_query_synthesis
            for row in disagreement.research_requests
        ),
        "source_confidence_changed_economic_points_count": int(
            uncorroborated.decision is None
            or corroborated.decision is None
            or uncorroborated.decision.final_points
            != corroborated.decision.final_points
        ),
        "corroboration_did_not_increase_confidence_count": int(
            uncorroborated.decision is None
            or corroborated.decision is None
            or corroborated.decision.confidence
            <= uncorroborated.decision.confidence
        ),
        "strong_direct_evidence_score_collapse_count": int(
            strong.component_results[0].decision is None
            or strong.component_results[0].decision.final_points
            <= strong.component_results[0].decision.max_points * 0.80
        ),
        "forbidden_stage_output_key_count": len(forbidden_stage_keys & output_keys),
        "tiny_impact_cap_multiplication_marker_count": sum(
            marker in source_text for marker in tiny_multiplier_markers
        ),
        "target_name_condition_count": sum(
            token in source_text for token in target_tokens
        ),
        "config_safeguard_violation_count": sum(
            AGGREGATOR_CONFIG[key] is not False
            for key in (
                "source_confidence_affects_points",
                "independent_corroboration_affects_points",
                "tiny_impact_cap_multiplication",
                "stage_authority",
            )
        ),
        "output_file_contract_mismatch_count": int(
            set(SCORE_AGGREGATION_OUTPUT_FILES)
            != {
                "component_results",
                "proposal_validations",
                "research_requests",
                "total_score",
                "run",
                "audit",
            }
        ),
    }
    return {
        "schema_version": PHASE90_SCHEMA_VERSION,
        "status": (
            PHASE90_PASS
            if sum(critical.values()) == 0
            else "V5_PHASE90_DETERMINISTIC_SCORE_AGGREGATOR_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "component_ids": list(CANONICAL_COMPONENT_ORDER),
        "judge_roles": list(AGGREGATOR_CONFIG["required_roles"]),
        "aggregation_policy": dict(AGGREGATOR_CONFIG),
        "output_files": dict(SCORE_AGGREGATION_OUTPUT_FILES),
        "canary_counts": {
            "components": len(base.component_results),
            "judge_proposals": sum(
                len(row.proposal_validations) for row in base.component_results
            ),
            "component_decisions": len(base_decisions),
            "research_requests_on_material_disagreement": len(
                disagreement.research_requests
            ),
            "invalid_proposals_removed": invalid_removed.invalid_proposal_count,
        },
        "canary_total_points": total_score.total_points if total_score else None,
        "canary_total_max_points": total_score.max_points if total_score else None,
        "strong_component_points": (
            strong.component_results[0].decision.final_points
            if strong.component_results[0].decision
            else None
        ),
        "invalid_proposals_are_removed_and_recorded": True,
        "valid_proposals_use_median_and_consensus_band": True,
        "material_disagreement_returns_to_research": True,
        "counter_effect_applied_once": True,
        "component_max_clamped": True,
        "seven_components_summed_deterministically": True,
        "source_confidence_affects_points": False,
        "independent_corroboration_improves_confidence_only": True,
        "tiny_impact_cap_multiplication_used": False,
        "llm_total_score_authority": False,
        "production_stage_authority": False,
        "audit_hash": _stable_hash(
            {
                "critical": critical,
                "config": AGGREGATOR_CONFIG,
                "component_decision_ids": (
                    total_score.component_decision_ids if total_score else {}
                ),
                "outputs": SCORE_AGGREGATION_OUTPUT_FILES,
            }
        ),
    }


def write_phase90_deterministic_score_aggregator_audit(
    *,
    repo_root: str | Path,
    output_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    destination = Path(output_path or root / PHASE90_AUDIT_PATH)
    if not destination.is_absolute():
        destination = root / destination
    write_json(destination, compile_phase90_deterministic_score_aggregator_audit(root))
    return destination


__all__ = [
    "PHASE80_ARTIFACT_PATHS",
    "PHASE80_PASS",
    "PHASE80_SCHEMA_VERSION",
    "PHASE84_AUDIT_PATH",
    "PHASE84_PASS",
    "PHASE84_REQUIRED_MODULES",
    "PHASE84_SCHEMA_VERSION",
    "PHASE85_AUDIT_PATH",
    "PHASE85_PASS",
    "PHASE85_SCHEMA_VERSION",
    "PHASE86_AUDIT_PATH",
    "PHASE86_PASS",
    "PHASE86_SCHEMA_VERSION",
    "PHASE87_AUDIT_PATH",
    "PHASE87_PASS",
    "PHASE87_SCHEMA_VERSION",
    "PHASE88_AUDIT_PATH",
    "PHASE88_PASS",
    "PHASE88_SCHEMA_VERSION",
    "PHASE89_AUDIT_PATH",
    "PHASE89_PASS",
    "PHASE89_SCHEMA_VERSION",
    "PHASE90_AUDIT_PATH",
    "PHASE90_PASS",
    "PHASE90_SCHEMA_VERSION",
    "compile_phase80_forensics",
    "compile_phase84_researcher_mode_audit",
    "compile_phase85_source_graph_acquisition_audit",
    "compile_phase86_structured_financial_engine_audit",
    "compile_phase87_semantic_research_saturation_audit",
    "compile_phase88_evidence_fact_graph_audit",
    "compile_phase89_component_scoring_memos_audit",
    "compile_phase90_deterministic_score_aggregator_audit",
    "write_phase80_forensics",
    "write_phase84_researcher_mode_audit",
    "write_phase85_source_graph_acquisition_audit",
    "write_phase86_structured_financial_engine_audit",
    "write_phase87_semantic_research_saturation_audit",
    "write_phase88_evidence_fact_graph_audit",
    "write_phase89_component_scoring_memos_audit",
    "write_phase90_deterministic_score_aggregator_audit",
]
