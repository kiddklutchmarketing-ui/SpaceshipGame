<#
build_exe.ps1
PowerShell helper to build a single-file executable using PyInstaller.

Usage (from repo root PowerShell):
  .\build_exe.ps1

Notes:
 - This will attempt to install PyInstaller into the repo venv if found.
 - Asset files (assets/) are added with --add-data; adjust paths if you move assets.
#>

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $RepoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $venvPython)) {
    $venvPython = 'python'
}

Write-Output "Using Python: $venvPython"

# Ensure PyInstaller is installed in the chosen interpreter
Start-Process -FilePath $venvPython -ArgumentList '-m','pip','install','pyinstaller','--upgrade' -NoNewWindow -Wait

$entry = Join-Path $RepoRoot 'PythonProject\Spaceship Game Project 2.py'
if (-not (Test-Path $entry)) {
    Write-Error "Game entry not found: $entry"
    exit 2
}

# Build (adjust --add-data as needed for extra assets)
Start-Process -FilePath $venvPython -ArgumentList '-m','PyInstaller','--noconfirm','--onefile','--name','SpaceshipGame','--add-data','assets;assets',"$entry" -NoNewWindow -Wait

Write-Output "Build complete. Check the dist folder for SpaceshipGame.exe"
