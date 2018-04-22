# -*- coding: utf-8 -*-
*** Settings ***
Documentation    Suite description
#Library  page_objects.IndexPage
Library  page_objects.SubscriptionPopup
Library  page_objects.IndexPage
Library  helpers.BrowserManager
#Library  helpers.IndexPageHelper
Variables  ../variables/global.py
Library  Selenium2Library

Suite Setup  Open Test Browser
#Suite Teardown  Close Test Browser

*** Test Cases ***
Test click search button
    [Tags]    DEBUG
#    Close Subscription Popup
    Click Search Button
