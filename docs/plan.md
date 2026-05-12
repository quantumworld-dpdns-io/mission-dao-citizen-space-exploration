# Phase 1 Execution Plan: DAO & Verifiable Data Foundation

## Objectives

1. Scaffold Noir ZK circuits for mission-data integrity, funding verification, and Merkle membership proofs
2. Deploy RISC Zero zkVM for verifiable mission-execution receipts
3. Generate Solidity verifier contracts for on-chain DAO governance (Arbitrum, Base, Sepolia)
4. Create shell scripts for toolchain setup, builds, and testing
5. Set up CI workflows for automated verification
6. Add Robot Framework integration tests covering all components
7. Maintain git commits to `dev` branch every 60 seconds throughout execution

## Agent Architecture

All 9 agents execute in parallel (non-conflicting file paths):

| Agent | Domain | Outputs |
|-------|--------|---------|
| Docs | Documentation | README.md, docs/plan.md, docs/progress.md |
| Circuits | Noir ZK | src/contracts/circuits/ (6 files) |
| zkVM | RISC Zero | src/zkvm/ (7 files) |
| Solidity | EVM Verifiers | src/contracts/solidity/ (7 files) |
| Scripts | Shell tooling | scripts/ (5 files) |
| CI | GitHub Actions | .github/workflows/ (2 files) |
| Root | Build system | Makefile, .gitignore |
| Robot | E2E Testing | tests/ (9 files) |
| Git Loop | Version control | Background commit every 60s |

## File Tree

```
.
├── README.md
├── docs/
│   ├── plan.md
│   └── progress.md
├── src/
│   ├── contracts/
│   │   ├── circuits/
│   │   │   ├── Nargo.toml
│   │   │   ├── Prover.toml
│   │   │   ├── Verifier.toml
│   │   │   └── src/
│   │   │       ├── main.nr          # telemetry-integrity
│   │   │       ├── funding.nr       # funding-verification
│   │   │       └── merkle.nr        # Merkle membership
│   │   └── solidity/
│   │       ├── TelemetryVerifier.sol
│   │       ├── FundingVerifier.sol
│   │       ├── deployment/deploy_arbitrum.ts
│   │       ├── deployment/deploy_base.ts
│   │       ├── deployment/deploy_sepolia.ts
│   │       ├── hardhat.config.ts
│   │       └── package.json
│   └── zkvm/
│       ├── Cargo.toml
│       ├── methods/
│       │   ├── Cargo.toml
│       │   └── guest/
│       │       ├── Cargo.toml
│       │       └── src/
│       │           ├── mission_receipt.rs
│       │           └── data_publication.rs
│       └── host/
│           ├── Cargo.toml
│           └── src/
│               └── main.rs
├── scripts/
│   ├── setup-noir.sh
│   ├── setup-zkvm.sh
│   ├── generate-verifiers.sh
│   ├── test-circuits.sh
│   └── test-zkvm.sh
├── tests/
│   ├── requirements.txt
│   ├── robot.yaml
│   ├── resources/
│   │   ├── common.resource
│   │   └── keywords.resource
│   ├── circuits/test_circuits.robot
│   ├── zkvm/test_zkvm.robot
│   ├── verifiers/test_verifiers.robot
│   ├── scripts/test_scripts.robot
│   └── suites/all_tests.robot
├── .github/workflows/
│   ├── verify-circuits.yml
│   └── verify-zkvm.yml
├── Makefile
└── .gitignore
```

## Technical Decisions

| Decision | Choice |
|----------|--------|
| Noir version | Latest stable (~0.36+) via noirup |
| RISC Zero version | v1.2.x via rzup |
| Solidity targets | Arbitrum, Base, Sepolia (EVM-compatible) |
| Proving mode | Local (CPU) default; BONSAI_API_KEY env for remote |
| Test framework | Robot Framework v7.x |
| Rust edition | 2021 |
| CI trigger | push & PR to main |
| Commit cadence | Every 60s to dev branch (--allow-empty) |
| License | MIT, ©2026 quantumworld-dpdns-io |

---

# Phase 2 Execution Plan: Agentic Governance & Workflows

## Objectives

1. Implement LangGraph state machine for proposal lifecycle (submit → review → vote → execute)
2. Define CrewAI agent roles for multi-agent mission planning: Mission Planner, Budget Analyst, Data Verifier, Community Liaison
3. Build MCP servers for tool integration: GitHub issues, IPFS/Arweave storage, on-chain queries, telemetry API
4. Add Robot Framework tests for all new components

## Agent Architecture

| Agent | Domain | Outputs |
|-------|--------|---------|
| Agents | LangGraph + CrewAI | src/agents/governance/ (6 files), src/agents/crews/ (5 files) |
| MCP | Protocol Servers | src/mcp/ (6 files) |
| Tests & Docs | E2E + Documentation | tests/agents/, tests/mcp/, docs/plan.md, docs/progress.md, README.md |

## Files Created

```
src/
├── __init__.py
├── agents/
│   ├── __init__.py
│   ├── requirements.txt
│   ├── governance/
│   │   ├── __init__.py
│   │   ├── state.py          # ProposalState TypedDict, ProposalStatus enum
│   │   ├── models.py         # Pydantic Proposal model
│   │   ├── nodes.py          # LangGraph node functions
│   │   └── graph.py          # StateGraph definition with conditional edges
│   └── crews/
│       ├── __init__.py
│       ├── agents.py          # 4 CrewAI agent definitions
│       ├── tasks.py           # 4 CrewAI task definitions
│       ├── crew.py            # CrewAI crew assembly (sequential)
│       └── tools.py           # Shared agent tool wrappers
├── mcp/
│   ├── __init__.py
│   ├── server.py              # Base MCPServer class (JSON-RPC 2.0)
│   ├── github_server.py       # GitHub issues tools
│   ├── storage_server.py      # IPFS/Arweave storage tools
│   ├── onchain_server.py      # On-chain proposal/vote tools
│   └── telemetry_server.py    # Telemetry query and ZK proof verification
tests/
├── agents/
│   └── test_governance.robot   # 11 test cases
└── mcp/
    └── test_mcp_servers.robot  # 6 test cases
```

## Governance State Machine

```
Proposal Lifecycle:
  DRAFT → SUBMITTED → UNDER_REVIEW → VOTING → APPROVED → EXECUTED
                                              → REJECTED
```

## MCP Server Architecture

| Server | Port | Tools |
|--------|------|-------|
| github-issues | 8001 | create_issue, list_issues |
| ipfs-arweave-storage | 8002 | store_data, retrieve_data |
| onchain-queries | 8003 | submit_proposal, query_votes |
| telemetry-api | 8004 | query_telemetry, verify_telemetry_proof |

## Technical Decisions

| Decision | Choice |
|----------|--------|
| LangGraph version | Latest (>=0.2.0) |
| CrewAI version | Latest (>=0.80.0) |
| Pydantic version | v2 |
| MCP transport | JSON-RPC 2.0 via jsonrpcserver |
| Agent process | Sequential (CrewAI Process.sequential) |
| Git commit cadence | Every 60s to dev branch (existing loop) |

---

# Phase 3 Execution Plan: Data Lakehouse & Retrieval

## Objectives

1. Deploy Apache Iceberg catalog via Polaris with mission telemetry schemas
2. Set up DuckDB for local mission analytics
3. Configure Trino for federated cross-mission queries
4. Deploy Qdrant for RAG over mission documents, regulatory filings, sensor manuals
5. Ingest telemetry into LanceDB for multimodal (image+vector+tabular) retrieval

## Agent Architecture

| Agent | Domain | Outputs |
|-------|--------|---------|
| Lakehouse Foundation | Iceberg + DuckDB + Trino | src/lakehouse/iceberg/ (3 files), src/lakehouse/duckdb/ (2 files), src/lakehouse/trino/ (3 files) |
| Vector Retrieval | Qdrant + LanceDB | src/lakehouse/qdrant/ (2 files), src/lakehouse/lancedb/ (2 files) |
| Tests & Docs | E2E + Documentation | tests/lakehouse/ (5 files), plan.md, progress.md, README.md |

## Files Created

```
src/lakehouse/
├── __init__.py
├── requirements.txt
├── iceberg/
│   ├── __init__.py
│   ├── schema.py          # TELEMETRY_SCHEMA, MISSION_SCHEMA
│   ├── catalog.py         # Polaris REST catalog init
│   └── queries.py         # 5 analytical queries
├── duckdb/
│   ├── __init__.py
│   ├── setup.py           # DuckDB + Iceberg extension init
│   └── queries.py         # 4 local analytics queries
├── trino/
│   ├── __init__.py
│   ├── catalog.py         # Trino connection config
│   ├── queries.py         # 4 federated queries
│   └── catalog.yaml       # Trino Iceberg catalog config
├── qdrant/
│   ├── __init__.py
│   ├── collection.py      # Vector collection configs + payload schemas
│   └── ingestion.py       # Document ingestion + semantic search
└── lancedb/
    ├── __init__.py
    ├── schema.py           # Multimodal table schemas (tabular + embeddings)
    └── ingestion.py        # Telemetry batch ingest + embedding search
tests/lakehouse/
├── test_iceberg.robot      # 6 test cases
├── test_duckdb.robot       # 4 test cases
├── test_trino.robot        # 4 test cases
├── test_qdrant.robot       # 4 test cases
└── test_lancedb.robot      # 4 test cases
```

## Technical Decisions

| Decision | Choice |
|----------|--------|
| Iceberg catalog | Polaris (REST) via PyIceberg |
| Vector embedding model | all-MiniLM-L6-v2 (384 dim) |
| Qdrant distance | Cosine |
| DuckDB extensions | iceberg, httpfs |
| Trino Iceberg connector | REST catalog type |
| LanceDB storage | Local (data/mission_lancedb) |

---

# Phase 4 Execution Plan: Local & Edge AI Serving

## Objectives

1. Serve mission-assist models via Ollama (anomaly detection, resource optimization, mission planning)
2. Deploy SGLang for high-throughput structured generation with JSON schema enforcement
3. Wrap observability with OpenTelemetry SDKs exporting to Arize Phoenix
4. Set up federated learning with Flower for cross-community telemetry model training

## Agent Architecture

| Agent | Domain | Outputs |
|-------|--------|---------|
| Ollama | Local model serving | src/serving/ollama/ (client, models, prompts) |
| SGLang + OTEL | Structured gen + observability | src/serving/sglang/ (client, server, schemas), src/serving/openllmetry/ (tracing, phoenix, metrics) |
| Federated | Flower FL | src/federated/ (client, server, strategy, models) |
| Tests & Docs | E2E + Documentation | 4 test files, plan.md, progress.md, README.md |

## Files Created

```
src/serving/
├── __init__.py
├── requirements.txt
├── ollama/
│   ├── __init__.py
│   ├── client.py          # Ollama HTTP API wrapper
│   ├── models.py          # Model configs for 5 mission tasks
│   └── prompts.py         # 4 prompt templates + system prompts
├── sglang/
│   ├── __init__.py
│   ├── client.py          # SGLang runtime client
│   ├── server.py          # Server launch config
│   └── structured_gen.py  # 3 JSON schemas + generate_structured
└── openllmetry/
    ├── __init__.py
    ├── tracing.py         # OpenTelemetry tracer + Phoenix OTLP
    ├── phoenix.py         # Arize Phoenix exporter config
    └── metrics.py         # 6 custom OTEL metrics

src/federated/
├── __init__.py
├── requirements.txt
├── client.py             # TelemetryFlowerClient
├── server.py             # Federated server launcher
├── strategy.py           # FedAvg + FedAdagrad strategies
└── models/
    ├── __init__.py
    ├── anomaly_detector.py  # Autoencoder-based anomaly detection
    └── resource_optimizer.py # Feed-forward resource optimizer

tests/
├── serving/
│   ├── test_ollama.robot    # 6 test cases
│   ├── test_sglang.robot    # 6 test cases
│   └── test_otel.robot      # 6 test cases
└── federated/
    └── test_flower.robot    # 7 test cases
```

## Technical Decisions

| Decision | Choice |
|----------|--------|
| Ollama models | llama3.2:3b (anomaly, optimization), llama3.1:8b (planning, reports) |
| SGLang features | FlashInfer, structured JSON decoding, metrics endpoint |
| OTEL transport | OTLP gRPC to Phoenix (localhost:6006) |
| Phoenix export | /v1/traces endpoint, project: mission-dao |
| Flower strategy | FedAvg with configurable local epochs + learning rate |
| Anomaly model | Autoencoder (10→64→32→16 latent) |
| Optimizer model | FFNN (8→128→128→64→4) with sigmoid output |

---

# Phase 5 Execution Plan: WebAssembly & Sandboxed Execution

## Objectives
1. Build Fermyon Spin micro-APIs for mission status, funding calculator, telemetry summary
2. Embed Wasmtime for sandboxed community plugin execution

## Files Created
```
src/wasm/
├── __init__.py
├── spin/
│   ├── spin.toml          # 4 HTTP routes
│   ├── Cargo.toml
│   └── src/lib.rs         # mission_status, funding_calculator, telemetry_summary, health_check
└── wasmtime/
    ├── Cargo.toml
    └── src/main.rs        # Plugin loader for .wasm files
```

---

# Phase 6 Execution Plan: Security, Caching & Commerce

## Objectives
1. Deploy Dragonfly cache layer for real-time telemetry dashboards
2. Configure Apache Teaclave TEE for confidential payload processing
3. Wire Google UCP for mission funding checkout
4. Enable PQC hybrid key exchange for mission communication

## Files Created
```
src/infra/
├── __init__.py
├── requirements.txt
├── dragonfly/
│   └── client.py            # DragonflyCache with telemetry/mission/agent methods
├── teaclave/
│   ├── config.toml          # TEE enclave configuration
│   └── functions.py         # telemetry_decrypt, payload_verify, mission_data_aggregate
├── ucp/
│   └── client.py            # UCPClient for checkout sessions + funding products
└── pqc/
    ├── setup.sh             # liboqs + OQS-OpenSSL3 install
    └── hybrid.py            # X25519 + AES-GCM hybrid encryption
```

---

# Container Microservices

## Objectives
1. Docker Compose stack for all services (12 containers)
2. Multi-stage Dockerfiles for web (Next.js) and API (Python)
3. Dev and production Compose overlays

## Files Created
```
docker/
├── docker-compose.yml        # 12 services: web, api, 4x mcp, qdrant, trino, polaris, dragonfly, phoenix, ollama
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── web.Dockerfile            # Node.js multi-stage (dev/build/prod)
├── api.Dockerfile            # Python multi-stage (dev/prod)
├── .dockerignore
└── config/trino/catalog/iceberg.properties
```

---

# Next.js Web Application

## Objectives
1. Next.js 14+ App Router with TypeScript and Tailwind CSS
2. Pages: Home, Missions, Proposals, DAO Dashboard
3. API client library for backend services

## Files Created
```
web/
├── package.json
├── next.config.ts
├── tsconfig.json
├── tailwind.config.ts
├── postcss.config.mjs
├── .env.local
└── src/
    ├── app/
    │   ├── globals.css
    │   ├── layout.tsx
    │   ├── page.tsx           # Landing page
    │   ├── missions/page.tsx
    │   ├── proposals/page.tsx
    │   └── dao/page.tsx
    ├── components/
    │   └── Header.tsx
    └── lib/
        └── api.ts             # Fetch wrapper for API/MCP services
```

## Technical Decisions

| Decision | Choice |
|----------|--------|
| Next.js version | 14.2 (App Router, standalone output) |
| Styling | Tailwind CSS 3.4 with custom cosmic color palette |
| API client | Typed fetch wrapper with env-configurable base URL |
| Spin runtime | Fermyon Spin 3.x with WASI target |
| Wasmtime version | 24.x with Tokio async runtime |
| Dragonfly image | docker.dragonflydb.io/dragonflydb/dragonfly:latest |
| Teaclave attestation | Simulation mode (SGX for production) |
| UCP integration | REST API with Bearer token auth |
| PQC algorithms | ML-KEM (key exchange), ML-DSA (signatures) via liboqs |
| Hybrid encryption | X25519 ECDH + AES-256-GCM |
