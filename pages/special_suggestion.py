from pages.main_page import MainPage
from selenium import webdriver

class SpecialSuggestions():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://es.wikipedia.org/w/index.php?search=meteorito&title=Especial%3ABuscar&fulltext=1&ns0=1&ns100=1&ns104=1")
        self.driver.implicitly_wait(2)
        self.TEST_SEARCH = "meteorito"

    def presented_suggestions(self):

        suggestions_titles = []
        titles = self.driver.find_elements_by_xpath("//li[@class='mw-search-result']//a/span")
        for title in titles:
            suggestions_titles.append(title.text)

        suggestions_texts = []
        texts = self.driver.find_elements_by_xpath("//li[@class='mw-search-result']//div/span[1]")
        for text in texts:
            suggestions_texts.append(text.text)

        return suggestions_titles, suggestions_texts

    def big_search_bar(self):

        self.driver.find_element_by_xpath("//div[@id='searchText']/input").clear()
        TEST_SEARCH = "meteorito"
        self.driver.find_element_by_xpath("//div[@id='searchText']/input").send_keys(TEST_SEARCH)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def quit_driver(self):
        self.driver.quit()



