from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/find_xpath_form')

    input1 = browser.find_element(By.XPATH, '//div/input')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.XPATH, '//input[@name = "last_name"]')
    input2.send_keys('Ivanov')
    input3 = browser.find_element(By.XPATH, '//input[@class = "form-control city"]')
    input3.send_keys('Samara')
    input3 = browser.find_element(By.XPATH, '//input[@id = "country"]')
    input3.send_keys('Russia')

    button = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
