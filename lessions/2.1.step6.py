from selenium import webdriver
from selemium.webdriver.common.by import By
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')

    people_radio = browser.find_element(By.ID, 'peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('Value of people radio: ' people_checked)

    assert people_checked is not None, "People radio is not selected by default"

finally:
    sleep(10)
    browser.quit()