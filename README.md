# mission-dao-citizen-space-exploration

> Mission DAO for citizen space exploration — platform for communities to fund and govern CubeSat missions with verifiable data publication

Part of the [quantumworld-dpdns-io](https://github.com/quantumworld-dpdns-io) Wild SaaS & Tech Development initiative.

## Status

All 6 phases of the project scaffold are complete and committed to `dev`.

## Architecture

The platform integrates:

- **ZK Proofs** — Noir circuits + RISC Zero zkVM for verifiable mission-data publication
- **DAO Governance** — Solidity verifiers deployed to Arbitrum / Base / Sepolia
- **Agent Orchestration** — LangGraph + CrewAI for proposal workflows
- **Data Lakehouse** — Apache Iceberg + Trino + DuckDB for telemetry analytics
- **Vector Retrieval** — Qdrant + LanceDB for mission-document RAG and multimodal telemetry search
- **Local AI** — Ollama + SGLang for edge model serving and structured generation
- **Federated Learning** — Flower for cross-community telemetry model training
- **Observability** — OpenTelemetry + Arize Phoenix for LLM tracing and metrics
- **WebAssembly** — Fermyon Spin + Wasmtime for sandboxed plugin execution
- **Cache** — Dragonfly (Redis-compatible) for real-time telemetry dashboards
- **Confidential Compute** — Apache Teaclave TEE for sensitive payload processing
- **Commerce** — Google UCP for mission funding checkout
- **PQC** — Hybrid post-quantum key exchange (X25519 + AES-GCM, liboqs)

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
│   ├── federated/             # Federated learning (Flower client/server/strategy/models)
│   ├── infra/
│   │   ├── dragonfly/         # Redis-compatible cache client
│   │   ├── teaclave/          # Apache Teaclave TEE config + functions
│   │   ├── ucp/               # Google Universal Commerce Protocol client
│   │   └── pqc/               # Post-quantum crypto setup + hybrid encryption
│   ├── lakehouse/
│   │   ├── iceberg/           # Iceberg schemas, Polaris catalog, queries
│   │   ├── duckdb/            # Local analytics with Iceberg extension
│   │   ├── trino/             # Federated query catalog + queries
│   │   ├── qdrant/            # Vector collection configs + document ingestion
│   │   └── lancedb/           # Multimodal tables + batch ingestion
│   ├── mcp/                   # MCP servers (GitHub, storage, on-chain, telemetry)
│   ├── serving/
│   │   ├── ollama/            # Local model client, configs, prompt templates
│   │   ├── sglang/            # High-throughput structured generation
│   │   └── openllmetry/       # OpenTelemetry tracing, Phoenix, custom metrics
│   ├── wasm/
│   │   ├── spin/              # Fermyon Spin micro-APIs (4 endpoints)
│   │   └── wasmtime/          # Wasmtime sandboxed plugin loader
│   └── zkvm/                  # RISC Zero zkVM guest/host programs
├── web/                       # Next.js 14 App Router frontend (5 pages)
├── docker/                    # Docker Compose (12 services) + multi-stage Dockerfiles
├── scripts/                   # Setup, build, and test scripts
├── tests/                     # Robot Framework test suites
│   ├── agents/                # Governance & CrewAI agent tests
│   ├── circuits/              # Circuit integration tests
│   ├── docker/                # Docker infrastructure tests
│   ├── federated/             # Federated learning tests
│   ├── infra/                 # Cache, TEE, UCP, PQC tests
│   ├── lakehouse/             # Iceberg, DuckDB, Trino, Qdrant, LanceDB tests
│   ├── mcp/                   # MCP server tests
│   ├── scripts/               # Script execution tests
│   ├── serving/               # Ollama, SGLang, OTEL tests
│   ├── verifiers/             # Solidity verifier tests
│   ├── wasm/                  # WebAssembly tests
│   ├── web/                   # Next.js frontend tests
│   └── zkvm/                  # zkVM integration tests
├── docs/
│   ├── CONTRIBUTING.md        # Contribution guide
│   ├── plan.md                # Full execution plan (all 6 phases)
│   └── progress.md            # Build progress tracker
├── .github/workflows/         # CI/CD pipelines
├── Makefile                   # Build automation
└── LICENSE                    # MIT
```

## Quick Start

### Web Frontend

```bash
cd web
npm install
npm run dev        # → http://localhost:3000
```

### Full Stack (Docker)

```bash
docker compose -f docker/docker-compose.yml up -d
# 12 services: web, api, 4x mcp, qdrant, trino, polaris, dragonfly, phoenix, ollama
```

### Local Toolchains

```bash
# Install ZK toolchains
make setup-noir        # Noir latest stable via noirup
make setup-zkvm        # RISC Zero v1.2 via rzup

# Build circuits + zkVM
make build-circuits
make build-zkvm

# Generate Solidity verifiers
make generate-verifiers

# Run tests
make test-circuits
make test-zkvm
make test-robot          # Full Robot Framework suite
```

## Deployment

### Vercel (Web)

The Next.js frontend deploys to Vercel. Connect the repo at:
`https://vercel.com/quantumworld-dpdns-io/mission-dao-citizen-space-exploration`

Root directory: `web`
Build command: `npm run build`
Output directory: `.next`

**Note:** `next.config.mjs` is used instead of `next.config.ts` — Vercel's Next.js 14.2 does not support TypeScript config files.

### Docker (Full Stack)

```bash
# Production stack
docker compose -f docker/docker-compose.prod.yml up -d

# Development stack with hot reload
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up -d
```

### Smart Contracts (Coming Soon)

```bash
cd src/contracts/solidity
npm install
npx hardhat compile
npx hardhat run deployment/deploy_sepolia.ts --network sepolia
```

## Features by Module

| Module | Tech | Key Capabilities |
|--------|------|------------------|
| Governance | LangGraph, CrewAI | Proposal lifecycle state machine, 4 agent roles, sequential mission crew |
| ZK Proofs | Noir, RISC Zero | Telemetry integrity, funding verification, Merkle membership, execution receipts |
| Data Lakehouse | Iceberg, Polaris, Trino, DuckDB | Mission telemetry schemas, federated cross-mission queries, local analytics |
| Vector Search | Qdrant, LanceDB | Document RAG with metadata filtering, multimodal telemetry embeddings |
| Model Serving | Ollama, SGLang | 5 model configs, 4 prompt templates, constrained JSON generation schemas |
| Observability | OpenTelemetry, Phoenix | Distributed tracing, 6 custom metrics, LLM evaluation exporter |
| Federated Learning | Flower | FedAvg/FedAdagrad, autoencoder anomaly detector, resource optimizer |
| WebAssembly | Fermyon Spin, Wasmtime | 4 HTTP micro-APIs, sandboxed `.wasm` plugin loader |
| Cache | Dragonfly | Async telemetry cache, mission summaries, active agent tracking, vote counters |
| Confidential Compute | Apache Teaclave | TEE-based decrypt, verify, aggregate functions |
| Commerce | Google UCP | Checkout sessions, funding products, payment flow |
| PQC | liboqs, OQS-OpenSSL3 | ML-KEM/ML-DSA algorithms, X25519 + AES-256-GCM hybrid encryption |
| Containers | Docker Compose | 12-service stack, multi-stage Dockerfiles, dev/prod overlays |
| Frontend | Next.js 14, Tailwind | 5 App Router pages, API client library, cosmic theme |

## Prerequisites

- [Noir](https://noir-lang.org/) (latest stable via `noirup`)
- [RISC Zero](https://risczero.com/) (v1.2.x via `rzup`)
- [Rust](https://www.rust-lang.org/) (edition 2021)
- [Node.js](https://nodejs.org/) 20+ (for web + Hardhat)
- [Python](https://python.org/) 3.10+ (for agents, lakehouse, serving, infra)
- [Docker](https://docker.com/) (for full-stack deployment)
- [Robot Framework](https://robotframework.org/) (v7.x, for integration tests)

## License

MIT — see [LICENSE](LICENSE). ©2026 quantumworld-dpdns-io.
