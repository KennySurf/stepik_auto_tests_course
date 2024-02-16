from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import choice
from string import ascii_letters as al
import os

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')

    browser.find_element(By.TAG_NAME, 'input').send_keys([choice(al) for i in range(5)])
    browser.find_element(By.NAME, 'lastname').send_keys([choice(al) for i in range(5)])
    browser.find_element(By.NAME, 'email').send_keys(f'{[choice(al) for i in range(5)]}@gmail.com')
    file = browser.find_element(By.CSS_SELECTOR, 'input#file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    sleep(10)
    browser.quit()