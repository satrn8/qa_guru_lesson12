import pytest
from selene.support.conditions import have
from selene.support.shared import browser
url = 'https://github.com/'


@pytest.fixture(scope='function')
def browser_desktop():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1980
    browser.config._window_height = 1080


@pytest.fixture(scope='function')
def browser_mobile():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 390
    browser.config._window_height = 844


def test_github_desktop(browser_desktop):
    browser.open(url)
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_mobile):
    browser.open(url)
    browser.element('.btn-mktg').click()
