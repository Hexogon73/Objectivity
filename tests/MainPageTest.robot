*** Settings ***
Documentation    Suite description
Library  page_objects.IndexPage

*** Test Cases ***
Test click blog button
    [Tags]    DEBUG
    Search Button.Button Click
