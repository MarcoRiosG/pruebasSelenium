from selenium import webdriver
# from tasks.startDriver import SetUpDriver

class MainPage():

    TEST_SEARCH = "meteorito"
    TEST_SEARCH2 = "object model"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    def search(self):

        self.driver.find_element_by_xpath("//input[@id='searchInput']").send_keys(self.TEST_SEARCH)
        answers_text = []
        suggestions = self.driver.find_elements_by_xpath("//div[@class='suggestions-results']/a")
        for suggestion in suggestions:
            answers_text.append(suggestion.text)

        return answers_text

    def enter_suggestion(self):

        self.driver.find_element_by_xpath("//div[@class='suggestions-results']/a[1]").click()

    def special_suggestion(self):

        self.driver.find_element_by_xpath("//div[contains(@class,'suggestions-special')]").click()

    def quit_driver(self):
        self.driver.quit()


