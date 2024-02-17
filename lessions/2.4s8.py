from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.TAG_NAME, 'button').click()

    button = browser.find_element(By.ID, 'solve')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    button.click()

finally:
    sleep(10)
    browser.quit()