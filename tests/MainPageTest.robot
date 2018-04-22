# -*- coding: utf-8 -*-
*** Settings ***
Documentation    Suite description
Library  page_objects.SubscriptionPopup
Library  page_objects.IndexPage
Library  helpers.BrowserManager
Variables  ../variables/global.py
Library  Selenium2Library

Suite Setup  Open Test Browser
#Suite Teardown  Close Test Browser

*** Test Cases ***
Test click search button
    [Documentation]  Тест открытия формы поиска
    [Tags]    DEBUG
#    Close Subscription Popup
    Click Search Button
    Check Search Form
