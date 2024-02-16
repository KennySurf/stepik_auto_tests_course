from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/alert_accept.html')

    browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    sleep(1)

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.CLASS_NAME,'form-control').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(10)
    browser.quit()