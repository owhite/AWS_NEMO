#!/usr/bin/env bash
# setup_environment.sh
# Bootstraps a Python virtual environment and installs project dependencies.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo "==> Setting up virtual environment..."
python3 -m venv "$REPO_ROOT/venv"
# shellcheck disable=SC1091
source "$REPO_ROOT/venv/bin/activate"

echo "==> Upgrading pip..."
pip install --upgrade pip

echo "==> Installing dependencies..."
pip install -r "$REPO_ROOT/requirements.txt"

echo ""
echo "Setup complete. Activate your environment with:"
echo "  source venv/bin/activate"
