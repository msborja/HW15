import pytest
from selene import browser, be


@pytest.fixture(params=['1920x1080', '1024x768', '1280x1024'])
def desktop_screen_size(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=['640x960', '480x800', '375x812'])
def mobile_screen_size(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


def test_github_desktop(desktop_screen_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').should(be.clickable).click()


def test_github_mobile(mobile_screen_size):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').should(be.clickable).click()
