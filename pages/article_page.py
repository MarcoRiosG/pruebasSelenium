from pages.main_page import MainPage
from selenium import webdriver


class ArticlePage():
    
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://es.wikipedia.org/wiki/Meteorito")
        self.driver.implicitly_wait(2)
        self.TEST_SEARCH = "meteorito"

    def verify_article(self):

        article_name = self.driver.find_element_by_xpath("//h1[@id='firstHeading']").text

        return article_name

    def search_from_article(self):

        self.driver.find_element_by_xpath("//input[@id='searchInput']").send_keys(self.TEST_SEARCH)
        answers_text = []
        suggestions = self.driver.find_elements_by_xpath("//div[@class='suggestions-results']/a")
        for suggestion in suggestions:
            answers_text.append(suggestion.text)

        return answers_text

    def quit_driver(self):
        self.driver.quit()

