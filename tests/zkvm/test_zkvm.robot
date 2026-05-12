*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource
Test Setup    Set Working Directory    ${ZKVM_DIR}

*** Test Cases ***
Workspace Cargo.toml Exists
    File Should Exist And Not Be Empty    Cargo.toml

Methods Directory Exists
    Directory Should Exist And Contain Files    methods

Guest Source Directory Exists
    Directory Should Exist And Contain Files    methods/guest/src

Mission Receipt Guest Exists
    File Should Exist And Not Be Empty    methods/guest/src/mission_receipt.rs

Data Publication Guest Exists
    File Should Exist And Not Be Empty    methods/guest/src/data_publication.rs

Host Directory Exists
    Directory Should Exist And Contain Files    host/src

Host Main Exists
    File Should Exist And Not Be Empty    host/src/main.rs
