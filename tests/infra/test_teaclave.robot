*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Teaclave Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/infra/teaclave/config.toml
Teaclave Functions Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/infra/teaclave/functions.py
Has TEE Functions
    ${content}    Get File    ${PROJECT_ROOT}/src/infra/teaclave/functions.py
    Should Contain    ${content}    telemetry_decrypt
    Should Contain    ${content}    payload_verify
    Should Contain    ${content}    mission_data_aggregate
