*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource
Test Setup    Set Working Directory    ${PROJECT_ROOT}/src

*** Test Cases ***
Governance Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/agents/governance

State Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/governance/state.py

Graph Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/governance/graph.py

Nodes Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/governance/nodes.py

Models Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/governance/models.py

Crews Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/agents/crews

Agents Definition Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/crews/agents.py

Tasks Definition Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/crews/tasks.py

Crew Definition Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/crews/crew.py

Tools Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/crews/tools.py

Requirements Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/agents/requirements.txt
