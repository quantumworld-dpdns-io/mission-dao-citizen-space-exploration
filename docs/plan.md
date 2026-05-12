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
