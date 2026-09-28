$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host "Installing pinned dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host "Installing project in editable mode..."
python -m pip install -e .

Write-Host "Running a quick verification..."
python -m pytest -q

Write-Host ""
Write-Host "Setup complete. The project environment is ready."
Write-Host "Use: pytest"
Write-Host "Use: python scripts/memory_test.py"
