from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')

    x = browser.find_element(By.ID, 'input_value').text

    answer = str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element(By.CSS_SELECTOR, 'div.form-group input')
    input1.send_keys(answer)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, 'div.form-check-custom input')
    robot_checkbox.click()

    correct = browser.find_element(By.CSS_SELECTOR, 'div.form-check #robotsRule')
    correct.click()

    button_send = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_send.click()



finally:
    sleep(5)
    browser.quit()