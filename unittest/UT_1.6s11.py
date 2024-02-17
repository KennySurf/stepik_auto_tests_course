from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class TestLayouts(unittest.TestCase):
    def test_layout1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second').send_keys('Ivanov')
        browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third').send_keys('ivan@gmail.com')
        sleep(1)
        browser.find_element(By.TAG_NAME, 'button').click()

        sleep(1)
        self.assertEqual(browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!', 'Invalid TEXT')

        sleep(5)
        browser.quit()

    def test_layout2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

        browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second').send_keys('Ivanov')
        browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third').send_keys('ivan@gmail.com')
        sleep(1)
        browser.find_element(By.TAG_NAME, 'button').click()

        sleep(1)
        self.assertEqual(browser.find_element(By.TAG_NAME, 'h1').text,
                        'Congratulations! You have successfully registered!', 'Invalid TEXT')

        sleep(5)
        browser.quit()
       
if __name__  == '__main__':
    unittest.main()
