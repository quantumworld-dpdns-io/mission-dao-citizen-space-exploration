*** Settings ***
Library    OperatingSystem
Library    Process
Library    Collections

*** Variables ***
${PROJECT_ROOT}    ${CURDIR}/../..
${CIRCUITS_DIR}    ${PROJECT_ROOT}/src/contracts/circuits
${ZKVM_DIR}        ${PROJECT_ROOT}/src/zkvm
${SOLIDITY_DIR}    ${PROJECT_ROOT}/src/contracts/solidity
${SCRIPTS_DIR}     ${PROJECT_ROOT}/scripts
