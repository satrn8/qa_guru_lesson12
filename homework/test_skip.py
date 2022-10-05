import pytest
from selene.support.shared import browser


url = "https://github.com/"


@pytest.fixture(params=[(1024, 780), (414, 896)])
def browser_window(request):
    return request


@pytest.fixture(scope="function", autouse=True)
def browser_config(browser_window):
    browser.open(url)
    browser.config.window_height = browser_window.param[0]
    browser.config.window_width = browser_window.param[1]


def test_desktop(browser_window):
    if browser.driver.get_window_size()["width"] < 1010:
        pytest.skip('Size for mobile version')
    browser.open(url)
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


def test_mobile():
    if browser.driver.get_window_size()["width"] > 1011:
        pytest.skip('Size for desktop version')
    browser.open(url)
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()

