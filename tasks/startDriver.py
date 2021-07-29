from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def oneTimeSetUp(request):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


class SetUpDriver():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def initial_setup(self):
        self.driver.maximize_window()
        self.driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

        return self.driver