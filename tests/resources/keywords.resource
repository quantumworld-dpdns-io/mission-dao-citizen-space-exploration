*** Settings ***
Resource    common.resource

*** Keywords ***
File Should Exist And Not Be Empty
    [Arguments]    ${filepath}
    File Should Exist    ${filepath}
    ${content}    Get File    ${filepath}
    Should Not Be Empty    ${content}

Directory Should Exist And Contain Files
    [Arguments]    ${dirpath}
    Directory Should Exist    ${dirpath}
    ${files}    List Files In Directory    ${dirpath}
    Should Not Be Empty    ${files}

Check Shell Script Is Executable
    [Arguments]    ${script}
    File Should Exist    ${script}
    ${result}    Run Process    test -x ${script}    shell=True
    Should Be Equal As Integers    ${result.rc}    0    ${script} should be executable
