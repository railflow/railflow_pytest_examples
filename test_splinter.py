import pytest
 
@pytest.mark.railflow(
    jira_ids=100211,
    case_fields="field_splint",
    result_fields="field_B1",
    testrail_ids="map id1",
    case_type="test browser",
    case_priority="important"
    )
def test_google(browser):
    "Testing visiting url"
    url = "https://www.google.com"
    browser.visit(url)
    assert  url in browser.url
       
        
@pytest.mark.railflow(
    jira_ids=100212,
    case_fields="field_splint",
    result_fields="field_B2",
    testrail_ids="map id2",
    case_type="test browser splinter",
    case_priority="important"
    )
def test_forward(browser):
    "testing forward and backward in browser"
    splint_url = 'https://splinter.readthedocs.io'
    browser.visit('https://www.google.com')
    browser.visit(splint_url)
    browser.back()
    browser.forward()
    assert splint_url in browser.url
    
@pytest.mark.railflow(
    jira_ids=100414,
    case_fields="field_splint reload",
    result_fields="field_B3",
    testrail_ids="map id4",
    case_type="test browser splinter",
    case_priority="important"
    )
def test_reload(browser):
    "test reload page"
    url = "https://www.duckduckgo.com"
    browser.visit(url)
    browser.reload()
    assert browser.url == 'https://www.google.com'

