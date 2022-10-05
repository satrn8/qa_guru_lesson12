import pytest
from selene.support.shared import browser

url = "https://github.com/"


@pytest.fixture(scope='function', params=[(1024, 768)])
def config_browser_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_desktop(config_browser_desktop):
    browser.open(url)
    browser.element('.btn-mktg').click()


@pytest.fixture(scope='function', params=[(390, 844)])
def config_mobile_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_mobile(config_mobile_desktop):
    browser.open(url)
    browser.element('.btn-mktg').click()
