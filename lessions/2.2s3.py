from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects2.html')

    sol = str(int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text))

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(sol)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(10)
    browser.quit()
