<#
run_game.ps1
One-command PowerShell launcher for the game.

Usage:
  Right-click -> Run with PowerShell, or from PowerShell:
    .\run_game.ps1

This script prefers a repo-local venv (.venv or venv) if present, otherwise
falls back to the system `python` on PATH.
#>

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

# look for common venv locations
$venvCandidates = @(Join-Path $RepoRoot '.venv\Scripts\python.exe', Join-Path $RepoRoot 'venv\Scripts\python.exe')

$python = 'python'
foreach ($cand in $venvCandidates) {
    if (Test-Path $cand) {
        $python = $cand
        break
    }
}

$game = Join-Path $RepoRoot 'run_game.py'
if (-not (Test-Path $game)) {
    Write-Error "Game launcher not found: $game"
    exit 2
}

Write-Output "Launching game with: $python"
& $python $game
