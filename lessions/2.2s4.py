from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    sleep(10)
    browser.quit()