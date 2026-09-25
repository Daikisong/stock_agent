param(
    [int]$RemoteDebuggingPort = 9222,
    [string]$ProfileDirectory = "$env:LOCALAPPDATA\E2R\ChromeProfile",
    [string]$ChatGPTUrl = "https://chatgpt.com/"
)

$ErrorActionPreference = "Stop"

$chromeCandidates = @(
    "$env:PROGRAMFILES\Google\Chrome\Application\chrome.exe",
    "${env:PROGRAMFILES(X86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)
$chrome = $chromeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $chrome) {
    throw "Google Chrome 실행 파일을 찾지 못했습니다."
}

$defaultChromeProfile = [System.IO.Path]::GetFullPath("$env:LOCALAPPDATA\Google\Chrome\User Data")
$resolvedProfile = [System.IO.Path]::GetFullPath($ProfileDirectory)
if ($resolvedProfile -eq $defaultChromeProfile) {
    throw "기본 Chrome profile 대신 E2R 전용 profile을 지정하세요."
}

New-Item -ItemType Directory -Force -Path $resolvedProfile | Out-Null
$arguments = @(
    "--remote-debugging-port=$RemoteDebuggingPort",
    "--remote-debugging-address=127.0.0.1",
    "--remote-allow-origins=http://127.0.0.1,http://localhost,http://127.0.0.1:$RemoteDebuggingPort,http://localhost:$RemoteDebuggingPort",
    "--user-data-dir=$resolvedProfile",
    "--no-first-run",
    $ChatGPTUrl
)

Start-Process -FilePath $chrome -ArgumentList $arguments
Write-Host "E2R 전용 Chrome을 열었습니다. 로그인은 사용자가 직접 수행해야 합니다."
Write-Host "CDP: http://127.0.0.1:$RemoteDebuggingPort"
