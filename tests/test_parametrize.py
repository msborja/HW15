import pytest
from selene import browser, be


@pytest.fixture(params=['1920x1080', '1024x768', '1280x1024', '640x960', '480x800', '375x812'])
def browser_configuration(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


desktop_tests = pytest.mark.parametrize(
    'browser_configuration', ['1920x1080', '1024x768', '1280x1024'],
    indirect=True
)

mobile_tests = pytest.mark.parametrize(
    'browser_configuration', ['640x960', '480x800', '375x812'],
    indirect=True
)


@desktop_tests
def test_github_desktop(browser_configuration):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').should(be.clickable).click()


@mobile_tests
def test_github_mobile(browser_configuration):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').should(be.clickable).click()
