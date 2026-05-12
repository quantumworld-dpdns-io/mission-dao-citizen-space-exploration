*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource
Test Setup    Set Working Directory    ${CIRCUITS_DIR}

*** Test Cases ***
Nargo.toml Exists
    File Should Exist And Not Be Empty    Nargo.toml

Source Directory Exists
    Directory Should Exist And Contain Files    src

Main Circuit File Exists
    File Should Exist And Not Be Empty    src/main.nr

Funding Circuit File Exists
    File Should Exist And Not Be Empty    src/funding.nr

Merkle Circuit File Exists
    File Should Exist And Not Be Empty    src/merkle.nr

Prover Config Exists
    File Should Exist And Not Be Empty    Prover.toml

Verifier Config Exists
    File Should Exist And Not Be Empty    Verifier.toml
