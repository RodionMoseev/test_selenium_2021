from cgitb import text

from selenium import webdriver

BASE_URL = "https://www.google.ru/"


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_main_page(self):
        self.driver.get(BASE_URL)

    def get_title(self) -> str:
        return self.driver.title

    def search(self):
        element = self.driver.find_element_by_name("q")
        element.clear()
        element.send_keys(text)

    def get_page_source(self) -> str:
        return self.driver.page_source

    def quit(self):
        self.driver.quit()
