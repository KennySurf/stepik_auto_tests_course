import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

#scope: область видимости - в данном примере фикстура будет вызываться только ОДИН раз для класса, можно также выбрать
#function, class, module, session, по названию соответсвтенно один раз для функции и т д
@pytest.fixture(scope='class')
def browser():
    print('\nstart browser for test..')
    wbrowser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    wbrowser.quit()

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")