*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
Run All Circuit Tests
    Set Working Directory    ${PROJECT_ROOT}/tests
    ${result}    Run Process    robot    --outputdir    report/circuits    --name    Circuits    circuits/test_circuits.robot
    Log    ${result.stdout}
    Log    ${result.stderr}

Run All zkVM Tests
    Set Working Directory    ${PROJECT_ROOT}/tests
    ${result}    Run Process    robot    --outputdir    report/zkvm    --name    zkVM    zkvm/test_zkvm.robot
    Log    ${result.stdout}
    Log    ${result.stderr}

Run All Verifier Tests
    Set Working Directory    ${PROJECT_ROOT}/tests
    ${result}    Run Process    robot    --outputdir    report/verifiers    --name    Verifiers    verifiers/test_verifiers.robot
    Log    ${result.stdout}
    Log    ${result.stderr}

Run All Script Tests
    Set Working Directory    ${PROJECT_ROOT}/tests
    ${result}    Run Process    robot    --outputdir    report/scripts    --name    Scripts    scripts/test_scripts.robot
    Log    ${result.stdout}
    Log    ${result.stderr}
