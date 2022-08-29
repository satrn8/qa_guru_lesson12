import pytest
from selene.support.shared import browser

url = "https://github.com/"


@pytest.fixture(scope="function", params=[(1200, 1024)])
def desktop_browser(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]


def test_github_desktop(desktop_browser):
    browser.open(url)
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


@pytest.fixture(scope="function", params=[(414, 896)])
def mobile_browser(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]


def test_github_mobile(mobile_browser):
    browser.open(url)
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()




