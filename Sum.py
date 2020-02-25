from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math




try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text


    def calc():
        z = str(int(x) + int(y))
        return z


    z = calc()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()



