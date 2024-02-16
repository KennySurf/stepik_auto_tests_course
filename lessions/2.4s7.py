from selenium import webdriver
from selenium.webdriver.common.by import By
from slenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC
from time import sleep

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/wait2.html")

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify')))
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    sleep(10)
    browser.quit()
