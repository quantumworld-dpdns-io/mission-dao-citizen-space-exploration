.PHONY: all setup-noir setup-zkvm build-circuits build-zkvm generate-verifiers \
        test-circuits test-zkvm test-robot clean

all: setup-noir setup-zkvm build-circuits build-zkvm generate-verifiers

# === Toolchain Setup ===

setup-noir:
	@bash scripts/setup-noir.sh

setup-zkvm:
	@bash scripts/setup-zkvm.sh

# === Build ===

build-circuits:
	cd src/contracts/circuits && nargo compile

build-zkvm:
	cd src/zkvm && cargo build --release

generate-verifiers:
	@bash scripts/generate-verifiers.sh

# === Test ===

test-circuits:
	cd src/contracts/circuits && nargo test --show-output

test-zkvm:
	cd src/zkvm && cargo test

test-robot:
	cd tests && robot --outputdir report suites/all_tests.robot

# === Clean ===

clean:
	rm -rf src/contracts/circuits/target
	rm -rf src/zkvm/target
	rm -rf tests/report
	find . -type d -name "out" -exec rm -rf {} + 2>/dev/null || true
