import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome, firefox")
    parser.addoption("--language", action="store", default="en", help="Choose language: ru, en")


def init_chrome(options):
    print("\nStart Chrome")
    options_ = Options()
    options_.add_experimental_option('prefs', options)
    chrome = webdriver.Chrome(options=options_)
    return chrome


def init_firefox(options):
    print("\nStart Firefox")
    fp = webdriver.FirefoxProfile()
    for key in options:
        fp.set_preference(key, options[key])
    return webdriver.Firefox(firefox_profile=fp)


@pytest.fixture(scope="function")
def driver(request):
    # Get CLI params
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    # Define browser options
    options = {"intl.accept_languages": language}

    driver = None
    if browser_name == "chrome":
        driver = init_chrome(options)
    elif browser_name == "firefox":
        driver = init_firefox(options)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")
    yield driver

    # Close browser
    print("Quit browser")
    driver.quit()
