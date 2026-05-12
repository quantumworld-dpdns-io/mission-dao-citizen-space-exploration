# mission-dao-citizen-space-exploration

> Mission DAO for citizen space exploration — platform for communities to fund and govern CubeSat missions with verifiable data publication

Part of the [quantumworld-dpdns-io](https://github.com/quantumworld-dpdns-io) Wild SaaS & Tech Development initiative.

## Architecture

The platform integrates:
- **ZK Proofs** — Noir circuits + RISC Zero zkVM for verifiable mission-data publication
- **DAO Governance** — Solidity verifiers deployed to Arbitrum / Base / Sepolia
- **Agent Orchestration** — LangGraph + CrewAI for proposal workflows
- **Data Lakehouse** — Apache Iceberg + Trino + DuckDB for telemetry analytics
- **Vector Retrieval** — Qdrant + LanceDB for mission-document RAG and multimodal telemetry search
- **Local AI** — Ollama + SGLang for edge model serving and structured generation
- **Edge AI** — Ollama/SGLang for local mission-assist model serving
- **Federated Learning** — Flower for cross-community telemetry model training
- **Observability** — OpenTelemetry + Arize Phoenix for LLM tracing and metrics
- **WebAssembly** — Fermyon Spin + Wasmtime for sandboxed plugin execution

## Phase Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| **1** | DAO & Verifiable Data Foundation (ZK circuits, zkVM, verifiers) | ✅ Complete |
| **2** | Agentic Governance & Workflows (LangGraph, CrewAI, MCP) | ✅ Complete |
| **3** | Data Lakehouse & Retrieval (Iceberg, Trino, Qdrant) | ✅ Complete |
| **4** | Local & Edge AI Serving (Ollama, SGLang, OpenTelemetry) | In Progress |
| **5** | WebAssembly & Sandboxed Execution (Spin, Wasmtime) | Planned |
| **6** | Security, Caching & Commerce (Dragonfly, Teaclave, UCP) | Planned |

## Project Structure

```
.
├── src/
│   ├── agents/
│   │   ├── governance/        # LangGraph proposal lifecycle state machine
│   │   └── crews/             # CrewAI multi-agent mission planning
│   ├── contracts/
│   │   ├── circuits/          # Noir ZK circuits (telemetry, funding, Merkle)
│   │   └── solidity/          # Solidity verifier contracts + deploy scripts
│   ├── lakehouse/             # Data lakehouse (Iceberg, DuckDB, Trino, Qdrant, LanceDB)
│   ├── serving/               # Local AI serving (Ollama, SGLang, OTEL)
│   ├── federated/             # Federated learning (Flower)
│   ├── mcp/                   # MCP servers (GitHub, storage, on-chain, telemetry)
│   └── zkvm/                  # RISC Zero zkVM guest/host programs
├── scripts/                   # Setup, build, and test scripts
├── tests/
│   ├── resources/             # Robot Framework shared resources
│   ├── agents/                # Governance & CrewAI agent tests
│   ├── circuits/              # Circuit integration tests
│   ├── mcp/                   # MCP server tests
│   ├── zkvm/                  # zkVM integration tests
│   ├── verifiers/             # Verifier contract tests
│   ├── scripts/               # Script execution tests
│   └── suites/                # Main test suites
├── docs/
│   ├── CONTRIBUTING.md        # Contribution guide
│   ├── plan.md                # Phase 1 execution plan
│   └── progress.md            # Live build progress
├── .github/workflows/         # CI/CD pipelines
├── Makefile                   # Build automation
└── LICENSE                    # MIT
```

## Prerequisites

- [Noir](https://noir-lang.org/) (latest stable via `noirup`)
- [RISC Zero](https://risczero.com/) (v1.2.x via `rzup`)
- [Rust](https://www.rust-lang.org/) (edition 2021)
- [Node.js](https://nodejs.org/) (for Hardhat/Solidity)
- [Python](https://python.org/) 3.10+ (for Robot Framework)
- [Robot Framework](https://robotframework.org/) (v7.x)

## Quick Start

```bash
# Install toolchains
make setup-noir
make setup-zkvm

# Build all circuits
make build-circuits

# Build zkVM programs
make build-zkvm

# Generate Solidity verifiers
make generate-verifiers

# Run tests
make test-circuits
make test-zkvm

# Run full Robot Framework test suite
make test-robot
```

## License

MIT — see [LICENSE](LICENSE). ©2026 quantumworld-dpdns-io.
