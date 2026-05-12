*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
MCP Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/mcp

Server Base Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/mcp/server.py

GitHub Server Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/mcp/github_server.py

Storage Server Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/mcp/storage_server.py

Onchain Server Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/mcp/onchain_server.py

Telemetry Server Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/mcp/telemetry_server.py
