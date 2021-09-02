import pytest
 
@pytest.mark.railflow(
    jira_ids=301219,
    case_fields="field_splint",
    result_fields="field_B2",
    testrail_ids="map id2",
    case_type="test browser splinter",
    case_priority="important"
)
def test_google(browser):
    """Test using real browser."""
    url = "https://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnK')
    # Interact with elements
    button.click()
    assert browser.is_text_present('splinter.cobrateam.info'), "splinter.cobrateam.info wasn't found... We need to"
    ' improve our SEO techniques'
