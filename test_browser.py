import os
import pytest


@pytest.mark.railflow(
    jira_ids=["301219"],
    case_fields=[
        {
            "name": "Required text field",
            "value": "Hello from Pytest"
        }
        , {
            "name": "Estimate",
            "value": "10s"
        }
    ],
    result_fields=[
        {
            "name": "Custom field",
            "value": "Result from attributes"
        }
    ],
    case_type="Railflow",
    case_priority="Critical"
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

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # screenshot_path = browser.screenshot(dir_path + '/your_screenshot.png', full=True)
    assert browser.is_text_present(
        'splinter.cobrateam.info'), "splinter.cobrateam.info wasn't found... We need to improve our SEO techniques"
