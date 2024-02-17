from selenium import webdriver
from selenium.webdriver.common.by import By
from string import ascii_letters as st
from random import choice
import time

count = 0

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/registration2.html')

    inputs = browser.find_elements(By.TAG_NAME, 'input')
    assert len(inputs) == 5, 'not enough fields!!!'

    for input in inputs:
        if count != 3:
            text = [choice(st) for i in range(3)]
            input.send_keys(text)
            count += 1
            continue
        break

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text, 'Error_assert'




finally:
    time.sleep(5)
    browser.quit()
