*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource
Test Setup    Set Working Directory    ${SOLIDITY_DIR}

*** Test Cases ***
TelemetryVerifier Exists
    File Should Exist And Not Be Empty    TelemetryVerifier.sol

FundingVerifier Exists
    File Should Exist And Not Be Empty    FundingVerifier.sol

Deployment Directory Exists
    Directory Should Exist And Contain Files    deployment

Deploy Arbitrum Script Exists
    File Should Exist And Not Be Empty    deployment/deploy_arbitrum.ts

Deploy Base Script Exists
    File Should Exist And Not Be Empty    deployment/deploy_base.ts

Deploy Sepolia Script Exists
    File Should Exist And Not Be Empty    deployment/deploy_sepolia.ts

Hardhat Config Exists
    File Should Exist And Not Be Empty    hardhat.config.ts

Package JSON Exists
    File Should Exist And Not Be Empty    package.json
