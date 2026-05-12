from crewai import Task
from .agents import mission_planner, budget_analyst, data_verifier, community_liaison

plan_mission = Task(
    description="Design a CubeSat mission plan including orbit, payload, and timeline",
    expected_output="Detailed mission plan document with orbit parameters, payload specs, and milestones",
    agent=mission_planner,
)

analyze_budget = Task(
    description="Analyze mission costs and verify funding threshold is met",
    expected_output="Budget analysis report with cost breakdown and funding verification",
    agent=budget_analyst,
)

verify_data = Task(
    description="Verify telemetry data integrity using ZK proof verification procedures",
    expected_output="Data verification report confirming integrity or flagging anomalies",
    agent=data_verifier,
)

engage_community = Task(
    description="Collect community feedback and communicate mission progress to stakeholders",
    expected_output="Community engagement report with feedback summary and status update",
    agent=community_liaison,
)
