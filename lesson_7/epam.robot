*** Settings ***
Documentation    This suite contains test cases related to Lesson 7 Homework.
Library           RPA.Browser.Selenium     auto_close=${FALSE}
Variables         variables.py
Suite Setup       Launch Browser
Suite Teardown    close browser

*** Variables ***
${LOCATION}=        class:location-selector__button
${SERVICES}=        //*[@class="top-navigation__item-link" and @href="/services"]
${OUR_WORK}=        //*[@class="top-navigation__item-link" and @href="/our-work"]
${INSIGHTS}=        //*[@class="top-navigation__item-link" and @href="/insights"]
${HOW_WE_DO_IT}=    //*[@class="top-navigation__item-link" and @href="/how-we-do-it"]
${ABOUT}=           //*[@class="top-navigation__item-link" and @href="/about"]
${CAREERS}=         //*[@class="top-navigation__item-link" and @href="/careers"]
${SEARCH}=          //*[@class="header-search__button header__icon"]

*** Test Cases ***
1). Testing Header
    [Documentation]    Test page language and translation of links in headers
    [Tags]    header
    Open Epam Website
    Verify language     Global (EN)
    Verify links

2). Testing 'About' page
    [Documentation]    Test About page can be opened
    [Tags]    about
    Open Epam Website
    wait until element is visible    ${ABOUT}
    click link    ${ABOUT}
    location should be    ${ABOUT_URL}

3) Testing Search and count for "Python"
    [Documentation]    Test search and results for Python
    [Tags]    search
    Open Epam Website
    Perform Search          Python
    Verify Search Result    10 RESULTS FOR "PYTHON"

*** Keywords ***
Launch Browser
    open browser    about:blank     ${BROWSER}
    maximize browser window
    log to console    Browser ${BROWSER} opened.
Open Epam Website
    log to console    ${\n}Opening site ${EPAM_URL}
    go to    ${EPAM_URL}
Verify language
    [Arguments]    ${LANGUAGE}
    log to console    ${\n}Checking language is ${LANGUAGE}
    page should contain element    ${LOCATION}
    element text should be          ${LOCATION}    ${LANGUAGE}
Verify links
    log to console    ${\n}Checking links in header
    element text should be    ${SERVICES}        SERVICES
    element text should be    ${HOW_WE_DO_IT}    HOW WE DO IT
    element text should be    ${OUR_WORK}        OUR WORK
    element text should be    ${INSIGHTS}        INSIGHTS
    element text should be    ${ABOUT}           ABOUT
    element text should be    ${CAREERS}         CAREERS
Perform Search
    [Arguments]    ${WORD}
    log to console    ${\n}Performing search for ${WORD}
    wait until element is visible    ${SEARCH}
    click button                     ${SEARCH}
    input text      id:new_form_search      ${WORD}
    click button    Find
Verify Search Result
    [Arguments]    ${SEARCH_RESULT}
    log to console    ${\n}Checking if search result is ${SEARCH_RESULT}
    element text should be    //*[@class="search-results__counter"]    ${SEARCH_RESULT}



