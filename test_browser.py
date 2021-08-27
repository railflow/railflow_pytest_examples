import pytest
 
@pytest.mark.railflow(
    testrail_user="Splint tester",
    description="google test search",
    jira_id=301219,
    test_path="test_browser.py",
    case_fields="field_splint",
    result_fields="field_B2",
    test_mappings="map id2",
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
