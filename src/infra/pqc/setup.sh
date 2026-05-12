#!/usr/bin/env bash
set -euo pipefail

echo "=== Post-Quantum Cryptography Setup ==="

# Install liboqs (Open Quantum Safe library)
echo "Installing liboqs..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install liboqs
else
    git clone --depth 1 https://github.com/open-quantum-safe/liboqs.git /tmp/liboqs
    cd /tmp/liboqs
    mkdir build && cd build
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local ..
    make -j$(nproc)
    sudo make install
fi

# Install OQS-OpenSSL3 provider
echo "Installing OQS-OpenSSL3 provider..."
git clone --depth 1 https://github.com/open-quantum-safe/oqs-provider.git /tmp/oqs-provider
cd /tmp/oqs-provider
cmake -DCMAKE_PREFIX_PATH=/usr/local ..
make -j$(nproc)
sudo make install

# Verify installation
echo "Verifying PQC algorithms..."
if command -v openssl &>/dev/null; then
    openssl list -kem-algorithms 2>/dev/null | grep -i "ml-kem" && echo "ML-KEM available" || echo "ML-KEM not found"
    openssl list -sig-algorithms 2>/dev/null | grep -i "ml-dsa" && echo "ML-DSA available" || echo "ML-DSA not found"
fi

echo "=== PQC Setup Complete ==="
