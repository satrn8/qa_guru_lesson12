import pytest
from selene.support.shared import browser
url = "https://github.com/"


@pytest.fixture(scope='function')
def github_desktop():
    browser.config.browser_name = "chrome"
    browser.config.window_width = 1920
    browser.config.window_height = 1024


@pytest.fixture(scope='function')
def github_mobile():
    browser.config.browser_name = "chrome"
    browser.config.window_width = 414
    browser.config.window_height = 896


def test_desktop(github_desktop):
    browser.open(url)
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


def test_mobile(github_mobile):
    browser.open(url)
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
