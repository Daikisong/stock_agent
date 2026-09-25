param(
    [string]$ConfigPath = "configs/e2r_pro_first_local.yaml",
    [int]$RemoteDebuggingPort = 9222
)

$ErrorActionPreference = "Stop"
$RepoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot ".."))
$ResolvedConfig = Join-Path $RepoRoot $ConfigPath
$ExampleConfig = Join-Path $RepoRoot "configs/e2r_pro_first_local.example.yaml"

if (-not (Test-Path $ResolvedConfig)) {
    Copy-Item -LiteralPath $ExampleConfig -Destination $ResolvedConfig
    Write-Host "로컬 설정을 생성했습니다: $ResolvedConfig"
}

$cdpAvailable = $false
try {
    Invoke-RestMethod -Uri "http://127.0.0.1:$RemoteDebuggingPort/json/version" -TimeoutSec 2 | Out-Null
    $cdpAvailable = $true
} catch {
    $cdpAvailable = $false
}

if (-not $cdpAvailable) {
    & (Join-Path $PSScriptRoot "start_e2r_pro_chrome.ps1") -RemoteDebuggingPort $RemoteDebuggingPort
    Write-Host "Chrome에서 ChatGPT 로그인이 필요하면 직접 완료하세요. 스택은 자동 로그인하지 않습니다."
}

$env:PYTHONPATH = (Join-Path $RepoRoot "src")
Set-Location $RepoRoot
python -m e2r.cli.run_e2r_pro_first_stack --config $ResolvedConfig --repo-root $RepoRoot
