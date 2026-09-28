"""Local dashboard pages and API over the durable Pro-first ledger."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hmac
from html import escape
import inspect
import ipaddress
import json
from pathlib import Path
import secrets
from typing import Any, Awaitable, Callable, Mapping

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse

from ..approval import ApprovalGrant, ProApprovalService
from ..job_store import ApprovalInvalid, ProFirstJobStore, RecordNotFound
from ..models import ProResearchJob
from ..publication import ProResultPublisher


Action = Callable[..., Any | Awaitable[Any]]


@dataclass(frozen=True)
class LocalDashboardConfig:
    runtime_root: Path
    host: str = "127.0.0.1"
    port: int = 8765
    allowed_origins: tuple[str, ...] = ()
    local_token: str | None = None

    def __post_init__(self) -> None:
        if not _is_loopback(self.host):
            raise ValueError("Pro-first dashboard must bind to a loopback address")
        if not 1 <= int(self.port) <= 65_535:
            raise ValueError("dashboard port is outside the TCP range")
        object.__setattr__(self, "runtime_root", Path(self.runtime_root).resolve())
        if self.local_token is not None and len(self.local_token) < 24:
            raise ValueError("local dashboard token must have at least 24 characters")

    @property
    def origins(self) -> frozenset[str]:
        defaults = {
            f"http://127.0.0.1:{self.port}",
            f"http://localhost:{self.port}",
            f"http://[::1]:{self.port}",
        }
        return frozenset(defaults | set(self.allowed_origins))


@dataclass(frozen=True)
class DashboardActions:
    run_scan: Action | None = None
    prepare_job: Action | None = None
    submit_clarification: Action | None = None


def create_pro_first_dashboard_app(
    *,
    store: ProFirstJobStore,
    config: LocalDashboardConfig,
    actions: DashboardActions | None = None,
    approval_service: ProApprovalService | None = None,
    publisher: ProResultPublisher | None = None,
) -> FastAPI:
    actions = actions or DashboardActions()
    approval_service = approval_service or ProApprovalService(store)
    publisher = publisher or ProResultPublisher(store)
    local_token = config.local_token or secrets.token_urlsafe(32)
    app = FastAPI(title="E2R Pro-first Local Dashboard", version="1.0")
    app.state.local_token = local_token
    app.state.dashboard_config = config

    @app.get("/api/health")
    async def health() -> Mapping[str, Any]:
        return {
            "status": "ok",
            "service": "e2r-pro-first-dashboard",
            "bind_host": config.host,
            "loopback_only": True,
            "database_ready": store.database_path.is_file(),
        }

    @app.get("/api/scans")
    async def scans() -> Mapping[str, Any]:
        rows = [asdict(row) for row in store.list_scan_runs()]
        return {"count": len(rows), "scans": rows}

    @app.post("/api/scans/run")
    async def run_scan(request: Request) -> Any:
        _require_mutation_security(request, token=local_token, config=config)
        if actions.run_scan is None:
            raise HTTPException(status_code=503, detail="scan handler is unavailable")
        body = await _request_json(request)
        return _jsonable(await _invoke(actions.run_scan, body))

    @app.get("/api/candidates")
    async def candidates() -> Mapping[str, Any]:
        rows = [asdict(row) for row in store.list_candidates()]
        return {"count": len(rows), "candidates": rows}

    @app.post("/api/candidates/{candidate_id}/create-job")
    async def create_job(candidate_id: str, request: Request) -> Mapping[str, Any]:
        _require_mutation_security(request, token=local_token, config=config)
        body = await _request_json(request)
        try:
            candidate = store.get_candidate(candidate_id)
            job = store.create_job(
                candidate.candidate_id,
                priority=int(body.get("priority") or 0),
                archetype_ids=tuple(body.get("archetype_ids") or ()),
                actor="dashboard-user",
            )
        except RecordNotFound as error:
            raise HTTPException(status_code=404, detail=str(error)) from error
        return _public_job(job)

    @app.get("/api/jobs")
    async def jobs() -> Mapping[str, Any]:
        rows = [_public_job(job) for job in store.list_jobs()]
        return {"count": len(rows), "jobs": rows}

    @app.get("/api/jobs/{job_id}")
    async def job_detail(job_id: str) -> Mapping[str, Any]:
        try:
            return _job_detail(store, job_id)
        except RecordNotFound as error:
            raise HTTPException(status_code=404, detail=str(error)) from error

    @app.post("/api/jobs/{job_id}/prepare")
    async def prepare(job_id: str, request: Request) -> Any:
        _require_mutation_security(request, token=local_token, config=config)
        if actions.prepare_job is None:
            raise HTTPException(status_code=503, detail="prepare handler is unavailable")
        store.get_job(job_id)
        body = await _request_json(request)
        return _jsonable(await _invoke(actions.prepare_job, job_id, body))

    @app.post("/api/jobs/{job_id}/approve")
    async def approve(job_id: str, request: Request) -> Mapping[str, Any]:
        _require_mutation_security(request, token=local_token, config=config)
        body = await _request_json(request)
        action = str(body.get("action") or "issue")
        prompt_hash = str(body.get("prompt_hash") or "")
        try:
            if action == "issue":
                grant = approval_service.issue(
                    job_id,
                    prompt_hash=prompt_hash,
                    actor="dashboard-user",
                )
                return {
                    "status": "APPROVAL_NONCE_ISSUED",
                    "job_id": job_id,
                    "approval_nonce": grant.approval_nonce,
                    "expires_at": grant.expires_at,
                    "state_version": grant.state_version,
                }
            if action != "consume":
                raise HTTPException(status_code=422, detail="unknown approval action")
            job = store.get_job(job_id)
            raw_nonce = str(body.get("approval_nonce") or "")
            if not all(
                (
                    raw_nonce,
                    prompt_hash,
                    job.packet_hash,
                    job.browser_session_id,
                    job.approval_expires_at,
                )
            ):
                raise ApprovalInvalid("approval consumption payload is incomplete")
            approved = approval_service.approve(
                ApprovalGrant(
                    job_id=job_id,
                    approval_nonce=raw_nonce,
                    packet_hash=str(job.packet_hash),
                    prompt_hash=prompt_hash,
                    browser_session_id=str(job.browser_session_id),
                    expires_at=str(job.approval_expires_at),
                    state_version=job.state_version,
                ),
                actor="dashboard-user",
            )
            return {"status": "APPROVED", "job": _public_job(approved)}
        except (ApprovalInvalid, ValueError) as error:
            raise HTTPException(status_code=409, detail=str(error)) from error

    @app.post("/api/jobs/{job_id}/cancel")
    async def cancel(job_id: str, request: Request) -> Mapping[str, Any]:
        _require_mutation_security(request, token=local_token, config=config)
        body = await _request_json(request)
        try:
            job = store.cancel_job(
                job_id,
                reason=str(body.get("reason") or "USER_CANCELLED"),
            )
        except RecordNotFound as error:
            raise HTTPException(status_code=404, detail=str(error)) from error
        except ValueError as error:
            raise HTTPException(status_code=409, detail=str(error)) from error
        return {"status": "CANCELLED", "job": _public_job(job)}

    @app.post("/api/jobs/{job_id}/clarification")
    async def clarification(job_id: str, request: Request) -> Any:
        _require_mutation_security(request, token=local_token, config=config)
        if actions.submit_clarification is None:
            raise HTTPException(
                status_code=503,
                detail="clarification handler is unavailable",
            )
        store.get_job(job_id)
        body = await _request_json(request)
        answer = str(body.get("answer") or "").strip()
        if not answer:
            raise HTTPException(status_code=422, detail="clarification answer is required")
        return _jsonable(
            await _invoke(actions.submit_clarification, job_id, answer)
        )

    @app.get("/api/jobs/{job_id}/artifacts")
    async def artifacts(job_id: str) -> Mapping[str, Any]:
        try:
            rows = list(store.list_artifacts(job_id))
        except RecordNotFound as error:
            raise HTTPException(status_code=404, detail=str(error)) from error
        return {"count": len(rows), "artifacts": rows}

    @app.get("/api/results/{job_id}")
    async def result(job_id: str) -> Mapping[str, Any]:
        try:
            receipt = store.get_publication(job_id)
            if receipt is None:
                raise HTTPException(status_code=404, detail="result is not published")
            return dict(receipt.get("result") or {})
        except RecordNotFound as error:
            raise HTTPException(status_code=404, detail=str(error)) from error

    @app.get("/", response_class=HTMLResponse)
    async def home() -> str:
        job_rows = store.list_jobs(limit=100)
        scan_rows = store.list_scan_runs(limit=20)
        candidate_rows = store.list_candidates(limit=100)
        status_counts: dict[str, int] = {}
        for job in job_rows:
            status_counts[job.status] = status_counts.get(job.status, 0) + 1
        body = ["<h1>E2R Pro-first</h1>"]
        body.append("<h2>상태 요약</h2><ul>")
        for status, count in sorted(status_counts.items()):
            body.append(f"<li>{escape(status)}: {count}</li>")
        body.append("</ul><h2>최근 스캔</h2><ul>")
        for scan in scan_rows:
            body.append(
                f"<li>{escape(scan.as_of_date)} {escape(scan.scan_window)} "
                f"{escape(scan.status)}</li>"
            )
        body.append("</ul><h2>후보 큐</h2><ul>")
        for candidate in candidate_rows:
            body.append(
                f"<li>{escape(candidate.symbol)} {escape(candidate.company_name)} "
                f"{escape(candidate.research_mode)}</li>"
            )
        body.append("</ul><h2>승인 대기</h2><ul>")
        for job in job_rows:
            if job.status == "AWAITING_USER_APPROVAL":
                body.append(_job_list_item(job))
        body.append("</ul><h2>진행 중</h2><ul>")
        for job in job_rows:
            if job.status not in {"AWAITING_USER_APPROVAL", "FINAL", "BLOCKED", "CANCELLED"}:
                body.append(_job_list_item(job))
        body.append("</ul><h2>완료</h2><ul>")
        for job in job_rows:
            if job.status in {"FINAL", "BLOCKED", "CANCELLED"}:
                body.append(_job_list_item(job))
        body.append('</ul><p><a href="/settings">설정</a></p>')
        return _page("E2R Pro-first", "".join(body))

    @app.get("/jobs/{job_id}", response_class=HTMLResponse)
    async def job_page(job_id: str) -> str:
        try:
            detail = _job_detail(store, job_id)
        except RecordNotFound as error:
            raise HTTPException(status_code=404, detail=str(error)) from error
        rendered = escape(str(detail))
        controls = _job_controls(detail)
        return _page(
            f"E2R job {job_id}",
            f"<h1>{escape(job_id)}</h1>{controls}<pre>{rendered}</pre>",
        )

    @app.get("/settings", response_class=HTMLResponse)
    async def settings() -> str:
        body = (
            "<h1>설정</h1>"
            f"<p>Dashboard: {escape(config.host)}:{config.port}</p>"
            "<p>보안: loopback-only / startup token / same-origin</p>"
            "<p>Chrome 연결과 scheduler 설정은 로컬 config에서 관리합니다.</p>"
        )
        return _page("E2R Pro-first settings", body)

    app.state.publisher = publisher
    return app


def _job_detail(store: ProFirstJobStore, job_id: str) -> Mapping[str, Any]:
    job = store.get_job(job_id)
    publication = store.get_publication(job_id)
    return {
        "job": _public_job(job),
        "packet": store.get_packet_manifest(job_id),
        "browser": store.get_browser_session_state(job_id),
        "approval": {
            "nonce_issued": job.approval_nonce_hash is not None,
            "expires_at": job.approval_expires_at,
            "consumed_at": job.approval_consumed_at,
            "approved_at": job.approved_at,
        },
        "progress": [asdict(row) for row in store.list_events(job_id)],
        "source_verification": store.get_source_verification_receipt(job_id),
        "gap_decisions": list(store.get_gap_decisions(job_id)),
        "score": store.get_score_receipt(job_id),
        "stagecourt": store.get_stagecourt_receipt(job_id),
        "result": None if publication is None else publication.get("result"),
    }


def _public_job(job: ProResearchJob) -> Mapping[str, Any]:
    return {
        "job_id": job.job_id,
        "candidate_id": job.candidate_id,
        "symbol": job.symbol,
        "company_name": job.company_name,
        "as_of_date": job.as_of_date,
        "mode": job.mode,
        "status": job.status,
        "state_version": job.state_version,
        "priority": job.priority,
        "archetype_ids": list(job.archetype_ids),
        "packet_id": job.packet_id,
        "browser_session_id": job.browser_session_id,
        "conversation_id": job.conversation_id,
        "submit_count": job.submit_count,
        "capture_count": job.capture_count,
        "dossier_id": job.dossier_id,
        "score_receipt_id": job.score_receipt_id,
        "stagecourt_receipt_id": job.stagecourt_receipt_id,
        "created_at": job.created_at,
        "updated_at": job.updated_at,
        "approved_at": job.approved_at,
        "submitted_at": job.submitted_at,
        "research_completed_at": job.research_completed_at,
        "published_at": job.published_at,
        "last_error_class": job.last_error_class,
        "last_error_message": job.last_error_message,
    }


def _require_mutation_security(
    request: Request,
    *,
    token: str,
    config: LocalDashboardConfig,
) -> None:
    supplied = request.headers.get("x-e2r-local-token", "")
    if not supplied or not hmac.compare_digest(supplied, token):
        raise HTTPException(status_code=403, detail="local dashboard token is invalid")
    origin = request.headers.get("origin", "")
    if origin not in config.origins:
        raise HTTPException(status_code=403, detail="same-origin check failed")


async def _request_json(request: Request) -> Mapping[str, Any]:
    try:
        body = await request.json()
    except Exception as error:
        raise HTTPException(status_code=400, detail="JSON body is required") from error
    if not isinstance(body, Mapping):
        raise HTTPException(status_code=422, detail="JSON body must be an object")
    return body


async def _invoke(function: Action, *args: Any) -> Any:
    result = function(*args)
    return await result if inspect.isawaitable(result) else result


def _jsonable(value: Any) -> Any:
    if isinstance(value, ProResearchJob):
        return _public_job(value)
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if hasattr(value, "__dataclass_fields__"):
        return asdict(value)
    return value


def _is_loopback(host: str) -> bool:
    if host.casefold() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def _page(title: str, body: str) -> str:
    return (
        "<!doctype html><html lang=\"ko\"><head><meta charset=\"utf-8\">"
        f"<title>{escape(title)}</title>"
        "<style>body{font-family:system-ui;max-width:1100px;margin:2rem auto;"
        "padding:0 1rem;background:#f7f8fa;color:#182230}"
        "pre{white-space:pre-wrap;background:white;padding:1rem;border-radius:.5rem}"
        "a{color:#155eef}</style></head><body>"
        f"{body}</body></html>"
    )


def _job_list_item(job: ProResearchJob) -> str:
    return (
        f'<li><a href="/jobs/{escape(job.job_id)}">'
        f"{escape(job.symbol)} {escape(job.company_name)}</a> "
        f"{escape(job.status)}</li>"
    )


def _job_controls(detail: Mapping[str, Any]) -> str:
    job = detail.get("job") or {}
    browser = detail.get("browser") or {}
    browser_state = browser.get("state") or {}
    job_id_json = json.dumps(str(job.get("job_id") or ""))
    prompt_hash_json = json.dumps(str(browser_state.get("prompt_hash") or ""))
    status = str(job.get("status") or "")
    approval_controls = ""
    if status == "AWAITING_USER_APPROVAL":
        approval_controls = (
            '<button id="issue-approval">1. 승인 nonce 발급</button> '
            '<button id="consume-approval" disabled>2. 연구 시작 승인</button>'
        )
    clarification_controls = ""
    if status == "AWAITING_CLARIFICATION":
        clarification_controls = (
            '<p><textarea id="clarification-answer" rows="3" cols="70" '
            'placeholder="추가 설명"></textarea> '
            '<button id="send-clarification">설명 전송</button></p>'
        )
    return (
        '<section><label>로컬 토큰 <input id="local-token" type="password" '
        'autocomplete="off"></label> '
        f"{approval_controls}"
        '<button id="cancel-job">작업 취소</button>'
        f"{clarification_controls}"
        '<p id="action-status" role="status"></p></section>'
        "<script>"
        f"const jobId={job_id_json};const promptHash={prompt_hash_json};"
        "let approvalNonce=null;"
        "const statusNode=document.getElementById('action-status');"
        "async function post(path,body){"
        "const token=document.getElementById('local-token').value;"
        "const response=await fetch(path,{method:'POST',headers:{"
        "'Content-Type':'application/json','X-E2R-Local-Token':token},"
        "body:JSON.stringify(body)});const data=await response.json();"
        "if(!response.ok){throw new Error(data.detail||'request failed');}return data;}"
        "const issue=document.getElementById('issue-approval');if(issue){"
        "issue.addEventListener('click',async()=>{try{const data=await post("
        "`/api/jobs/${jobId}/approve`,{action:'issue',prompt_hash:promptHash});"
        "approvalNonce=data.approval_nonce;"
        "document.getElementById('consume-approval').disabled=false;"
        "statusNode.textContent='nonce가 발급됐습니다. 두 번째 승인 버튼을 눌러야 전송됩니다.';"
        "}catch(error){statusNode.textContent=error.message;}});}"
        "const consume=document.getElementById('consume-approval');if(consume){"
        "consume.addEventListener('click',async()=>{try{await post("
        "`/api/jobs/${jobId}/approve`,{action:'consume',prompt_hash:promptHash,"
        "approval_nonce:approvalNonce});approvalNonce=null;"
        "statusNode.textContent='승인 완료. Browser Worker가 exactly-once 전송을 이어갑니다.';"
        "consume.disabled=true;}catch(error){statusNode.textContent=error.message;}});}"
        "const cancel=document.getElementById('cancel-job');cancel.addEventListener("
        "'click',async()=>{if(!confirm('이 작업을 취소할까요?'))return;try{await post("
        "`/api/jobs/${jobId}/cancel`,{reason:'USER_CANCELLED_FROM_DASHBOARD'});"
        "statusNode.textContent='작업을 취소했습니다.';}catch(error){"
        "statusNode.textContent=error.message;}});"
        "const clarify=document.getElementById('send-clarification');if(clarify){"
        "clarify.addEventListener('click',async()=>{try{const answer="
        "document.getElementById('clarification-answer').value;await post("
        "`/api/jobs/${jobId}/clarification`,{answer});"
        "statusNode.textContent='추가 설명을 전송했습니다.';}catch(error){"
        "statusNode.textContent=error.message;}});}"
        "</script>"
    )


__all__ = [
    "DashboardActions",
    "LocalDashboardConfig",
    "create_pro_first_dashboard_app",
]
