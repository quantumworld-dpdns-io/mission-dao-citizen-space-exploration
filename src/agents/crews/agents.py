from crewai import Agent

mission_planner = Agent(
    role="Mission Planner",
    goal="Design and plan CubeSat missions including orbit parameters, payload configuration, and timeline",
    backstory="Expert space mission architect with experience in small satellite deployment",
    verbose=True,
    allow_delegation=False,
)

budget_analyst = Agent(
    role="Budget Analyst",
    goal="Analyze mission costs, verify funding thresholds, and optimize resource allocation",
    backstory="Financial analyst specialized in aerospace project budgeting and DAO treasury management",
    verbose=True,
    allow_delegation=False,
)

data_verifier = Agent(
    role="Data Verifier",
    goal="Verify telemetry data integrity using ZK proofs and ensure compliance with mission parameters",
    backstory="Cryptographic data integrity specialist with deep knowledge of zero-knowledge proofs",
    verbose=True,
    allow_delegation=False,
)

community_liaison = Agent(
    role="Community Liaison",
    goal="Facilitate community governance, collect feedback, and communicate mission status to stakeholders",
    backstory="Community manager experienced in DAO governance and decentralized decision-making",
    verbose=True,
    allow_delegation=False,
)
