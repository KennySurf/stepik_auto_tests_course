import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from math import log
from time import sleep, time

@pytest.fixture(scope='session')
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config

@pytest.fixture(scope='class')
def browser():
    print('\nstarting browser..')
    wbrowser = webdriver.Chrome()
    wbrowser.implicitly_wait(10)
    yield wbrowser
    print('\nbrowser quit..')
    wbrowser.quit()

links = [str(i) for i in range(895, 900)]
links += [str(i) for i in range(903,906)]



class TestLogin():
    def test_autorization(self, browser, load_config):
        print('start first test')
        browser.get('https://stepik.org/lesson/236895/step/1')
        browser.find_element(By.ID, 'ember33').click()
        browser.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys(load_config['login_stepik'])
        browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(load_config['password_stepik'])
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @pytest.mark.parametrize('numbers_of_links', links)
    def test_guest_send_text(self, browser, numbers_of_links):
        sleep(5)
        print('start second test')

        browser.get(f'https://stepik.org/lesson/236{numbers_of_links}/step/1')
        text_area = browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area')
        text_area.send_keys(str(log(int(time()))))
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
        sleep(5)

        optional_fidback = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        assert optional_fidback.text == 'Correct!', optional_fidback.text

