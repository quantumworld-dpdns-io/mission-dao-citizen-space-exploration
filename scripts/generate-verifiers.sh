#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CIRCUITS_DIR="$PROJECT_DIR/src/contracts/circuits"
SOLIDITY_DIR="$PROJECT_DIR/src/contracts/solidity"

echo "=== Generating Solidity verifiers from Noir circuits ==="

# Check nargo availability
if ! command -v nargo &>/dev/null; then
    echo "Error: nargo not found. Run scripts/setup-noir.sh first."
    exit 1
fi

# Build circuits
cd "$CIRCUITS_DIR"
nargo compile

# Generate Solidity verifier
nargo codegen-verifier

# Copy verifier to solidity directory
cp -v "$CIRCUITS_DIR/contract/TelemetryVerifier.sol" "$SOLIDITY_DIR/" 2>/dev/null || echo "Warning: TelemetryVerifier.sol not generated"
cp -v "$CIRCUITS_DIR/contract/FundingVerifier.sol" "$SOLIDITY_DIR/" 2>/dev/null || echo "Warning: FundingVerifier.sol not generated"

echo "=== Verifier generation complete ==="
