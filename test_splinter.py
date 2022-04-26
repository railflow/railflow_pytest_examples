import pytest


@pytest.mark.railflow(
    case_type="Automated",
    case_priority="High"
)
def test_google_two(browser):
    "Testing visiting url"
    url = "https://www.google.com"
    browser.visit(url)
    assert url in browser.url


@pytest.mark.railflow(
    case_type="Automated",
    case_priority="Low"
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
    case_type="Automated",
    case_priority="Low"
)
def test_reload(browser):
    "test reload page"
    url = "https://www.duckduckgo.com"
    browser.visit(url)
    browser.reload()
    assert browser.url == 'https://www.google.com'
