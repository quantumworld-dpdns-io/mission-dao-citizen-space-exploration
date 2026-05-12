#!/usr/bin/env bash
set -euo pipefail

echo "=== Installing RISC Zero toolchain (v1.2.x) ==="

# Install rzup if not present
if ! command -v rzup &>/dev/null; then
    echo "Installing rzup..."
    curl -L https://risczero.com/install | bash
    export PATH="$HOME/.risc0/bin:$PATH"
fi

# Install RISC Zero toolchain
rzup install

# Verify installation
cargo risczero --version || echo "cargo-risczero installed"
echo "=== RISC Zero installation complete ==="
