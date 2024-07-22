import pytest
from selene import browser, be


@pytest.fixture(params=['1920x1080', '1024x768', '1280x1024', '640x960', '480x800', '375x812'])
def browser_configuration(request):
    if request.param in ['1920x1080', '1024x768', '1280x1024']:
        width, height = map(int, request.param.split('x'))
        browser.config.window_width = width
        browser.config.window_height = height
        yield 'desktop'
    elif request.param in ['640x960', '480x800', '375x812']:
        width, height = map(int, request.param.split('x'))
        browser.config.window_width = width
        browser.config.window_height = height
        yield 'mobile'

    browser.quit()


def test_github_desktop(browser_configuration):
    if browser_configuration == 'mobile':
        pytest.skip(reason='Не запускаем mobile')

    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').should(be.clickable).click()


def test_github_mobile(browser_configuration):
    if browser_configuration == 'desktop':
        pytest.skip(reason='Не запускаем desktop')

    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').should(be.clickable).click()
