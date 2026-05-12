from crewai import Crew, Process
from .agents import (
    mission_planner,
    budget_analyst,
    data_verifier,
    community_liaison,
)
from .tasks import (
    plan_mission,
    analyze_budget,
    verify_data,
    engage_community,
)

mission_crew = Crew(
    agents=[mission_planner, budget_analyst, data_verifier, community_liaison],
    tasks=[plan_mission, analyze_budget, verify_data, engage_community],
    process=Process.sequential,
    verbose=True,
)
