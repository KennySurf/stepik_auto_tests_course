from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://suninjuly.github.io/wait1.html')

    browser.find_element(By.ID, 'verify').click()
    v_mess = browser.find_element(By.ID, 'verify_message').text
    assert v_mess == 'Verification was successful!', 'error - ver not success'
finally:
    sleep(10)
    browser.quit()