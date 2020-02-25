from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
    browser.get("https://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    browser.execute_script("window.scrollBy(0, 200);")
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()