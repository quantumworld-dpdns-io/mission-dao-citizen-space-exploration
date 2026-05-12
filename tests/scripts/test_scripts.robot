*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Setup Noir Script Exists And Executable
    Check Shell Script Is Executable    ${SCRIPTS_DIR}/setup-noir.sh

Setup zkVM Script Exists And Executable
    Check Shell Script Is Executable    ${SCRIPTS_DIR}/setup-zkvm.sh

Generate Verifiers Script Exists And Executable
    Check Shell Script Is Executable    ${SCRIPTS_DIR}/generate-verifiers.sh

Test Circuits Script Exists And Executable
    Check Shell Script Is Executable    ${SCRIPTS_DIR}/test-circuits.sh

Test zkVM Script Exists And Executable
    Check Shell Script Is Executable    ${SCRIPTS_DIR}/test-zkvm.sh
