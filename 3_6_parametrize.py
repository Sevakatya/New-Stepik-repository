import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('linknumber', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_link(browser, linknumber):
    link = f"https://stepik.org/lesson/{linknumber}/step/1"
    browser.get(link)
    answer = math.log(int(time.time() - 1.2))
    input1 = browser.find_element_by_css_selector('.textarea')
    input1.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    message = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" == message.text
