from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
 return str(math.log(abs(12 * math.sin(int(x)))))

try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
        browser.get(link)
        button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        button = browser.find_element_by_class_name("btn.btn-primary")
        button.click()
        browser.execute_script("window.scrollBy(0, 100);")
        x_element = browser.find_element_by_id("input_value")
        x = x_element.text
        y = calc(x)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        button = browser.find_element_by_id("solve")
        button.click()

finally:
    time.sleep(30)
    browser.quit()

