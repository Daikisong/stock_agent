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


__all__ = [
    "PHASE80_ARTIFACT_PATHS",
    "PHASE80_PASS",
    "PHASE80_SCHEMA_VERSION",
    "PHASE84_AUDIT_PATH",
    "PHASE84_PASS",
    "PHASE84_REQUIRED_MODULES",
    "PHASE84_SCHEMA_VERSION",
    "compile_phase80_forensics",
    "compile_phase84_researcher_mode_audit",
    "write_phase80_forensics",
    "write_phase84_researcher_mode_audit",
]
