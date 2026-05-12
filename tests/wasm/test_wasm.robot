*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Spin Manifest Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/wasm/spin/spin.toml
Spin Cargo Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/wasm/spin/Cargo.toml
Spin Source Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/wasm/spin/src/lib.rs
Wasmtime Cargo Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/wasm/wasmtime/Cargo.toml
Wasmtime Main Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/wasm/wasmtime/src/main.rs
Has Four Spin Components
    ${content}    Get File    ${PROJECT_ROOT}/src/wasm/spin/src/lib.rs
    Should Contain    ${content}    mission_status
    Should Contain    ${content}    funding_calculator
    Should Contain    ${content}    telemetry_summary
    Should Contain    ${content}    health_check
