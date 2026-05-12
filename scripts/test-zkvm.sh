#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ZKVM_DIR="$PROJECT_DIR/src/zkvm"

echo "=== Testing RISC Zero zkVM ==="

cd "$ZKVM_DIR"

echo "Building zkVM programs..."
cargo build --release

echo "Running host tests..."
cargo test

echo "=== zkVM tests complete ==="
