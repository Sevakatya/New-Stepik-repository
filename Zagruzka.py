from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Test")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    input3.send_keys("1@gmail.coo")
    input4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
