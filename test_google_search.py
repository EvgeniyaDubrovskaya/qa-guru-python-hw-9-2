import pytest
from selene.support.shared import browser
from selene import be, have, by
from selenium import webdriver


@pytest.fixture
def setup():
    browser.config.window_height = 1024
    browser.config.window_width = 768
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en-GB')
    browser.config.driver_options = options


@pytest.fixture
def open_start_page(setup):
    browser.open('https://google.com')


def test_search_no_result_page(open_start_page):
    browser.element('[name="q"]').should(be.blank).type('qwertyu dfgh677').press_enter()
    browser.element(by.class_name('mnr-c')).should(have.text('Your search - qwertyu dfgh677 - did not match '
                                                                    'any documents.'))


def test_search_result_page(open_start_page):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
