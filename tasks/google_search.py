from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleSearch():

    _word_search = "github"

    def search(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get("https://www.google.com/")

        driver.find_element_by_xpath("//input[@role='combobox']").send_keys(self._word_search)
        driver.find_element_by_xpath("//input[@type='submit'][1]").click()
        driver.implicitly_wait(4)

        answers_texts = []
        for result in range(1, 7):
            if result == 1:
                answers_texts.append(driver.find_element_by_xpath("//div[@id='search']//div[@data-async-context='query:" + self._word_search + "']/div[" + str(result) + "]/div[@class='g']//div[@class='g']//h3"))
            elif result != 2:
                answers_texts.append(driver.find_element_by_xpath("//div[@id='search']//div[@data-async-context='query:" + self._word_search + "']/div[" + str(result) + "]//h3"))

        results_texts = []
        for element in answers_texts:
            results_texts.append(element.text)

        driver.quit()

        return results_texts




