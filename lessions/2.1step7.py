from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/get_attribute.html')

    value_x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(math.log(abs(12*math.sin(int(value_x))))))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    sleep(10)
    browser.quit()