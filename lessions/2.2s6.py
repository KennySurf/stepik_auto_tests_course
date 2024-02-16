from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/execute_script.html')

    x = browser.find_element(By.ID, 'input_value').text
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element(By.ID, 'robotCheckbox').click()
    robot_rule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);',robot_rule)
    robot_rule.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script('return arguments[0].scrollIntoView(true);',button)
    button.click()
finally:
    sleep(5)
    browser.quit()