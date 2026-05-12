#!/usr/bin/env bash
set -euo pipefail

echo "=== Installing Noir toolchain (latest stable) ==="

# Install noirup if not present
if ! command -v noirup &>/dev/null; then
    echo "Installing noirup..."
    curl -L https://raw.githubusercontent.com/noir-lang/noirup/main/install | bash
    export PATH="$HOME/.nargo/bin:$PATH"
fi

# Install latest Noir
noirup

# Verify installation
nargo --version
echo "=== Noir installation complete ==="
