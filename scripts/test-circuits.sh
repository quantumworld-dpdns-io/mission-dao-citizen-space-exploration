#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CIRCUITS_DIR="$PROJECT_DIR/src/contracts/circuits"

echo "=== Testing Noir circuits ==="

if ! command -v nargo &>/dev/null; then
    echo "Error: nargo not found. Run scripts/setup-noir.sh first."
    exit 1
fi

cd "$CIRCUITS_DIR"

echo "Compiling circuits..."
nargo compile

echo "Running tests..."
nargo test --show-output

echo "=== Circuit tests complete ==="
